use pyo3::prelude::*;
use crate::cercle::Cercle;
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::triangle::Triangle;
use crate::polygon::Polygone;

// --- 1. ENUMÉRATION UNIFIÉE ---
enum Geometrie {
    Cercle(Cercle),
    // Une forme peut être composée de PLUSIEURS morceaux convexes (des triangles)
    Composite(Vec<Vec<(f64, f64)>>), 
}

// --- ALGORYTHME DE TRIANGULATION ROBUSTE (EAR CLIPPING) ---

/// Calcule le produit vectoriel (Cross Product) pour savoir si un angle est convexe
fn produit_vectoriel(a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> f64 {
    (b.0 - a.0) * (c.1 - a.1) - (b.1 - a.1) * (c.0 - a.0)
}

/// Vérifie si un point P est à l'intérieur du triangle ABC
fn point_dans_triangle(p: (f64, f64), a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> bool {
    let cp1 = produit_vectoriel(a, b, p);
    let cp2 = produit_vectoriel(b, c, p);
    let cp3 = produit_vectoriel(c, a, p);
    // Si tous les produits vectoriels ont le même signe, le point est dedans
    (cp1 >= 0.0 && cp2 >= 0.0 && cp3 >= 0.0) || (cp1 <= 0.0 && cp2 <= 0.0 && cp3 <= 0.0)
}

/// Vérifie si le sommet 'i' est une "oreille" (un triangle valide qu'on peut couper)
fn est_une_oreille(points: &Vec<(f64, f64)>, i: usize) -> bool {
    let n = points.len();
    let prev = points[(i + n - 1) % n];
    let curr = points[i];
    let next = points[(i + 1) % n];

    // 1. Vérifier la convexité (l'angle doit être "sortant")
    // Note : On suppose un sens anti-horaire standard. Si c'est horaire, ça peut inverser le signe.
    // Pour être robuste, on vérifie juste que ça ne rentre pas vers l'intérieur de manière aberrante.
    // Ici on simplifie : si le produit vectoriel est négatif, c'est un angle rentrant (concave).
    // (Ajustement selon le système de coordonnées, ici standard maths).
    if produit_vectoriel(prev, curr, next) <= 0.0 {
        return false;
    }

    // 2. Vérifier qu'aucun autre point du polygone n'est DANS ce triangle
    // Sinon ce n'est pas une oreille, c'est une bouche !
    for j in 0..n {
        if j == i || j == (i + n - 1) % n || j == (i + 1) % n {
            continue; // On ignore les sommets du triangle lui-même
        }
        if point_dans_triangle(points[j], prev, curr, next) {
            return false;
        }
    }

    true
}

/// Algorithme principal : Ear Clipping
fn trianguler(points_input: &Vec<(f64, f64)>) -> Vec<Vec<(f64, f64)>> {
    let mut triangles = Vec::new();
    // On travaille sur une copie modifiable de la liste des points
    let mut poly = points_input.clone();

    // Sécurité : On s'assure que le polygone est dans le sens anti-horaire (Counter-Clockwise)
    // Sinon l'algorithme Ear Clipping ne marchera pas.
    // Calcul de l'aire signée
    let mut area = 0.0;
    for i in 0..poly.len() {
        let j = (i + 1) % poly.len();
        area += (poly[j].0 - poly[i].0) * (poly[j].1 + poly[i].1);
    }
    // Si aire positive (dans ce calcul spécifique), c'est souvent Horaire en coordonnées écran.
    // On inverse si nécessaire pour standardiser.
    if area > 0.0 {
        poly.reverse();
    }

    // Boucle de découpage
    let mut error_count = 0;
    while poly.len() >= 3 {
        let n = poly.len();
        let mut ear_found = false;

        for i in 0..n {
            if est_une_oreille(&poly, i) {
                // On a trouvé une oreille ! On crée le triangle.
                let prev = poly[(i + n - 1) % n];
                let curr = poly[i];
                let next = poly[(i + 1) % n];
                
                triangles.push(vec![prev, curr, next]);
                
                // On coupe l'oreille (on retire le sommet)
                poly.remove(i);
                ear_found = true;
                break; // On recommence la boucle principale
            }
        }

        if !ear_found {
            // Cas de secours : Si la géométrie est trop tordue et qu'on ne trouve pas d'oreille,
            // on force un découpage pour éviter une boucle infinie, ou on arrête.
            // Pour ce projet, on arrête.
            error_count += 1;
            if error_count > 3 { break; } // Sécurité anti-boucle infinie
        }
    }

    triangles
}


// --- 2. FONCTIONS UTILITAIRES (HELPER) ---

fn extraire_forme(obj: &Bound<'_, PyAny>) -> PyResult<Geometrie> {
    // A. CERCLE
    if let Ok(c) = obj.extract::<Cercle>() {
        return Ok(Geometrie::Cercle(c));
    }

    // B. POLYGONE
    if let Ok(p) = obj.extract::<Polygone>() {
        let points_py: Vec<(f64, f64)> = obj.getattr("points")?.extract()?;
        let sous_formes = trianguler(&points_py);
        return Ok(Geometrie::Composite(sous_formes));
    }

    // C. RECTANGLE / CARRÉ / TRIANGLE
    let pts = if let Ok(r) = obj.extract::<Rectangle>() {
        vec![(r.x, r.y), (r.x + r.largeur, r.y), (r.x + r.largeur, r.y + r.hauteur), (r.x, r.y + r.hauteur)]
    } else if let Ok(t) = obj.extract::<Triangle>() {
        vec![(t.ax, t.ay), (t.bx, t.by), (t.cx, t.cy)]
    } else if let Ok(c) = obj.extract::<Carre>() {
        vec![(c.x, c.y), (c.x + c.cote, c.y), (c.x + c.cote, c.y + c.cote), (c.x, c.y + c.cote)]
    } else {
        return Err(pyo3::exceptions::PyTypeError::new_err("Forme non supportée"));
    };

    Ok(Geometrie::Composite(vec![pts]))
}


// --- 3. MOTEUR SAT (Separating Axis Theorem) ---

fn dot(v1: (f64, f64), v2: (f64, f64)) -> f64 {
    v1.0 * v2.0 + v1.1 * v2.1
}

fn project(shape: &Vec<(f64, f64)>, axis: (f64, f64)) -> (f64, f64) {
    let mut min = dot(shape[0], axis);
    let mut max = min;
    for i in 1..shape.len() {
        let p = dot(shape[i], axis);
        if p < min { min = p; }
        if p > max { max = p; }
    }
    (min, max)
}

fn overlap(p1: (f64, f64), p2: (f64, f64)) -> bool {
    !(p1.1 < p2.0 || p2.1 < p1.0)
}

fn sat_poly_poly(p1: &Vec<(f64, f64)>, p2: &Vec<(f64, f64)>) -> bool {
    let shapes = [p1, p2];
    for shape in shapes.iter() {
        for i in 0..shape.len() {
            let p_curr = shape[i];
            let p_next = shape[(i + 1) % shape.len()];
            let edge = (p_next.0 - p_curr.0, p_next.1 - p_curr.1);
            let axis = (-edge.1, edge.0);
            let proj1 = project(p1, axis);
            let proj2 = project(p2, axis);
            if !overlap(proj1, proj2) { return false; }
        }
    }
    true
}

fn sat_poly_cercle(poly: &Vec<(f64, f64)>, c: &Cercle) -> bool {
    let mut closest_point = poly[0];
    let mut min_dist_sq = f64::MAX;

    for i in 0..poly.len() {
        let p_curr = poly[i];
        let p_next = poly[(i + 1) % poly.len()];
        let dx = c.centre_x - p_curr.0;
        let dy = c.centre_y - p_curr.1;
        let d_sq = dx*dx + dy*dy;
        if d_sq < min_dist_sq { min_dist_sq = d_sq; closest_point = p_curr; }

        let edge = (p_next.0 - p_curr.0, p_next.1 - p_curr.1);
        let axis = (-edge.1, edge.0);
        let (min_p, max_p) = project(poly, axis);
        let axis_len = (axis.0.powi(2) + axis.1.powi(2)).sqrt();
        let proj_c = dot((c.centre_x, c.centre_y), axis);
        let min_c = proj_c - c.rayon * axis_len;
        let max_c = proj_c + c.rayon * axis_len;

        if !overlap((min_p, max_p), (min_c, max_c)) { return false; }
    }

    let axis = (closest_point.0 - c.centre_x, closest_point.1 - c.centre_y);
    let axis_len = (axis.0.powi(2) + axis.1.powi(2)).sqrt();
    if axis_len > 1e-9 {
        let (min_p, max_p) = project(poly, axis);
        let proj_c = dot((c.centre_x, c.centre_y), axis);
        let min_c = proj_c - c.rayon * axis_len;
        let max_c = proj_c + c.rayon * axis_len;
        if !overlap((min_p, max_p), (min_c, max_c)) { return false; }
    }
    true
}

// --- 4. FONCTION PRINCIPALE ---

#[pyfunction]
#[pyo3(signature = (forme_a, forme_b, mode="bool"))]
pub fn intersecte(forme_a: &Bound<'_, PyAny>, forme_b: &Bound<'_, PyAny>, mode: &str) -> PyResult<bool> {
    if mode != "bool" { return Err(pyo3::exceptions::PyValueError::new_err("Mode non supporté")); }
    let g1 = extraire_forme(forme_a)?;
    let g2 = extraire_forme(forme_b)?;

    let result = match (g1, g2) {
        (Geometrie::Composite(liste_a), Geometrie::Composite(liste_b)) => {
            for partie_a in &liste_a {
                for partie_b in &liste_b {
                    if sat_poly_poly(partie_a, partie_b) { return Ok(true); }
                }
            }
            false
        },
        (Geometrie::Composite(liste_a), Geometrie::Cercle(c)) => {
            for partie_a in &liste_a {
                if sat_poly_cercle(partie_a, &c) { return Ok(true); }
            }
            false
        },
        (Geometrie::Cercle(c), Geometrie::Composite(liste_a)) => {
            for partie_a in &liste_a {
                if sat_poly_cercle(partie_a, &c) { return Ok(true); }
            }
            false
        },
        (Geometrie::Cercle(c1), Geometrie::Cercle(c2)) => {
             let dx = c1.centre_x - c2.centre_x;
             let dy = c1.centre_y - c2.centre_y;
             (dx*dx + dy*dy) < (c1.rayon + c2.rayon).powi(2)
        }
    };
    Ok(result)
}
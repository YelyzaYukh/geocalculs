use pyo3::prelude::*;
use crate::cercle::Cercle;
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::triangle::Triangle;
use crate::polygon::Polygone;

/// Type enum pour identifier ce que l'utilisateur envoie
enum Geometrie {
    Cercle(Cercle),
    Composite(Vec<Vec<(f64, f64)>>), 
}

/// Helper pour convertir un Carré en Rectangle (car la logique est la même)
fn carre_vers_rect(c: &Carre) -> Rectangle {
    Rectangle { x: c.x, y: c.y, largeur: c.cote, hauteur: c.cote }
}

/// Helper pour extraire la forme depuis un objet Python générique
// Remplace toute la fonction extraire_forme par celle-ci :

fn extraire_forme(obj: &Bound<'_, PyAny>) -> PyResult<Geometrie> {
    // 1. CERCLE
    if let Ok(c) = obj.extract::<Cercle>() {
        return Ok(Geometrie::Cercle(c));
    }

    // 2. POLYGONE
//  POLYGONE
    if let Ok(p) = obj.extract::<Polygone>() {

        let points_py = p.points.clone(); 
        
        let sous_formes = trianguler(&points_py);
        return Ok(Geometrie::Composite(sous_formes));
    }

    // 3. RECTANGLE
    if let Ok(r) = obj.extract::<Rectangle>() {
        let pts = vec![
            (r.x, r.y),
            (r.x + r.largeur, r.y),
            (r.x + r.largeur, r.y + r.hauteur),
            (r.x, r.y + r.hauteur),
        ];
        return Ok(Geometrie::Composite(vec![pts]));
    }

    // 4. CARRÉ
    if let Ok(c) = obj.extract::<Carre>() {
        let pts = vec![
            (c.x, c.y),
            (c.x + c.cote, c.y),
            (c.x + c.cote, c.y + c.cote),
            (c.x, c.y + c.cote),
        ];
        return Ok(Geometrie::Composite(vec![pts]));
    }

    // 5. TRIANGLE
    if let Ok(t) = obj.extract::<Triangle>() {
        let pts = vec![
            (t.ax, t.ay),
            (t.bx, t.by),
            (t.cx, t.cy),
        ];
        return Ok(Geometrie::Composite(vec![pts]));
    }

    let type_name = obj.get_type().name()?;
    Err(pyo3::exceptions::PyTypeError::new_err(format!(
        "Type de forme non supporté pour l'intersection : {}", type_name
    )))
}





// --- ALGORYTHME DE TRIANGULATION (EAR CLIPPING) ---

/// Calcule le produit vectoriel (Cross Product)
fn produit_vectoriel(a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> f64 {
    (b.0 - a.0) * (c.1 - a.1) - (b.1 - a.1) * (c.0 - a.0)
}

/// Vérifie si un point P est à l'intérieur du triangle ABC
fn point_dans_triangle(p: (f64, f64), a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> bool {
    let cp1 = produit_vectoriel(a, b, p);
    let cp2 = produit_vectoriel(b, c, p);
    let cp3 = produit_vectoriel(c, a, p);
    (cp1 >= 0.0 && cp2 >= 0.0 && cp3 >= 0.0) || (cp1 <= 0.0 && cp2 <= 0.0 && cp3 <= 0.0)
}

/// Vérifie si le sommet 'i' est une "oreille"
fn est_une_oreille(points: &Vec<(f64, f64)>, i: usize) -> bool {
    let n = points.len();
    let prev = points[(i + n - 1) % n];
    let curr = points[i];
    let next = points[(i + 1) % n];

    if produit_vectoriel(prev, curr, next) <= 0.0 {
        return false;
    }

    for j in 0..n {
        if j == i || j == (i + n - 1) % n || j == (i + 1) % n {
            continue;
        }
        if point_dans_triangle(points[j], prev, curr, next) {
            return false;
        }
    }
    true
}

fn collide_rect_rect(r1: &Rectangle, r2: &Rectangle) -> bool {
    // Logique AABB (Axis-Aligned Bounding Box)
    r1.x < r2.x + r2.largeur &&
    r1.x + r1.largeur > r2.x &&
    r1.y < r2.y + r2.hauteur &&
    r1.y + r1.hauteur > r2.y
}

fn collide_cercle_cercle(c1: &Cercle, c2: &Cercle) -> bool {
    let dx = c1.centre_x - c2.centre_x;
    let dy = c1.centre_y - c2.centre_y;
    let distance_sq = dx*dx + dy*dy;
    let rayons_sum = c1.rayon + c2.rayon;
    distance_sq < rayons_sum * rayons_sum
}

fn collide_rect_cercle(rect: &Rectangle, cerc: &Cercle) -> bool {
    // Trouver le point du rectangle le plus proche du centre du cercle
    // clamp(value, min, max)
    let closest_x = cerc.centre_x.max(rect.x).min(rect.x + rect.largeur);
    let closest_y = cerc.centre_y.max(rect.y).min(rect.y + rect.hauteur);

    let dx = cerc.centre_x - closest_x;
    let dy = cerc.centre_y - closest_y;

    (dx*dx + dy*dy) < (cerc.rayon * cerc.rayon)
}

fn trianguler(points_input: &Vec<(f64, f64)>) -> Vec<Vec<(f64, f64)>> {
    let mut triangles = Vec::new();
    let mut poly = points_input.clone();

    // Standardisation sens anti-horaire
    let mut area = 0.0;
    for i in 0..poly.len() {
        let j = (i + 1) % poly.len();
        area += (poly[j].0 - poly[i].0) * (poly[j].1 + poly[i].1);
    }
    if area > 0.0 { poly.reverse(); }

    let mut error_count = 0;
    while poly.len() >= 3 {
        let n = poly.len();
        let mut ear_found = false;

        for i in 0..n {
            if est_une_oreille(&poly, i) {
                let prev = poly[(i + n - 1) % n];
                let curr = poly[i];
                let next = poly[(i + 1) % n];
                
                triangles.push(vec![prev, curr, next]);
                poly.remove(i);
                ear_found = true;
                break;
            }
        }

        if !ear_found {
            error_count += 1;
            if error_count > 3 { break; }
            // Si pas d'oreille trouvée (forme très complexe), on force la sortie
            if poly.len() >= 3 {
                 triangles.push(vec![poly[0], poly[1], poly[2]]);
                 poly.remove(1);
            }
        }
    }
    triangles
}


// --- MOTEUR SAT---

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
    let epsilon = 1e-9;
    !(p1.1 < p2.0 - epsilon || p2.1 < p1.0 - epsilon)
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

// --- FONCTION PRINCIPALE EXPOSÉE ---

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
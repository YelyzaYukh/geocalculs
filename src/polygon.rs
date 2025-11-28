use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;

/// Une classe représentant un polygone arbitraire défini par une liste de points.
#[pyclass]
#[derive(Clone)]
pub struct Polygone {
    #[pyo3(get, set)]
    pub points: Vec<(f64, f64)>,
}

#[pymethods]
impl Polygone {
    #[new]
    fn new(points: Vec<(f64, f64)>) -> PyResult<Self> {
        let n = points.len();
        if n < 3 {
            return Err(PyValueError::new_err("Un polygone doit avoir au moins 3 points."));
        }

        // --- VALIDATION 1 : Points Colinéaires ---
        for i in 0..n {
            let p1 = points[i];
            let p2 = points[(i + 1) % n];
            let p3 = points[(i + 2) % n];

            if sont_colineaires(p1, p2, p3) {
                return Err(PyValueError::new_err(format!(
                    "Points colinéaires détectés aux indices {}, {}, {}. Le polygone est invalide.",
                    i, (i + 1) % n, (i + 2) % n
                )));
            }
        }

        // --- VALIDATION 2 : Auto-Intersection ---
        // On compare chaque segment (i) avec tous les autres segments (j)
        // Complexité O(N^2) - Acceptable pour N < 1000
        for i in 0..n {
            let p1 = points[i];
            let p2 = points[(i + 1) % n]; // Segment A

            // On commence j à i+2 pour ne pas tester le segment contre lui-même
            // ou son voisin immédiat (qui se touchent forcément par un sommet)
            for j in (i + 2)..n {
                // Cas particulier : Si on teste le dernier segment contre le premier
                if i == 0 && j == n - 1 { continue; }

                let p3 = points[j];
                let p4 = points[(j + 1) % n]; // Segment B

                if segments_se_croisent(p1, p2, p3, p4) {
                    return Err(PyValueError::new_err("Le polygone s'auto-intersecte (croisement de lignes)."));
                }
            }
        }

        Ok(Polygone { points })
    }

    fn perimetre(&self) -> f64 {
        let n = self.points.len();
        let mut perim = 0.0;
        for i in 0..n {
            let (x1, y1) = self.points[i];
            let (x2, y2) = self.points[(i + 1) % n];
            perim += ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();
        }
        perim
    }

    fn surface(&self) -> f64 {
        let n = self.points.len();
        let mut somme1 = 0.0;
        let mut somme2 = 0.0;
        for i in 0..n {
            let (x1, y1) = self.points[i];
            let (x2, y2) = self.points[(i + 1) % n];
            somme1 += x1 * y2;
            somme2 += x2 * y1;
        }
        (somme1 - somme2).abs() / 2.0
    }
    
    fn nombre_de_sommets(&self) -> usize {
        self.points.len()
    }
}

// --- FONCTIONS UTILITAIRES PRIVÉES (Géométrie pure) ---

/// Vérifie si 3 points sont alignés (colinéaires)
fn sont_colineaires(p1: (f64, f64), p2: (f64, f64), p3: (f64, f64)) -> bool {
    // Calcul de l'aire signée du triangle formé par les 3 points (Produit en croix)
    // Si l'aire est ~0, ils sont alignés.
    let val = (p2.0 - p1.0) * (p3.1 - p1.1) - (p2.1 - p1.1) * (p3.0 - p1.0);
    val.abs() < 1e-9 // Tolérance epsilon pour les flottants
}

/// Vérifie l'orientation de 3 points (0: colinéaire, 1: horaire, 2: anti-horaire)
fn orientation(p: (f64, f64), q: (f64, f64), r: (f64, f64)) -> i32 {
    let val = (q.1 - p.1) * (r.0 - q.0) - (q.0 - p.0) * (r.1 - q.1);
    if val.abs() < 1e-9 { return 0; } // Colinéaire
    if val > 0.0 { 1 } else { 2 } // Horaire ou Anti-horaire
}

/// Vérifie si le point q est sur le segment pr
fn sur_segment(p: (f64, f64), q: (f64, f64), r: (f64, f64)) -> bool {
    q.0 <= p.0.max(r.0) && q.0 >= p.0.min(r.0) &&
    q.1 <= p.1.max(r.1) && q.1 >= p.1.min(r.1)
}

/// Vérifie si le segment p1q1 croise le segment p2q2
fn segments_se_croisent(p1: (f64, f64), q1: (f64, f64), p2: (f64, f64), q2: (f64, f64)) -> bool {
    let o1 = orientation(p1, q1, p2);
    let o2 = orientation(p1, q1, q2);
    let o3 = orientation(p2, q2, p1);
    let o4 = orientation(p2, q2, q1);

    // Cas général : ils se croisent franchement
    if o1 != o2 && o3 != o4 {
        return true;
    }

    // Cas particuliers (points sur les segments) - considérés comme intersection ici
    if o1 == 0 && sur_segment(p1, p2, q1) { return true; }
    if o2 == 0 && sur_segment(p1, q2, q1) { return true; }
    if o3 == 0 && sur_segment(p2, p1, q2) { return true; }
    if o4 == 0 && sur_segment(p2, q1, q2) { return true; }

    false
}
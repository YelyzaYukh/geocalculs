use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Rectangle {
    #[pyo3(get, set)]
    pub x: f64,         // Coin "origine" (souvent bas-gauche ou haut-gauche selon convention)
    #[pyo3(get, set)]
    pub y: f64,
    #[pyo3(get, set)]
    pub largeur: f64,
    #[pyo3(get, set)]
    pub hauteur: f64,
}

#[pymethods]
impl Rectangle {
    // --- 1. CONSTRUCTEUR STANDARD ---
    // Usage Python : g.Rectangle(x, y, largeur, hauteur)
    #[new]
    fn new_py(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les dimensions doivent être strictement positives.",
            ));
        }
        Ok(Self { x, y, largeur, hauteur })
    }

    // --- 2. CONSTRUCTEUR PAR COINS OPPOSÉS (Nouveau) ---
    // Usage Python : g.Rectangle.from_corners(x1, y1, x2, y2)
    // Utile quand on a deux points de souris (drag & drop)
    #[staticmethod]
    fn from_corners(x1: f64, y1: f64, x2: f64, y2: f64) -> PyResult<Self> {
        let x = x1.min(x2); // On prend le minimum pour trouver le coin origine
        let y = y1.min(y2);
        let largeur = (x1 - x2).abs();
        let hauteur = (y1 - y2).abs();

        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les points ne doivent pas être identiques (largeur ou hauteur nulle).",
            ));
        }

        Ok(Self { x, y, largeur, hauteur })
    }

    // --- 3. CONSTRUCTEUR PAR LE CENTRE (Nouveau) ---
    // Usage Python : g.Rectangle.from_center(cx, cy, largeur, hauteur)
    // Utile pour la physique ou le placement d'objets centrés
    #[staticmethod]
    fn from_center(cx: f64, cy: f64, largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les dimensions doivent être strictement positives.",
            ));
        }
        
        let x = cx - (largeur / 2.0);
        let y = cy - (hauteur / 2.0);

        Ok(Self { x, y, largeur, hauteur })
    }

    // --- MÉTHODES CLASSIQUES ---

    pub fn perimetre(&self) -> f64 {
        2.0 * (self.largeur + self.hauteur)
    }

    pub fn surface(&self) -> f64 {
        self.largeur * self.hauteur
    }
}

// --- FONCTION UTILITAIRE EXTERNE ---
#[pyfunction]
pub fn definir_rectangle(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<String> {
    let rect = Rectangle::new_py(x, y, largeur, hauteur)?;
    Ok(format!(
        "Rectangle en ({}, {}) : {}x{}",
        rect.x, rect.y, rect.largeur, rect.hauteur
    ))
}
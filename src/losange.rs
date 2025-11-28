use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct Losange {
    #[pyo3(get, set)]
    pub x: f64,
    #[pyo3(get, set)]
    pub y: f64,

    #[pyo3(get, set)]
    pub largeur: f64,

    #[pyo3(get, set)]
    pub hauteur: f64,
}

#[pymethods]
impl Losange {
    #[new]
    pub fn new(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "La largeur et la hauteur doivent être strictement positives",
            ));
        }

        Ok(Self { x, y, largeur, hauteur })
    }

    /// Surface : (largeur * hauteur) / 2
    pub fn surface(&self) -> f64 {
        (self.largeur * self.hauteur) / 2.0
    }

    /// Périmètre : 4 * côté (supposé losange régulier)
    pub fn perimetre(&self) -> f64 {
        // Formule approchée du côté à partir des demi-diagonales
        let a = self.largeur / 2.0;
        let b = self.hauteur / 2.0;
        let cote = (a * a + b * b).sqrt();
        4.0 * cote
    }

    pub fn description(&self) -> String {
        format!(
            "Losange(centre=({}, {}), largeur={}, hauteur={})",
            self.x, self.y, self.largeur, self.hauteur
        )
    }
}
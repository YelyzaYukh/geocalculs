use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// Représentation d’un carré
#[pyclass]
#[derive(Debug, Clone)]
pub struct Carre {
    #[pyo3(get, set)]
    pub x: f64,      // coordonnée X du coin supérieur gauche
    #[pyo3(get, set)]
    pub y: f64,      // coordonnée Y du coin supérieur gauche
    #[pyo3(get, set)]
    pub cote: f64,   // longueur du côté
}

#[pymethods]
impl Carre {
    #[new]
    fn new(x: f64, y: f64, cote: f64) -> PyResult<Self> {
        if cote < 0.0 {
            return Err(PyValueError::new_err("Le côté doit être positif."));
        }
        Ok(Self { x, y, cote })
    }

    /// Calcule le périmètre du carré
    pub fn perimetre(&self) -> f64 {
        4.0 * self.cote
    }

    /// Calcule la surface du carré
    pub fn surface(&self) -> f64 {
        self.cote.powi(2)
    }
}
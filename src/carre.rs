use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// Représentation d’un carré
#[pyclass]
#[derive(Debug, Clone)]
pub struct Carre {
    #[pyo3(get, set)]
    pub x: f64, // coordonnée X du coin supérieur gauche optionnel
    #[pyo3(get, set)]
    pub y: f64, // coordonnée Y du coin supérieur gauche optionnel
    #[pyo3(get, set)]
    pub cote: f64,   // longueur du côté
}

#[pymethods]
impl Carre {
    #[new]
    fn new(x: Option<f64>, y: Option<f64>, cote: f64) -> PyResult<Self> {
        // Default values 0.0 if not provided
        let x_val = x.unwrap_or(0.0);
        let y_val = y.unwrap_or(0.0);

        if cote < 0.0 {
            return Err(PyValueError::new_err("Le côté doit être positif."));
        }
        if x_val < 0.0 || y_val < 0.0 {
            return Err(PyValueError::new_err("Les coordonnées du coin supérieur gauche doivent être positives."));
        }
        Ok(Self { x: x_val, y: y_val, cote })
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
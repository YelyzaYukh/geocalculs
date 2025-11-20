use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// Représentation d´un cercle par :
/// - centre_x : coordonnée X du centre
/// - centre_y : coordonnée Y du centre
/// - rayon : rayon du cercle (doit être positif)
#[pyclass]
#[derive(Debug, Clone)]
pub struct Cercle {
    #[pyo3(get, set)]
    pub centre_x: f64,
    #[pyo3(get, set)]
    pub centre_y: f64,
    #[pyo3(get, set)]
    pub rayon: f64,
}

#[pymethods]
impl Cercle {
    #[new]
    fn new(centre_x: f64, centre_y: f64, rayon: f64) -> PyResult<Self> {
        if rayon < 0.0 {
            return Err(PyValueError::new_err("Le rayon ne peut pas être négatif."));
        }

        Ok(Self {
            centre_x,
            centre_y,
            rayon,
        })
    }

    //calcule le pérmiétre d'un cercle
    pub fn perimetre(&self) -> f64 {
        2.0 * std::f64::consts::PI * self.rayon
    }

    //calcule la surface d'un cercle
    pub fn surface(&self) -> f64 {
        std::f64::consts::PI * self.rayon.powi(2)
    }
}
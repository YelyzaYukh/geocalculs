/// function qui calcule la distances entre deux point en donnant 
/// les cordonnée des deux points
///
use pyo3::prelude::*;




#[pyfunction]
pub fn distance_2d(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt()
}
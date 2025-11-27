pub mod point_distance;
pub mod carre_distance;
pub mod rectangle_distance;
pub mod triangle_distance;
pub mod cercle_distance;
pub mod polygon_distance;
pub mod losange_distance;
pub mod segment_distance;

pub use segment_distance::dist_segment_point;
use pyo3::prelude::*;
use pyo3::exceptions::PyTypeError;


/// Fonction centrale python : distance_formes(A, B)
#[pyfunction]
pub fn distance_formes(a: &Bound<'_, PyAny>, b: &Bound<'_, PyAny>) -> PyResult<f64> {
    // On complétera ici après avoir fini tous les modules
    Err(PyTypeError::new_err(
        "distance_formes() pas encore implémenté."
    ))
}

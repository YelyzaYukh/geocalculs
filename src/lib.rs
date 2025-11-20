use pyo3::prelude::*;

mod distance;
mod shapes;
mod triangle;
mod rectangle;

/// A Python module implemented in Rust.
#[pymodule]
fn geocalculs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Rectangle
    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(rectangle::definir_rectangle, m)?)?;


    // Distance
    m.add_function(wrap_pyfunction!(distance::distance_2d, m)?)?;

    // Cercle
    m.add_function(wrap_pyfunction!(shapes::perimetre_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_cercle, m)?)?;

    // Triangle
    m.add_function(wrap_pyfunction!(shapes::perimetre_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(triangle::definir_triangle, m)?)?;

    Ok(())
}

use pyo3::prelude::*;

mod distance;
mod shapes;
/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn geocalculs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle,m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_ractangle,m)?)?;
    m.add_function(wrap_pyfunction!(distance::distance_2d,m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle,m)?)?;
    Ok(())
}


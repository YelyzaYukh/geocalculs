use pyo3::prelude::*;

mod distance;
mod shapes;
mod triangle;
mod rectangle;

mod cercle;
mod polygon;
mod validation;
mod losange;


/// A Python module implemented in Rust.
#[pymodule]
fn geocalculs(m: &Bound<'_, PyModule>) -> PyResult<()> {

    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(rectangle::definir_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distance::distance_2d,m)?)?;
    m.add_function(wrap_pyfunction!(shapes::perimetre_triangle,m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_triangle,m)?)?;

    m.add_class::<cercle::Cercle>()?;

    m.add_class::<polygon::Polygone>()?;
    m.add_function(wrap_pyfunction!(validation::valider_valeurs, m)?)?;
    m.add_function(wrap_pyfunction!(validation::valider_triangle, m)?)?;
    m.add_class::<losange::Losange>()?;


    // Cercle
    m.add_function(wrap_pyfunction!(shapes::perimetre_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_cercle, m)?)?;

    // Triangle
    m.add_function(wrap_pyfunction!(shapes::perimetre_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(triangle::definir_triangle, m)?)?;

    Ok(())
}

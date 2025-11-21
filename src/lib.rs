use pyo3::prelude::*;

mod distance;
mod shapes;
mod triangle;
mod rectangle;
mod cercle;
mod polygon;
mod validation;
mod losange;
mod carre;
mod appartenance;

#[pymodule]
fn geocalculs(m: &Bound<'_, PyModule>) -> PyResult<()> {

    // Fonctions rectangle
    m.add_function(wrap_pyfunction!(rectangle::definir_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle, m)?)?;

    // Autres fonctions
    m.add_function(wrap_pyfunction!(distance::distance_2d, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::perimetre_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_triangle, m)?)?;

    // Classes
    m.add_class::<rectangle::Rectangle>()?;
    m.add_class::<cercle::Cercle>()?;
    m.add_class::<polygon::Polygone>()?;
    m.add_class::<losange::Losange>()?;
    m.add_class::<triangle::Triangle>()?;
    m.add_class::<carre::Carre>()?;

    // Validation
    m.add_function(wrap_pyfunction!(validation::valider_valeurs, m)?)?;
    m.add_function(wrap_pyfunction!(validation::valider_triangle, m)?)?;

    //Appartennance
    m.add_function(wrap_pyfunction!(appartenance::appartient, m)?)?;

    Ok(())
}

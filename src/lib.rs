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
mod helpers;
mod intersection;
mod distances;
mod appartenance;

#[pymodule]
fn geocalculs(m: &Bound<'_, PyModule>) -> PyResult<()> {

    // Rectangle
    m.add_function(wrap_pyfunction!(rectangle::definir_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle, m)?)?;

    // Fonctions géométriques classiques
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

    // Helpers
    m.add_class::<helpers::Point>()?;
    m.add_class::<helpers::AABB>()?;
    m.add_function(wrap_pyfunction!(helpers::orientation, m)?)?;
    m.add_function(wrap_pyfunction!(helpers::on_segment, m)?)?;

    // Intersections
    m.add_function(wrap_pyfunction!(intersection::intersecte, m)?)?;
    m.add_function(wrap_pyfunction!(appartenance::appartient, m)?)?;

    // DISTANCES — CARRÉ
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_carre_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_carre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_carre_carre, m)?)?;
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_carre_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_carre_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::carre_distance::dist_point_carre, m)?)?;

    // DISTANCES — RECTANGLE
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_rect_rect, m)?)?;
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_point_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_rectangle_carre, m)?)?;
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_rectangle_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_rectangle_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::rectangle_distance::dist_rectangle_polygone, m)?)?;

    // DISTANCES — TRIANGLE
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_point_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_triangle_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_triangle_carre, m)?)?;
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_triangle_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_triangle_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::triangle_distance::dist_triangle_polygone, m)?)?;

    // DISTANCES — CERCLE
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_point_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_cercle_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_cercle_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_cercle_carre, m)?)?;
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_cercle_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::cercle_distance::dist_cercle_polygone, m)?)?;

    // DISTANCES — POLYGONE
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_carre_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_rectangle_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_cercle_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_triangle_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_poly_poly, m)?)?;
    m.add_function(wrap_pyfunction!(distances::polygon_distance::dist_point_polygone, m)?)?;


    // DISTANCES — LOSANGE
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_point_losange, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_carre, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_polygone, m)?)?;
    m.add_function(wrap_pyfunction!(distances::losange_distance::dist_losange_losange, m)?)?;

    Ok(())
}

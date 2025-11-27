use pyo3::prelude::*;

///
/// Distance entre un segment AB et un point P
/// Formel : projection + clamp.
///
#[pyfunction]
pub fn dist_segment_point(
    ax: f64, ay: f64,
    bx: f64, by: f64,
    px: f64, py: f64
) -> f64 {

    let abx = bx - ax;
    let aby = by - ay;

    let apx = px - ax;
    let apy = py - ay;

    let ab2 = abx * abx + aby * aby;

    if ab2 == 0.0 {
        // A et B confondus → distance point-A
        return ((px - ax).powi(2) + (py - ay).powi(2)).sqrt();
    }

    // t = projection normalisée sur AB
    let t = (apx * abx + apy * aby) / ab2;

    // Clamp t à [0,1]
    let t_clamped = if t < 0.0 { 0.0 } else if t > 1.0 { 1.0 } else { t };

    let proj_x = ax + t_clamped * abx;
    let proj_y = ay + t_clamped * aby;

    ((px - proj_x).powi(2) + (py - proj_y).powi(2)).sqrt()
}

use pyo3::prelude::*;

/// Struct Point
#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct Point {
    #[pyo3(get, set)]
    pub x: f64,
    #[pyo3(get, set)]
    pub y: f64,
}

#[pymethods]
impl Point {
    #[new]
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }
}

/// Helper 1 : orientation(A, B, C)

#[pyfunction]
pub fn orientation(a: &Point, b: &Point, c: &Point) -> i32 {
    let val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y);

    if val.abs() < 1e-9 {
        0
    } else if val > 0.0 {
        1
    } else {
        2
    }
}

/// -----------------------------------------------------------
/// Helper 2 : on_segment(A, B, C)
/// -----------------------------------------------------------
/// Vérifie si C est sur le segment AB
/// -----------------------------------------------------------
#[pyfunction]
pub fn on_segment(a: &Point, b: &Point, c: &Point) -> bool {
    (c.x >= a.x.min(b.x) - 1e-9)
        && (c.x <= a.x.max(b.x) + 1e-9)
        && (c.y >= a.y.min(b.y) - 1e-9)
        && (c.y <= a.y.max(b.y) + 1e-9)
}

/// -----------------------------------------------------------
/// Helper 3 : AABB → Axis Aligned Bounding Box
/// -----------------------------------------------------------
#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct AABB {
    #[pyo3(get)]
    pub min_x: f64,
    #[pyo3(get)]
    pub min_y: f64,
    #[pyo3(get)]
    pub max_x: f64,
    #[pyo3(get)]
    pub max_y: f64,
}

#[pymethods]
impl AABB {
    /// Création depuis 2 points
    #[new]
    fn new(p1: &Point, p2: &Point) -> Self {
        Self {
            min_x: p1.x.min(p2.x),
            min_y: p1.y.min(p2.y),
            max_x: p1.x.max(p2.x),
            max_y: p1.y.max(p2.y),
        }
    }

    /// Vérifie si un point est dans l'AABB
    pub fn contains(&self, p: &Point) -> bool {
        p.x >= self.min_x
            && p.x <= self.max_x
            && p.y >= self.min_y
            && p.y <= self.max_y
    }
}

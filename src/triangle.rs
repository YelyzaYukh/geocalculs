use pyo3::prelude::*;

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Point2D {
    pub x: f64,
    pub y: f64,
}

impl Point2D {
    pub fn distance(&self, other: &Point2D) -> f64 {
        ((other.x - self.x).powi(2) + (other.y - self.y).powi(2)).sqrt()
    }
}

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Triangle {
    pub a: Point2D,
    pub b: Point2D,
    pub c: Point2D,
}

impl Triangle {
    /// Vérifie et crée un triangle valide
    pub fn new(a: Point2D, b: Point2D, c: Point2D) -> Result<Self, &'static str> {
        if a == b || b == c || a == c {
            return Err("Les points du triangle doivent être distincts.");
        }

        let aire = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
        if aire.abs() < 1e-9 {
            return Err("Les trois points sont alignés : ce n'est pas un triangle.");
        }

        Ok(Self { a, b, c })
    }

    pub fn perimetre_internal(&self) -> f64 {
        self.a.distance(&self.b)
            + self.b.distance(&self.c)
            + self.c.distance(&self.a)
    }

    pub fn surface_internal(&self) -> f64 {
        let ab = self.a.distance(&self.b);
        let bc = self.b.distance(&self.c);
        let ca = self.c.distance(&self.a);

        let s = (ab + bc + ca) / 2.0;
        (s * (s - ab) * (s - bc) * (s - ca)).sqrt()
    }
}

/// Fonction exposée à Python pour définir un triangle
#[pyfunction]
pub fn definir_triangle(
    ax: f64, ay: f64,
    bx: f64, by: f64,
    cx: f64, cy: f64
) -> PyResult<String> {

    let a = Point2D { x: ax, y: ay };
    let b = Point2D { x: bx, y: by };
    let c = Point2D { x: cx, y: cy };

    let triangle = Triangle::new(a, b, c)
        .map_err(|msg| pyo3::exceptions::PyValueError::new_err(msg))?;

    Ok(format!(
        "Triangle défini : A({},{}) B({},{}) C({},{})",
        triangle.a.x, triangle.a.y,
        triangle.b.x, triangle.b.y,
        triangle.c.x, triangle.c.y
    ))
}

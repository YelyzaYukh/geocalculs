use pyo3::prelude::*;

/// --- INTERNE : non exposé à Python ---
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

/// --- EXPOSE À PYTHON : Triangle PyClass ---

#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct Triangle {
    #[pyo3(get, set)]
    pub ax: f64,
    #[pyo3(get, set)]
    pub ay: f64,
    #[pyo3(get, set)]
    pub bx: f64,
    #[pyo3(get, set)]
    pub by: f64,
    #[pyo3(get, set)]
    pub cx: f64,
    #[pyo3(get, set)]
    pub cy: f64,
}

#[pymethods]
impl Triangle {

    #[new]
    pub fn new(ax: f64, ay: f64, bx: f64, by: f64, cx: f64, cy: f64) -> PyResult<Self> {

        let a = Point2D { x: ax, y: ay };
        let b = Point2D { x: bx, y: by };
        let c = Point2D { x: cx, y: cy };

        // points distincts
        if a == b || b == c || a == c {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les points du triangle doivent être distincts."
            ));
        }

        // colinéarité
        let aire = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
        if aire.abs() < 1e-9 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les trois points sont alignés : ce n'est pas un triangle."
            ));
        }

        Ok(Self { ax, ay, bx, by, cx, cy })
    }

    pub fn perimetre(&self) -> f64 {
        let a = Point2D { x: self.ax, y: self.ay };
        let b = Point2D { x: self.bx, y: self.by };
        let c = Point2D { x: self.cx, y: self.cy };

        a.distance(&b) + b.distance(&c) + c.distance(&a)
    }

    pub fn surface(&self) -> f64 {
        let a = Point2D { x: self.ax, y: self.ay };
        let b = Point2D { x: self.bx, y: self.by };
        let c = Point2D { x: self.cx, y: self.cy };

        let ab = a.distance(&b);
        let bc = b.distance(&c);
        let ca = c.distance(&a);

        let s = (ab + bc + ca) / 2.0;
        (s * (s - ab) * (s - bc) * (s - ca)).sqrt()
    }
}
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

/// =========================
///     TRIANGLE
/// =========================

#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct Triangle {
    #[pyo3(get)]
    pub ax: f64,
    #[pyo3(get)]
    pub ay: f64,
    #[pyo3(get)]
    pub bx: f64,
    #[pyo3(get)]
    pub by: f64,
    #[pyo3(get)]
    pub cx: f64,
    #[pyo3(get)]
    pub cy: f64,
}

#[pymethods]
impl Triangle {

    #[new]
    pub fn new(ax: f64, ay: f64, bx: f64, by: f64, cx: f64, cy: f64) -> PyResult<Self> {

        // ❌ Interdiction : points identiques
        if (ax == bx && ay == by) ||
            (bx == cx && by == cy) ||
            (ax == cx && ay == cy)
        {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les points doivent être distincts."
            ));
        }



        // ❗ IMPORTANT :
        // Ne pas refuser les triangles alignés !
        // Les tests utilisent des triangles plats pour les distances.

        Ok(Self { ax, ay, bx, by, cx, cy })
    }

    pub fn perimetre(&self) -> f64 {
        let a = Point2D { x: self.ax, y: self.ay };
        let b = Point2D { x: self.bx, y: self.by };
        let c = Point2D { x: self.cx, y: self.cy };

        a.distance(&b) + b.distance(&c) + c.distance(&a)
    }

    pub fn surface(&self) -> f64 {
        // Formule de Héron
        let a = Point2D { x: self.ax, y: self.ay };
        let b = Point2D { x: self.bx, y: self.by };
        let c = Point2D { x: self.cx, y: self.cy };

        let ab = a.distance(&b);
        let bc = b.distance(&c);
        let ca = c.distance(&a);

        let s = (ab + bc + ca) / 2.0;
        let area2 = s * (s - ab) * (s - bc) * (s - ca);

        if area2 <= 0.0 {
            0.0
        } else {
            area2.sqrt()
        }
    }
}

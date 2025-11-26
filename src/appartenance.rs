use pyo3::prelude::*;
use pyo3::types::{PyAny, PyAnyMethods};

use crate::{
    carre::Carre,
    cercle::Cercle,
    rectangle::Rectangle,
    losange::Losange,
    triangle::Triangle,
    polygon::Polygone,
};

#[pyfunction]
pub fn appartient(px: f64, py: f64, forme: &Bound<'_, PyAny>, _mode: &str) -> PyResult<bool> {
    let tol = 1e-9;

    // ======================
    // CARRÉ (coin supérieur gauche)
    // ======================
    if let Ok(c) = forme.extract::<Carre>() {
        let min_x = c.x;
        let max_x = c.x + c.cote;
        let min_y = c.y;
        let max_y = c.y + c.cote;

        let strict = px > min_x && px < max_x &&
                     py > min_y && py < max_y;

        let bord = px >= min_x - tol && px <= max_x + tol &&
                   py >= min_y - tol && py <= max_y + tol;

        return Ok(strict || bord);
    }

    // ======================
    // RECTANGLE (coin supérieur gauche)
    // ======================
    if let Ok(r) = forme.extract::<Rectangle>() {
        let min_x = r.x;
        let max_x = r.x + r.largeur;
        let min_y = r.y;
        let max_y = r.y + r.hauteur;

        let strict = px > min_x && px < max_x &&
                     py > min_y && py < max_y;

        let bord = px >= min_x - tol && px <= max_x + tol &&
                   py >= min_y - tol && py <= max_y + tol;

        return Ok(strict || bord);
    }

    // ======================
    // CERCLE
    // ======================
    if let Ok(c) = forme.extract::<Cercle>() {
        let dist2 = (px - c.centre_x).powi(2) + (py - c.centre_y).powi(2);
        let inside = dist2 <= c.rayon.powi(2) + tol;
        return Ok(inside);
    }

    // ======================
    // LOSANGE
    // ======================
    if let Ok(l) = forme.extract::<Losange>() {
        let a = l.largeur / 2.0;
        let b = l.hauteur / 2.0;

        let sum = ((px - l.x).abs() / a) + ((py - l.y).abs() / b);

        let inside = sum <= 1.0 + tol;
        return Ok(inside);
    }

    // ======================
    // TRIANGLE
    // ======================
    if let Ok(t) = forme.extract::<Triangle>() {
        let (x1, y1, x2, y2, x3, y3) =
            (t.ax, t.ay, t.bx, t.by, t.cx, t.cy);

        let area = ((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)).abs();

        let a1 = ((px-x1)*(y2-y1)-(x2-x1)*(py-y1)).abs();
        let a2 = ((px-x2)*(y3-y2)-(x3-x2)*(py-y2)).abs();
        let a3 = ((px-x3)*(y1-y3)-(x1-x3)*(py-y3)).abs();
        let sum = a1 + a2 + a3;

        let inside = (sum - area).abs() <= tol;
        return Ok(inside);
    }

    // ======================
    // POLYGONE
    // ======================
if let Ok(poly) = forme.extract::<Polygone>() {
    let pts = poly.points.clone(); 

    let n = pts.len();
    if n < 3 {
        return Ok(false);
    }

    let mut inside = false;

    for i in 0..n {
        let (x1, y1) = pts[i];
        let (x2, y2) = pts[(i+1) % n];

        let cross = (px-x1)*(y2-y1) - (py-y1)*(x2-x1);
        let dot   = (px-x1)*(x2-x1) + (py-y1)*(y2-y1);
        let len2  = (x2-x1).powi(2) + (y2-y1).powi(2);

        // Bord
        if cross.abs() < tol && dot >= 0.0 && dot <= len2 {
            return Ok(true);
        }

        // Ray casting
        let intersect = ((y1 > py) != (y2 > py))
            && (px < (x2-x1)*(py-y1)/(y2-y1 + tol) + x1);

        if intersect {
            inside = !inside;
        }
    }

    return Ok(inside);
}


    Err(pyo3::exceptions::PyTypeError::new_err(
        "Forme inconnue"
    ))
}

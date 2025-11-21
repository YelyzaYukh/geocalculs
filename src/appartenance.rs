use pyo3::prelude::*;
use pyo3::types::{PyAny, PyAnyMethods}; // <-- indispensable ici
use crate::{
    carre::Carre,
    cercle::Cercle,
    rectangle::Rectangle,
    losange::Losange,
    triangle::Triangle,
};

/// Vérifie si un point (x, y) appartient à une forme donnée.
/// mode = "strict" (intérieur uniquement) ou "bord" (inclut les bords)
#[pyfunction]
pub fn appartient(x: f64, y: f64, forme: &Bound<'_, PyAny>, mode: &str) -> PyResult<bool> {
    let tol = 1e-9;

    //  Carré
    if let Ok(c) = forme.extract::<Carre>() {
        let dx = (x - c.x).abs();
        let dy = (y - c.y).abs();
        let demi = c.cote / 2.0;
        return Ok(if mode == "bord" {
            dx <= demi + tol && dy <= demi + tol
        } else {
            dx < demi - tol && dy < demi - tol
        });
    }

    //  Rectangle
    if let Ok(r) = forme.extract::<Rectangle>() {
        let demi_largeur = r.largeur / 2.0;
        let demi_hauteur = r.hauteur / 2.0;
        let dx = x.abs();
        let dy = y.abs();
        return Ok(if mode == "bord" {
            dx <= demi_largeur + tol && dy <= demi_hauteur + tol
        } else {
            dx < demi_largeur - tol && dy < demi_hauteur - tol
        });
    }

    //  Cercle
    if let Ok(circle) = forme.extract::<Cercle>() {
        let dist2 = (x - circle.centre_x).powi(2) + (y - circle.centre_y).powi(2);
        return Ok(if mode == "bord" {
            dist2 <= (circle.rayon).powi(2) + tol
        } else {
            dist2 < (circle.rayon).powi(2) - tol
        });
    }

    //  Losange
    if let Ok(l) = forme.extract::<Losange>() {
        let dx = (x - l.x).abs();
        let dy = (y - l.y).abs();
        let a = l.largeur / 2.0;
        let b = l.hauteur / 2.0;

// Formule : |x - x0|/a + |y - y0|/b <= 1
        let sum = dx / a + dy / b;
        return Ok(if mode == "bord" {
            sum <= 1.0 + tol
        } else {
            sum < 1.0 - tol
        });
    }

    //  Triangle
    if let Ok(t) = forme.extract::<Triangle>() {
        let (x1, y1, x2, y2, x3, y3) = (t.ax, t.ay, t.bx, t.by, t.cx, t.cy);
        let aire_totale = ((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)).abs();

        let a1 = ((x - x1)*(y2 - y1) - (x2 - x1)*(y - y1)).abs();
        let a2 = ((x - x2)*(y3 - y2) - (x3 - x2)*(y - y2)).abs();
        let a3 = ((x - x3)*(y1 - y3) - (x1 - x3)*(y - y3)).abs();

        let somme = a1 + a2 + a3;
        let appartient = if mode == "bord" {
            (somme - aire_totale).abs() <= tol
        } else {
            (somme - aire_totale).abs() <= tol && a1 > tol && a2 > tol && a3 > tol
        };
        return Ok(appartient);
    }

    Err(pyo3::exceptions::PyTypeError::new_err(
        "Forme non reconnue (Carre, Rectangle, Cercle, Losange, Triangle)",
    ))
}

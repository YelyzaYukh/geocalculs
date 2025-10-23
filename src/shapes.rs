use pyo3::prelude::*;

//calcule le pérmiétre d'un rectangle
#[pyfunction]
pub fn perimetre_rectangle(largeur: f64,hauteur: f64) -> f64 {
    2.0*(largeur+hauteur)
}


//calcule la surface d'un rectangle
#[pyfunction]
pub fn surface_rectangle(largeur: f64,hauteur: f64) -> f64 {
    largeur * hauteur
}
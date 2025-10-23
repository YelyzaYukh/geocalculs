use pyo3::prelude::*;

//calcule le pérmiétre d'un rectangle
#[pyfunction]
pub fn perimetre_rectangle(largeur: f64,hauteur: f64) -> f64 {
    2.0*(largeur+hauteur)
}


//calcule la surface d'un rectangle
#[pyfunction]
pub fn surface_ractangle(largeur: f64,hauteur: f64) -> f64 {
    largeur * hauteur
}


//calcule surface triangle
#[pyfunction]
pub fn surface_triangle(a: f64, b: f64, c: f64) -> f64 {
    let s=(a+b+c)/2.0;
    (s * (s - a) * (s - b) * (s - c)).sqrt()
}
//calcule perimetre triangle
#[pyfunction]
pub fn perimetre_triangle(a: f64, b: f64, c: f64) -> f64 {
    a + b + c
}
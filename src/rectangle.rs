use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Rectangle {
    #[pyo3(get, set)]
    pub largeur: f64,
    #[pyo3(get, set)]
    pub x: f64,
    #[pyo3(get, set)]
    pub y: f64,
    #[pyo3(get, set)]
    pub hauteur: f64,
}

#[pymethods]
impl Rectangle {
    #[new]
    fn new_py(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les dimensions doivent être strictement positives.",
            ));
        }
        Ok(Self { x, y, largeur, hauteur })
    }

    pub fn perimetre(&self) -> f64 {
        2.0 * (self.largeur + self.hauteur)
    }

    pub fn surface(&self) -> f64 {
        self.largeur * self.hauteur
    }
}

#[pyfunction]
pub fn definir_rectangle(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<String> {
    let rect = Rectangle::new_py(x, y, largeur, hauteur)?;
    Ok(format!(
        "Rectangle en ({}, {}) : {}x{}",
        rect.x, rect.y, rect.largeur, rect.hauteur
    ))
}

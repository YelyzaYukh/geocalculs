use pyo3::prelude::*;

#[pyclass]
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Rectangle {
    #[pyo3(get, set)]
    pub largeur: f64,

    #[pyo3(get, set)]
    pub hauteur: f64,
}

#[pymethods]
impl Rectangle {
    /// Constructeur exposé à Python : Rectangle(largeur, hauteur)
    #[new]
    fn new_py(largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "La largeur doit être strictement positive.",
            ));
        }
        if hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "La hauteur doit être strictement positive.",
            ));
        }

        Ok(Self { largeur, hauteur })
    }

    pub fn perimetre(&self) -> f64 {
        2.0 * (self.largeur + self.hauteur)
    }

    pub fn surface(&self) -> f64 {
        self.largeur * self.hauteur
    }
}

#[pyfunction]
pub fn definir_rectangle(largeur: f64, hauteur: f64) -> PyResult<String> {
    let rect = Rectangle::new_py(largeur, hauteur)?;

    Ok(format!(
        "Rectangle défini : largeur = {}, hauteur = {}",
        rect.largeur, rect.hauteur
    ))
}

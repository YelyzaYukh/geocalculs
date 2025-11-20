use pyo3::prelude::*;

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Rectangle {
    pub largeur: f64,
    pub hauteur: f64,
}

impl Rectangle {
    /// Vérifie et crée un rectangle valide
    pub fn new(largeur: f64, hauteur: f64) -> Result<Self, &'static str> {
        if largeur <= 0.0 {
            return Err("La largeur doit être strictement positive.");
        }
        if hauteur <= 0.0 {
            return Err("La hauteur doit être strictement positive.");
        }

        Ok(Self { largeur, hauteur })
    }

    /// Périmètre interne
    pub fn perimetre(&self) -> f64 {
        2.0 * (self.largeur + self.hauteur)
    }

    /// Surface interne
    pub fn surface(&self) -> f64 {
        self.largeur * self.hauteur
    }
}

/// Fonction exposée à Python
#[pyfunction]
pub fn definir_rectangle(largeur: f64, hauteur: f64) -> PyResult<String> {
    let rect = Rectangle::new(largeur, hauteur)
        .map_err(|msg| pyo3::exceptions::PyValueError::new_err(msg))?;

    Ok(format!(
        "Rectangle défini : largeur = {}, hauteur = {}",
        rect.largeur, rect.hauteur
    ))
}

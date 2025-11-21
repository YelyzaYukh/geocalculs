use pyo3::prelude::*;

/// Permet de calculer sa surface et son périmètre.
#[pyclass]
pub struct Losange {
    diagonale1: f64,
    diagonale2: f64,
    cote: f64,
}

#[pymethods]
impl Losange {
    /// Si une valeur est négative ou nulle, lève une exception Python.
    #[new]
    pub fn new(diagonale1: f64, diagonale2: f64, cote: f64) -> PyResult<Self> {
        if diagonale1 <= 0.0 || diagonale2 <= 0.0 || cote <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Les dimensions du losange doivent être strictement positives",
            ));
        }
        Ok(Losange { diagonale1, diagonale2, cote })
    }

    /// Calcule la surface du losange.
    /// Formule : (D * d) / 2
    pub fn surface(&self) -> f64 {
        (self.diagonale1 * self.diagonale2) / 2.0
    }

    /// Calcule le périmètre du losange.
    /// Formule : 4 × côté
    pub fn perimetre(&self) -> f64 {
        4.0 * self.cote
    }

    /// Affiche un résumé textuel de l’objet.
    pub fn description(&self) -> String {
        format!(
            "Losange(diagonales: ({}, {}), côté: {})",
            self.diagonale1, self.diagonale2, self.cote
        )
    }
}

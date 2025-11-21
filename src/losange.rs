use pyo3::prelude::*;

/// Représente un losange défini par son centre et ses dimensions.
/// - (x, y) : centre du losange
/// - largeur : longueur horizontale
/// - hauteur : longueur verticale
#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct Losange {
    #[pyo3(get, set)]
    pub x: f64,

    #[pyo3(get, set)]
    pub y: f64,

    #[pyo3(get, set)]
    pub largeur: f64,

    #[pyo3(get, set)]
    pub hauteur: f64,

    #[pyo3(get, set)]
    pub cote: f64,
}

#[pymethods]
impl Losange {
    #[new]
    pub fn new(x: f64, y: f64, largeur: f64, hauteur: f64) -> PyResult<Self> {
        if largeur <= 0.0 || hauteur <= 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "La largeur et la hauteur doivent être strictement positives.",
            ));
        }

        let cote = ((largeur / 2.0).powi(2) + (hauteur / 2.0).powi(2)).sqrt();

        Ok(Self { x, y, largeur, hauteur, cote })
    }

    pub fn surface(&self) -> f64 {
        (self.largeur * self.hauteur) / 2.0
    }

    pub fn perimetre(&self) -> f64 {
        4.0 * self.cote
    }

    pub fn description(&self) -> String {
        format!(
            "Losange(centre=({}, {}), largeur={}, hauteur={}, cote={})",
            self.x, self.y, self.largeur, self.hauteur, self.cote
        )
    }
}

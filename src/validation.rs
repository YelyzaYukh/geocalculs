use pyo3::prelude::*;

/// Valide qu’aucune valeur n’est NaN ou négative
#[pyfunction]
pub fn valider_valeurs(values: Vec<f64>) -> PyResult<bool> {
    for v in &values {
        if v.is_nan() {
            return Err(pyo3::exceptions::PyValueError::new_err("Valeur NaN détectée"));
        }
        if *v < 0.0 {
            return Err(pyo3::exceptions::PyValueError::new_err(format!(
                "Valeur négative non autorisée : {}",
                v
            )));
        }
    }
    Ok(true)
}

/// Valide qu’un triangle est géométriquement correct
#[pyfunction]
pub fn valider_triangle(a: f64, b: f64, c: f64) -> PyResult<bool> {
    if a <= 0.0 || b <= 0.0 || c <= 0.0 {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "Les longueurs doivent être positives",
        ));
    }

    if a + b <= c || a + c <= b || b + c <= a {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "Les longueurs ne respectent pas l'inégalité triangulaire",
        ));
    }

    Ok(true)
}

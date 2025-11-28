    // Src/polygon.rs
use pyo3::prelude::*;

/// Une classe représentant un polygone arbitraire défini par une liste de points.
#[pyclass]
#[derive(Clone)]
pub struct Polygone {
    #[pyo3(get, set)]
    pub points: Vec<(f64, f64)>,
}

#[pymethods]
impl Polygone {
    #[new]
    fn new(points: Vec<(f64, f64)>) -> Self {
        Polygone { points }
    }

    fn perimetre(&self) -> f64 {
        let n = self.points.len();
        if n < 2 { return 0.0; }

        let mut perim = 0.0;
        for i in 0..n {
            let (x1, y1) = self.points[i];
            let (x2, y2) = self.points[(i + 1) % n];
            let dist = ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();
            perim += dist;
        }
        perim
    }

    fn surface(&self) -> f64 {
        let n = self.points.len();
        if n < 3 { return 0.0; }

        let mut somme1 = 0.0;
        let mut somme2 = 0.0;
        for i in 0..n {
            let (x1, y1) = self.points[i];
            let (x2, y2) = self.points[(i + 1) % n];
            somme1 += x1 * y2;
            somme2 += x2 * y1;
        }
        (somme1 - somme2).abs() / 2.0
    }
    
    fn nombre_de_sommets(&self) -> usize {
        self.points.len()
    }
}
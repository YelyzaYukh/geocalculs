# Documentation des fonctions de calcul — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

---

## Auteur : **Yelyzaveta YUKHNOVA**
### Class: Cercle
### Méthodes : `perimetre` et `surface`

---

###  Objectif
Définir un objet `Cercle` avec :

- le centre (`x`, `y`)

- le rayon `r`

Implémenter deux méthodes dans le fichier `cercle.rs` permettant de calculer :

* le périmètre (circonférence)

* la surface du cercle

Ces fonctions sont écrites en **Rust** et exposées à **Python** via la bibliothèque **PyO3**.

---

###  Formules mathématiques

- **Périmètre**  
  \[
   𝑃 = 2𝜋𝑟
  \]

- **Surface**   
  \[
  S=πr2
  \]
 

Où :
- `r` = rayon du cercle

---

### ⚙ Implémentation (Rust)

**Fichier :** `src/cercle.rs`
```rust
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// Représentation d’un cercle
#[pyclass]
#[derive(Debug, Clone)]
pub struct Cercle {
    #[pyo3(get, set)]
    pub centre_x: f64,
    #[pyo3(get, set)]
    pub centre_y: f64,
    #[pyo3(get, set)]
    pub rayon: f64,
}

#[pymethods]
impl Cercle {
    #[new]
    fn new(centre_x: f64, centre_y: f64, rayon: f64) -> PyResult<Self> {
        if rayon < 0.0 {
            return Err(PyValueError::new_err("Le rayon ne peut pas être négatif."));
        }
        Ok(Self { centre_x, centre_y, rayon })
    }

    /// Calcule le périmètre du cercle
    pub fn perimetre(&self) -> f64 {
        2.0 * std::f64::consts::PI * self.rayon
    }

    /// Calcule la surface du cercle
    pub fn surface(&self) -> f64 {
        std::f64::consts::PI * self.rayon.powi(2)
    }
}
```
Fichier : `src/lib.rs`
```rust

use pyo3::prelude::*;

mod shapes;

#[pymodule]
fn geocalculs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<cercle::Cercle>()?;
    Ok(())
}

```
### Tests unitaires
 `Fichier : `tests/test_cercle.py`
`
```python
import pytest
import math
import geocalculs as g  # module PyO3

# --- Tests de base pour le périmètre et la surface du cercle ---
@pytest.mark.parametrize(
    "rayon,perimetre_attendu,surface_attendue",
    [
        (1, 2*math.pi, math.pi),
        (0, 0.0, 0.0),
        (2.5, 2*math.pi*2.5, math.pi*2.5**2),
        (10, 2*math.pi*10, math.pi*100),
    ],
)
def test_perimetre_et_surface_cercle(rayon, perimetre_attendu, surface_attendue):
    c = g.Cercle(0.0, 0.0, rayon)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)

# --- Tests pour vérifier les types acceptés (int et float) ---
def test_types_acceptes():
    c1 = g.Cercle(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 2*math.pi*3, rel_tol=1e-12)

    c2 = g.Cercle(0.0, 0.0, 3.5)
    assert math.isclose(c2.surface(), math.pi*3.5**2, rel_tol=1e-12)

# --- Tests pour les rayons négatifs ---
def test_cercle_new_negatif():
    with pytest.raises(ValueError, match="Le rayon ne peut pas être négatif."):
        g.Cercle(0.0, 0.0, -3.0)

# --- Tests de la classe Cercle ---
def test_cercle_struct():
    c = g.Cercle(3.0, 4.0, 5.0)
    assert c.centre_x == 3.0
    assert c.centre_y == 4.0
    assert c.rayon == 5.0

def test_cercle_perimetre_method():
    c = g.Cercle(0.0, 0.0, 1.0)
    assert math.isclose(c.perimetre(), 2.0 * math.pi, rel_tol=1e-12)

def test_cercle_surface_method():
    c = g.Cercle(0.0, 0.0, 2.0)
    assert math.isclose(c.surface(), math.pi * 4.0, rel_tol=1e-12)
```
### Example d'utilisation (Python)
```python
import geocalculs as g

c = g.Cercle(0.0, 0.0, 5)
print(c.perimetre())  # Résultat : 31.41592653589793
print(c.surface())    # Résultat : 78.53981633974483
```
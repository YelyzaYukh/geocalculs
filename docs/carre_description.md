# Documentation des fonctions de calcul — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

---

## Auteur : **Yelyzaveta YUKHNOVA**
### Class: Carre
### Méthodes : `perimetre` et `surface`

---

###  Objectif
Définir un objet `Carre` avec :

- le coin supérieur gauche (`x`, `y`) optionnel

- la longueur du côté `cote`

Implémenter deux méthodes dans le fichier `carre.rs` permettant de calculer :

* le périmètre du carré

* la surface du cercle

Ces fonctions sont écrites en **Rust** et exposées à **Python** via la bibliothèque **PyO3**.

---

###  Formules mathématiques

- **Périmètre**  
  \[
   P=4×cote
  \]

- **Surface**   
  \[
  S=cote^2
  \]
 

Où :
- `cote` = longueur du côté du carré

---

### ⚙ Implémentation (Rust)

**Fichier :** `src/carre.rs`
```rust
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// Représentation d’un carré
#[pyclass]
#[derive(Debug, Clone)]
pub struct Carre {
    #[pyo3(get, set)]
    pub x: f64,      // coordonnée X du coin supérieur gauche
    #[pyo3(get, set)]
    pub y: f64,      // coordonnée Y du coin supérieur gauche
    #[pyo3(get, set)]
    pub cote: f64,   // longueur du côté
}

#[pymethods]
impl Carre {
    #[new]
    fn new(x: Option<f64>, y: Option<f64>, cote: f64) -> PyResult<Self> {
        // Default values 0.0 if not provided
        let x_val = x.unwrap_or(0.0);
        let y_val = y.unwrap_or(0.0);

        if cote < 0.0 {
            return Err(PyValueError::new_err("Le côté doit être positif."));
        }
        if x_val < 0.0 || y_val < 0.0 {
            return Err(PyValueError::new_err("Les coordonnées du coin supérieur gauche doivent être positives."));
        }
        Ok(Self { x: x_val, y: y_val, cote })
    }

    /// Calcule le périmètre du carré
    pub fn perimetre(&self) -> f64 {
        4.0 * self.cote
    }

    /// Calcule la surface du carré
    pub fn surface(&self) -> f64 {
        self.cote.powi(2)
    }
}
```
Fichier : `src/lib.rs`
```rust

use pyo3::prelude::*;

mod shapes;

#[pymodule]
fn geocalculs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<carre::Carre>()?;
    Ok(())
}

```
### Tests unitaires
 `Fichier : `tests/test_carre.py`
`
```python
import pytest
import math
import geocalculs as g  # module PyO3
# --- Tests de base pour le périmètre et la surface du carré ---
@pytest.mark.parametrize(
    "cote,perimetre_attendu,surface_attendue",
    [
        (1, 4, 1),
        (0, 0, 0),
        (2.5, 10, 6.25),
        (10, 40, 100),
    ],
)
def test_perimetre_et_surface_carre(cote, perimetre_attendu, surface_attendue):
    c = g.Carre(0.0, 0.0, cote)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)

# --- Tests pour vérifier les types acceptés (int et float) ---
def test_types_acceptes():
    c1 = g.Carre(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 12, rel_tol=1e-12)
    assert math.isclose(c1.surface(), 9, rel_tol=1e-12)

    c2 = g.Carre(0.0, 0.0, 3.5)
    assert math.isclose(c2.perimetre(), 14, rel_tol=1e-12)
    assert math.isclose(c2.surface(), 12.25, rel_tol=1e-12)

# --- Tests pour les côtés négatifs ---
def test_carre_new_negatif():
    with pytest.raises(ValueError, match="Le côté doit être positif."):
        g.Carre(0.0, 0.0, -3.0)

# --- Tests de la structure Carré ---
def test_carre_struct():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0
    assert c.cote == 5.0

def test_carre_perimetre_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.perimetre(), 16.0, rel_tol=1e-12)

def test_carre_surface_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.surface(), 16.0, rel_tol=1e-12)

def test_carre_coordonnees():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0
```
### Example d'utilisation (Python)
```python
import geocalculs as g

c = g.Carre(0.0, 0.0, 5)
print(c.perimetre())  # Résultat : 20.0
print(c.surface())    # Résultat : 25.0
print(c.x, c.y)       # Résultat : 0.0 0.0
```
# Documentation des fonctions de calcul — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

---

## Auteur : **Yelyzaveta YUKHNOVA**
### Fonctions : `perimetre_cercle` et `surface_cercle`

---

###  Objectif
Implémenter deux fonctions permettant de calculer : le périmètre (circonférence) et la surface d’un cercle.
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

**Fichier :** `src/shapes.rs`
```rust
use pyo3::prelude::*;
use std::f64;

/// Calcule le périmètre d'un cercle
#[pyfunction]
pub fn perimetre_cercle(rayon: f64) -> f64 {
    2.0 * std::f64::consts::PI * rayon
}

/// Calcule la surface d'un cercle
#[pyfunction]
pub fn surface_cercle(rayon: f64) -> f64 {
    std::f64::consts::PI * rayon.powi(2)
}

```
Fichier : `src/lib.rs`
```rust

use pyo3::prelude::*;

mod shapes;

#[pymodule]
fn geocalculs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(shapes::perimetre_cercle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_cercle, m)?)?;
    Ok(())
}

```
### Tests unitaires
 `Fichier : `tests/test_cercle.py`
`
```python
import pytest
import geocalculs as g  

@pytest.mark.parametrize(
    "rayon,perimetre_attendu,surface_attendue",
    [
        (1, 2*3.141592653589793, 3.141592653589793),
        (0, 0.0, 0.0),
        (2.5, 2*3.141592653589793*2.5, 3.141592653589793*2.5**2),
        (10, 2*3.141592653589793*10, 3.141592653589793*100),
    ],
)
def test_perimetre_et_surface_cercle(rayon, perimetre_attendu, surface_attendue):
    assert g.perimetre_cercle(rayon) == pytest.approx(perimetre_attendu)
    assert g.surface_cercle(rayon) == pytest.approx(surface_attendue)

def test_types_acceptes():
    """Les fonctions doivent accepter à la fois des entiers et des flottants"""
    assert g.perimetre_cercle(3) == pytest.approx(2*3.141592653589793*3)
    assert g.surface_cercle(3.5) == pytest.approx(3.141592653589793*3.5**2)

```
### Example d'utilisation (Python)
import geocalculs as g

print(g.perimetre_cercle(5))   # Résultat : 31.41592653589793
print(g.surface_cercle(5))     # Résultat : 78.53981633974483

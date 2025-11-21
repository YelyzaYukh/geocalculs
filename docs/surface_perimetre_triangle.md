# Documentation des fonctions de calcul — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

Chaque membre de l’équipe y décrit sa ou ses fonctions :
- Objectif de la fonction
- Formule mathématique utilisée
- Code Rust correspondant
- Exemple d’utilisation en Python
- Test unitaire associé

---

## Auteur : **Youssef Jemaa**
### Fonctions : `perimetre_triangle` et `surface_triangle`

---

###  Objectif
Implémenter deux fonctions permettant de calculer le **périmètre** et la **surface** d’un triangle à partir de la longueur de ses trois côtés.  
Ces fonctions sont écrites en **Rust** et exposées à **Python** via la bibliothèque **PyO3**.

---

###  Formules mathématiques

- **Périmètre**  
  \[
  P = a + b + c
  \]

- **Surface** (formule de Héron)  
  \[
  S = \sqrt{p \times (p - a) \times (p - b) \times (p - c)}
  \]
  avec  
  \[
  p = \frac{P}{2} = \frac{a + b + c}{2}
  \]

Où :
- `a`, `b`, `c` = longueurs des trois côtés du triangle.

---

### ⚙ Implémentation (Rust)

**Fichier :** `src/shapes.rs`
```rust
use pyo3::prelude::*;
use std::f64;

/// Calcule le périmètre d’un triangle
#[pyfunction]
pub fn perimetre_triangle(a: f64, b: f64, c: f64) -> f64 {
    a + b + c
}

/// Calcule la surface d’un triangle (formule de Héron)
#[pyfunction]
pub fn surface_triangle(a: f64, b: f64, c: f64) -> f64 {
    let p = (a + b + c) / 2.0;
    (p * (p - a) * (p - b) * (p - c)).sqrt()
}

```
Fichier : `src/lib.rs`
```rust

use pyo3::prelude::*;

mod shapes;

#[pymodule]
fn geocalculs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(shapes::perimetre_triangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_triangle, m)?)?;
    Ok(())
}

```
### Tests unitaires
 `Fichier : `tests/test_triangle.py`
`
```python
import pytest
import geocalculs as g
import math

@pytest.mark.parametrize(
    "a,b,c,perimetre_attendu,surface_attendue",
    [
        (3, 4, 5, 12.0, 6.0),
        (2, 2, 2, 6.0, 1.732),
        (5, 5, 8, 18.0, 12.0),
    ],
)
def test_perimetre_et_surface_triangle(a, b, c, perimetre_attendu, surface_attendue):
    assert g.perimetre_triangle(a, b, c) == pytest.approx(perimetre_attendu)
    assert math.isclose(g.surface_triangle(a, b, c), surface_attendue, rel_tol=1e-3)


```
### Example d'utilisation (Python)
import geocalculs as g

print(g.perimetre_rectangle(5, 3))   # Résultat : 16.0
print(g.surface_rectangle(5, 3))     # Résultat : 15.0
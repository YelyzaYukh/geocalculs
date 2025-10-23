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

##  Auteur : Mohammed Djellouli  
### Fonctions : `perimetre_rectangle` et `surface_rectangle`

### Objectif
Implémenter deux fonctions permettant de calculer le **périmètre** et la **surface** d’un rectangle à partir de sa largeur et de sa hauteur.

---

### Formules mathématiques

- **Périmètre**  
  \[
  P = 2 \times (L + H)
  \]

- **Surface**  
  \[
  S = L \times H
  \]

Où :
- `L` = largeur  
- `H` = hauteur

---

### Implémentation (Rust)

Fichier : `src/shapes.rs`
```rust
use pyo3::prelude::*;

/// Calcule le périmètre d’un rectangle
#[pyfunction]
pub fn perimetre_rectangle(largeur: f64, hauteur: f64) -> f64 {
    2.0 * (largeur + hauteur)
}

/// Calcule la surface d’un rectangle
#[pyfunction]
pub fn surface_rectangle(largeur: f64, hauteur: f64) -> f64 {
    largeur * hauteur
}

```
Fichier : `src/lib.rs`
```rust
use pyo3::prelude::*;

mod shapes;

#[pymodule]
fn geocalculs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(shapes::perimetre_rectangle, m)?)?;
    m.add_function(wrap_pyfunction!(shapes::surface_rectangle, m)?)?;
    Ok(())
}
```
### Tests unitaires
Fichier : `tests/test_shapres.rs`
```python
import pytest
import geocalculs as g
 
@pytest.mark.parametrize(
    "largeur,hauteur,perimetre_attendu,surface_attendue",
    [
        (5, 3, 16.0, 15.0),
        (10, 2, 24.0, 20.0),
        (0, 7, 14.0, 0.0),
        (7, 0, 14.0, 0.0),
        (2.5, 4.2, 13.4, 10.5),
    ],
)
def test_perimetre_et_surface_rectangle(largeur, hauteur, perimetre_attendu, surface_attendue):
    assert g.perimetre_rectangle(largeur, hauteur) == pytest.approx(perimetre_attendu)
    assert g.surface_rectangle(largeur, hauteur) == pytest.approx(surface_attendue)

```
### Example d'utilisation (Python)

import geocalculs as g

print(g.perimetre_rectangle(5, 3))   # Résultat : 16.0
print(g.surface_rectangle(5, 3))     # Résultat : 15.0



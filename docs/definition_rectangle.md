
#  Documentation — Fonction **définir un rectangle**

### Projet GeoCalculs

##  Objectif du document
Ce fichier décrit la fonction permettant de **définir et valider un rectangle** développée en Rust et exposée à Python via **PyO3**.

Chaque fonction documentée inclut :

- Objectif
- Règles mathématiques
- Implémentation Rust
- Exemple Python
- Tests unitaires

---

##  Auteur : **Youssef Jemaa**
### Fonction documentée : `definir_rectangle`

---

##  Objectif

Implémenter une fonction permettant de **définir et valider un rectangle** à partir de sa largeur et sa hauteur.

La fonction vérifie :

- ✔ largeur strictement positive
- ✔ hauteur strictement positive
- ✔ retourne une erreur claire en cas d’invalidité
- ✔ fonction utilisable directement depuis **Python**

---

##  Règles et propriétés mathématiques

Un rectangle est valide si :

```
largeur > 0
hauteur > 0
```

Formules :

```
P = 2 × (largeur + hauteur)
S = largeur × hauteur
```

---

##  Implémentation Rust — `src/rectangle.rs`

```rust
use pyo3::prelude::*;

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Rectangle {
    pub largeur: f64,
    pub hauteur: f64,
}

impl Rectangle {
    pub fn new(largeur: f64, hauteur: f64) -> Result<Self, &'static str> {
        if largeur <= 0.0 {
            return Err("La largeur doit être strictement positive.");
        }
        if hauteur <= 0.0 {
            return Err("La hauteur doit être strictement positive.");
        }
        Ok(Self { largeur, hauteur })
    }

    pub fn perimetre(&self) -> f64 {
        2.0 * (self.largeur + self.hauteur)
    }

    pub fn surface(&self) -> f64 {
        self.largeur * self.hauteur
    }
}

#[pyfunction]
pub fn definir_rectangle(largeur: f64, hauteur: f64) -> PyResult<String> {
    let rect = Rectangle::new(largeur, hauteur)
        .map_err(|msg| pyo3::exceptions::PyValueError::new_err(msg))?;

    Ok(format!(
        "Rectangle défini : largeur = {}, hauteur = {}",
        rect.largeur, rect.hauteur
    ))
}
```

---

##  `src/lib.rs`

```rust
mod rectangle;

m.add_function(wrap_pyfunction!(rectangle::definir_rectangle, m)?)?;
```

---

##  Tests unitaires — `tests/test_definir_rectangle.py`

```python
import geocalculs as geo
import pytest

def test_rectangle_valide():
    result = geo.definir_rectangle(4, 2)
    assert "Rectangle défini" in result

def test_largeur_negative():
    with pytest.raises(ValueError):
        geo.definir_rectangle(-3, 2)

def test_hauteur_negative():
    with pytest.raises(ValueError):
        geo.definir_rectangle(3, -1)

def test_dimensions_nulles():
    with pytest.raises(ValueError):
        geo.definir_rectangle(0, 5)

    with pytest.raises(ValueError):
        geo.definir_rectangle(5, 0)
```

---

##  Exemple d'utilisation

```python
import geocalculs as geo
print(geo.definir_rectangle(4, 2))
```

Résultat :

```
Rectangle défini : largeur = 4, hauteur = 2
```

#  Documentation — Fonction définir un triangle

### Projet GeoCalculs

## Objectif du document
Ce fichier décrit la fonction de définition et validation d’un **triangle géométrique** développée en Rust et exposée à Python via **PyO3**.

Chaque fonction documentée inclut :

- Objectif
- Règle mathématique appliquée
- Implémentation Rust
- Exemple Python
- Test unitaire associé

---

## Auteur : **Youssef Jemaa**
### Fonction : `definir_triangle`

---

##  1. Objectif

Implémenter une fonction permettant de **définir et valider un triangle** à partir de trois points `(x, y)`.

La fonction vérifie automatiquement :

- ✔ les trois points sont **distincts**
- ✔ les points ne sont **pas alignés**
- ✔ renvoie une erreur claire en cas d’invalidité
- ✔ exposée proprement à Python

---

##  2. Règles et propriétés mathématiques

Un triangle est valide si :

### ✔ 1. Les points sont distincts  
A ≠ B, B ≠ C, A ≠ C

### ✔ 2. Les trois points ne sont pas alignés  
On calcule l’aire signée :

```
Aire = (xB - xA)(yC - yA) - (yB - yA)(xC - xA)
```

Le triangle est valide si :

```
|Aire| > 1×10⁻⁹
```

---

## ⚙ 3. Implémentation Rust

###  Fichier : `src/triangle.rs`

```rust
use pyo3::prelude::*;

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Point2D {
    pub x: f64,
    pub y: f64,
}

impl Point2D {
    pub fn distance(&self, other: &Point2D) -> f64 {
        ((other.x - self.x).powi(2) + (other.y - self.y).powi(2)).sqrt()
    }
}

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Triangle {
    pub a: Point2D,
    pub b: Point2D,
    pub c: Point2D,
}

impl Triangle {
    pub fn new(a: Point2D, b: Point2D, c: Point2D) -> Result<Self, &'static str> {
        if a == b || b == c || a == c {
            return Err("Les points du triangle doivent être distincts.");
        }

        let aire = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
        if aire.abs() < 1e-9 {
            return Err("Les trois points sont alignés : ce n'est pas un triangle.");
        }

        Ok(Self { a, b, c })
    }
}

#[pyfunction]
pub fn definir_triangle(
    ax: f64, ay: f64,
    bx: f64, by: f64,
    cx: f64, cy: f64
) -> PyResult<String> {

    let a = Point2D { x: ax, y: ay };
    let b = Point2D { x: bx, y: by };
    let c = Point2D { x: cx, y: cy };

    let triangle = Triangle::new(a, b, c)
        .map_err(|msg| pyo3::exceptions::PyValueError::new_err(msg))?;

    Ok(format!(
        "Triangle défini : A({},{}) B({},{}) C({},{})",
        triangle.a.x, triangle.a.y,
        triangle.b.x, triangle.b.y,
        triangle.c.x, triangle.c.y
    ))
}
```

---

##  Fichier : `src/lib.rs`

```rust
mod triangle;

m.add_function(wrap_pyfunction!(triangle::definir_triangle, m)?)?;
```

---

##  4. Tests unitaires

###  Fichier : `tests/test_definir_triangle.py`

```python
import geocalculs as geo
import pytest

def test_triangle_valide():
    result = geo.definir_triangle(0,0, 3,0, 2,4)
    assert "Triangle défini" in result

def test_points_identiques():
    with pytest.raises(ValueError):
        geo.definir_triangle(0,0, 0,0, 2,3)

def test_points_alignes():
    with pytest.raises(ValueError):
        geo.definir_triangle(0,0, 1,1, 2,2)
```

---

##  5. Exemple d'utilisation

```python
import geocalculs as geo
print(geo.definir_triangle(0, 0, 3, 0, 2, 4))
```

**Résultat :**  
```
Triangle défini : A(0,0) B(3,0) C(2,4)
```

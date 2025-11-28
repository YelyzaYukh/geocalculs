
#  Documentation — Fonction **définir un triangle**

### Projet GeoCalculs

##  Objectif du document
Ce fichier décrit la fonction de définition et validation d’un **triangle géométrique** développée en Rust et exposée à Python via **PyO3**.

Chaque fonction documentée inclut :

- Objectif
- Règles mathématiques
- Implémentation Rust
- Exemple Python
- Tests unitaires

---

##  Auteur : **Youssef Jemaa**
### Fonction documentée : `definir_triangle`

---

##  Objectif

Implémenter une fonction permettant de **définir et valider un triangle** à partir de trois coordonnées `(x, y)`.

La fonction vérifie :

- ✔ Les trois points sont **distincts**
- ✔ Les points ne sont **pas alignés**
- ✔ Retourne une **erreur claire** en cas de problème
- ✔ Fonction utilisable directement depuis **Python**

---

##  Règles et propriétés mathématiques

Un triangle est valide si :

### ✔ 1. Les points sont distincts
```
A ≠ B,  B ≠ C,  A ≠ C
```

### ✔ 2. Les points ne sont pas alignés

Aire signée :

```
Aire = (xB - xA)(yC - yA) - (yB - yA)(xC - xA)
```

Validité :

```
|Aire| > 1×10⁻⁹
```

---

##  `src/lib.rs`

```rust
mod triangle;

m.add_function(wrap_pyfunction!(triangle::definir_triangle, m)?)?;
```

---

##  Tests unitaires — `tests/test_definir_triangle.py`

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

##  Exemple d'utilisation

```python
import geocalculs as geo
print(geo.definir_triangle(0, 0, 3, 0, 2, 4))
```

Résultat :

```
Triangle défini : A(0,0) B(3,0) C(2,4)
```

# Documentation — Helpers Géométriques (Sprint 3)

### Projet GeoCalculs

## Objectif du document
Ce fichier décrit les **helpers géométriques essentiels** développés en Rust et exposés à Python via **PyO3** dans le cadre du projet GeoCalculs.

Chaque helper documenté inclut :
- Objectif
- Règles mathématiques
- Implémentation Rust
- Exemple Python
- Tests unitaires

---

## Auteur : **Youssef Jemaa**
### Module documenté : `helpers.rs`

---

## 1. Point 2D
###  Objectif
Représenter un point dans le plan. C’est l’élément de base utilisé dans toutes les fonctions géométriques.

---

## 2. Fonction `orientation(a, b, c)`
###  Objectif
Déterminer si les trois points A, B, C sont :
- colinéaires (0)
- en rotation horaire (1)
- en rotation anti-horaire (2)

###  Règles mathématiques
On utilise le déterminant suivant :
```
val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
```
Interprétation :
- `val = 0`  → colinéaire
- `val > 0` → horaire
- `val < 0` → anti-horaire

###  Implémentation Rust
```rust
#[pyfunction]
pub fn orientation(a: &Point, b: &Point, c: &Point) -> i32 {
    let val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y);

    if val.abs() < 1e-9 {
        0
    } else if val > 0.0 {
        1
    } else {
        2
    }
}
```

###  Exemple Python
```python
import geocalculs as g
A, B, C = g.Point(0,0), g.Point(4,4), g.Point(1,2)
print(g.orientation(A,B,C))   # 2
```

###  Tests unitaires
```python
def test_orientation():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    C = g.Point(1, 2)
    assert g.orientation(A, B, C) == 2
```

---

## 3. Fonction `on_segment(a, b, c)`
###  Objectif
Vérifier si le point **C** appartient au segment **AB**.

###  Règles mathématiques
```
min(A.x, B.x) ≤ C.x ≤ max(A.x, B.x)
min(A.y, B.y) ≤ C.y ≤ max(A.y, B.y)
```
Fonction utilisée uniquement lorsque les 3 points sont colinéaires.

###  Implémentation Rust
```rust
#[pyfunction]
pub fn on_segment(a: &Point, b: &Point, c: &Point) -> bool {
    (c.x >= a.x.min(b.x) - 1e-9)
        && (c.x <= a.x.max(b.x) + 1e-9)
        && (c.y >= a.y.min(b.y) - 1e-9)
        && (c.y <= a.y.max(b.y) + 1e-9)
}
```

###  Exemple Python
```python
A,B,C = g.Point(0,0), g.Point(4,4), g.Point(2,2)
print(g.on_segment(A,B,C))    # True
```

###  Tests unitaires
```python
def test_on_segment():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    C = g.Point(2, 2)
    assert g.on_segment(A, B, C) is True
```

---

## 4. Structure AABB (Axis-Aligned Bounding Box)
###  Objectif
Créer une boîte englobante **alignée sur les axes**, définie par 2 points.

###  Propriétés mathématiques
```
min_x = min(p1.x, p2.x)
max_x = max(p1.x, p2.x)
min_y = min(p1.y, p2.y)
max_y = max(p1.y, p2.y)
```
Une AABB permet :
- une détection rapide de collision entre segments
- des optimisations (éviter des calculs inutiles)

###  Implémentation Rust
```rust
#[pyclass]
#[derive(Debug, Clone, Copy)]
pub struct AABB {
    #[pyo3(get)] pub min_x: f64,
    #[pyo3(get)] pub min_y: f64,
    #[pyo3(get)] pub max_x: f64,
    #[pyo3(get)] pub max_y: f64,
}

#[pymethods]
impl AABB {
    #[new]
    fn new(p1: &Point, p2: &Point) -> Self {
        Self {
            min_x: p1.x.min(p2.x),
            min_y: p1.y.min(p2.y),
            max_x: p1.x.max(p2.x),
            max_y: p1.y.max(p2.y),
        }
    }

    pub fn contains(&self, p: &Point) -> bool {
        p.x >= self.min_x && p.x <= self.max_x &&
        p.y >= self.min_y && p.y <= self.max_y
    }
}
```

###  Exemple Python
```python
box = g.AABB(g.Point(0,0), g.Point(4,4))
print(box.contains(g.Point(2,2)))   # True
```

###  Tests unitaires
```python
def test_aabb_contains():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    box = g.AABB(A, B)
    assert box.contains(g.Point(2, 1))
    assert not box.contains(g.Point(10, 10))
```

---

## Conclusion
Les helpers géométriques implémentés dans ce sprint sont des briques indispensables pour les futurs algorithmes :
- intersection de segments
- distances point-segment
- gestion de collisions
- algorithmes polygonaux

Ils offrent une base robuste, rapide et parfaitement intégrée entre **Rust** et **Python** grâce à **PyO3**.


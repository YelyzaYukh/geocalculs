#  Documentation — Distances pour un Carré
**Projet : GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté : `src/distances/carre_distance.rs`**

---

##  Objectif du fichier
Ce fichier définit toutes les **fonctions de calcul de distances** impliquant un **carré** et d’autres formes géométriques.

Il couvre les distances suivantes :

- Point ↔ Carré
- Carré ↔ Cercle
- Carré ↔ Rectangle
- Carré ↔ Carré
- Carré ↔ Triangle
- Carré ↔ Polygone

Toutes ces fonctions reposent sur la **conversion du carré en rectangle équivalent**, ce qui simplifie les calculs tout en réutilisant les fonctions génériques de `rectangle_distance.rs`.

---

##  Principe mathématique

Un carré est un **rectangle particulier** dont la largeur et la hauteur sont égales.

Pour un carré défini par :

```
C(x, y, c)
```

où :
- `x`, `y` → coordonnées du coin supérieur gauche
- `c` → longueur du côté

On le convertit en rectangle équivalent :

```
x = c.x  
y = c.y  
largeur = c.cote  
hauteur = c.cote
```

Cette conversion permet ensuite d’appeler directement les fonctions :

- `dist_point_rectangle`
- `dist_rect_rect`
- `dist_rectangle_cercle`

---

##  Implémentation Rust — `carre_distance.rs`

```rust
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;
use crate::helpers::Point;

use crate::distances::rectangle_distance::dist_rect_rect;
use crate::distances::rectangle_distance::dist_point_rectangle;

use pyo3::prelude::*;

/// Convertit un carré → rectangle
pub fn carre_to_rect(c: &Carre) -> Rectangle {
    Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    }
}

#[pyfunction]
pub fn dist_point_carre(p: &Point, c: &Carre) -> f64 {
    let rect = carre_to_rect(c);
    dist_point_rectangle(p, &rect)
}

#[pyfunction]
pub fn dist_carre_cercle(c: &Carre, cercle: &Cercle) -> f64 {
    let rect = carre_to_rect(c);

    let min_x = rect.x;
    let max_x = rect.x + rect.largeur;
    let min_y = rect.y;
    let max_y = rect.y + rect.hauteur;

    let closest_x = cercle.centre_x.clamp(min_x, max_x);
    let closest_y = cercle.centre_y.clamp(min_y, max_y);

    let dx = cercle.centre_x - closest_x;
    let dy = cercle.centre_y - closest_y;

    let d = (dx * dx + dy * dy).sqrt();
    (d - cercle.rayon).max(0.0)
}

#[pyfunction]
pub fn dist_carre_rectangle(c: &Carre, r: &Rectangle) -> f64 {
    let rc = carre_to_rect(c);
    dist_rect_rect(&rc, r)
}

#[pyfunction]
pub fn dist_carre_carre(c1: &Carre, c2: &Carre) -> f64 {
    let r1 = carre_to_rect(c1);
    let r2 = carre_to_rect(c2);
    dist_rect_rect(&r1, &r2)
}

#[pyfunction]
pub fn dist_carre_triangle(c: &Carre, t: &Triangle) -> f64 {
    let rect = carre_to_rect(c);

    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let cpt = Point { x: t.cx, y: t.cy };

    let d1 = dist_point_rectangle(&a, &rect);
    let d2 = dist_point_rectangle(&b, &rect);
    let d3 = dist_point_rectangle(&cpt, &rect);

    d1.min(d2).min(d3)
}

#[pyfunction]
pub fn dist_carre_polygone(c: &Carre, poly: &crate::polygon::Polygone) -> f64 {
    let rect = carre_to_rect(c);

    let mut min_dist = f64::INFINITY;

    for &(x, y) in &poly.points {
        let p = Point { x, y };
        let d = dist_point_rectangle(&p, &rect);
        if d < min_dist {
            min_dist = d;
        }
    }

    min_dist
}
```

---

##  Tests unitaires — `tests/test_carre.py`

Les tests vérifient :

- les méthodes de base (périmètre, surface, création d’objet)
- la gestion des erreurs (valeurs négatives)
- toutes les distances entre carré et autres formes
- les cas de tangence et séparation

###  Tests principaux

```python
import pytest
import geocalculs as g

# --- Carré ↔ Carré ---
def test_dist_carre_carre_tangent():
    c1 = g.Carre(0, 0, 2)
    c2 = g.Carre(2, 0, 2)
    assert g.dist_carre_carre(c1, c2) == 0

def test_dist_carre_carre_separe():
    c1 = g.Carre(0, 0, 2)
    c2 = g.Carre(5, 0, 2)
    assert g.dist_carre_carre(c1, c2) == 3

# --- Carré ↔ Cercle ---
def test_dist_carre_cercle_tangent():
    carre = g.Carre(0, 0, 2)
    cercle = g.Cercle(3, 1, 1)
    assert g.dist_carre_cercle(carre, cercle) == 0

# --- Carré ↔ Triangle ---
def test_dist_carre_triangle():
    carre = g.Carre(0, 0, 2)
    tri = g.Triangle(5, 0, 6, 1, 5, 2)
    d = g.dist_carre_triangle(carre, tri)
    assert d == 3
```

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

c = g.Carre(0, 0, 2)
r = g.Rectangle(3, 0, 2, 2)
print(g.dist_carre_rectangle(c, r))   # Résultat : 1.0

p = g.Point(5, 5)
print(g.dist_point_carre(p, c))       # Résultat : ~4.24
```

---

##  Fonctions à exposer dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_rectangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_polygone, m)?)?;
```

---


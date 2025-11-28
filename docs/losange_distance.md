#  Documentation — Distances pour un Losange
**Projet : GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté :** `src/distances/losange_distance.rs`

---

##  Objectif du fichier
Ce fichier regroupe toutes les fonctions permettant de calculer la **distance minimale entre un losange et d’autres formes géométriques** du projet *GeoCalculs*.

Formes couvertes :

- Point
- Cercle
- Rectangle
- Carré
- Triangle
- Polygone
- Losange

La méthode utilisée est simple et robuste :  
 Le losange est converti en **rectangle englobant AABB** (Axis-Aligned Bounding Box).  
Ce rectangle simplifie tous les calculs en réutilisant les fonctions de distance rectangle ↔ forme.

---

##  Formules et principes utilisés

###  Conversion Losange → Rectangle AABB

Pour un losange défini par :

```
centre = (x, y)
largeur = L
hauteur = H
```

rectangle englobant :

```
x_rect = x - L/2
y_rect = y - H/2
largeur_rect = L
hauteur_rect = H
```

Ce rectangle est ensuite utilisé dans toutes les distances.

---

##  Implémentation Rust — `losange_distance.rs`

```rust
use crate::helpers::Point;
use crate::polygon::Polygone;

use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;
use crate::losange::Losange;

use crate::distances::rectangle_distance::{
    dist_point_rectangle,
    dist_rect_rect,
};

use crate::distances::cercle_distance::{
    dist_point_cercle,
    dist_cercle_cercle,
};

use crate::distances::carre_distance::carre_to_rect;

use pyo3::prelude::*;

/// ===============================================================
///     Convertir LOSANGE → RECTANGLE englobant (AABB)
/// ===============================================================
fn losange_to_rect(l: &Losange) -> Rectangle {
    Rectangle {
        x: l.x - l.largeur / 2.0,
        y: l.y - l.hauteur / 2.0,
        largeur: l.largeur,
        hauteur: l.hauteur,
    }
}

/// Convertit Polygone → Vec<Point>
fn points_polygone(p: &Polygone) -> Vec<Point> {
    p.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}

/// ===============================================================
///                     LOSANGE ↔ POINT
/// ===============================================================
#[pyfunction]
pub fn dist_point_losange(p: &Point, l: &Losange) -> f64 {
    let rect = losange_to_rect(l);
    dist_point_rectangle(p, &rect)
}

/// ===============================================================
///                     LOSANGE ↔ CERCLE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_cercle(l: &Losange, c: &Cercle) -> f64 {
    let rect = losange_to_rect(l);
    let closest_x = c.centre_x.clamp(rect.x, rect.x + rect.largeur);
    let closest_y = c.centre_y.clamp(rect.y, rect.y + rect.hauteur);

    let dx = c.centre_x - closest_x;
    let dy = c.centre_y - closest_y;

    let d = (dx * dx + dy * dy).sqrt();
    (d - c.rayon).max(0.0)
}

/// ===============================================================
///                     LOSANGE ↔ RECTANGLE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_rectangle(l: &Losange, r: &Rectangle) -> f64 {
    let rect_l = losange_to_rect(l);
    dist_rect_rect(&rect_l, r)
}

/// ===============================================================
///                     LOSANGE ↔ CARRE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_carre(l: &Losange, c: &Carre) -> f64 {
    let rect_l = losange_to_rect(l);
    let rect_c = carre_to_rect(c);
    dist_rect_rect(&rect_l, &rect_c)
}

/// ===============================================================
///                     LOSANGE ↔ TRIANGLE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_triangle(l: &Losange, t: &Triangle) -> f64 {
    let rect = losange_to_rect(l);
    let pts = vec![
        Point { x: t.ax, y: t.ay },
        Point { x: t.bx, y: t.by },
        Point { x: t.cx, y: t.cy },
    ];

    pts.iter()
        .map(|p| dist_point_rectangle(p, &rect))
        .fold(f64::INFINITY, f64::min)
}

/// ===============================================================
///                     LOSANGE ↔ POLYGONE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_polygone(l: &Losange, p: &Polygone) -> f64 {
    let rect = losange_to_rect(l);

    points_polygone(p)
        .iter()
        .map(|pt| dist_point_rectangle(pt, &rect))
        .fold(f64::INFINITY, f64::min)
}

/// ===============================================================
///                     LOSANGE ↔ LOSANGE
/// ===============================================================
#[pyfunction]
pub fn dist_losange_losange(l1: &Losange, l2: &Losange) -> f64 {
    let r1 = losange_to_rect(l1);
    let r2 = losange_to_rect(l2);
    dist_rect_rect(&r1, &r2)
}
```

---

##  Tests unitaires — `tests/test_losange.py`

Tests réalisés :

- conversion losange → rectangle
- distances losange ↔ formes
- tangence (distance = 0)
- séparation (> 0)
- valeurs attendues cohérentes

### Exemples :

```python
import geocalculs as g

def test_dist_losange_carre():
    los = g.Losange(5, 1, 2, 2)
    carre = g.Carre(0, 0, 2)
    d = g.dist_losange_carre(los, carre)
    assert d > 0

def test_dist_point_losange():
    l = g.Losange(0, 0, 4, 2)
    p = g.Point(3, 0)
    assert g.dist_point_losange(p, l) == 0
```

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

los = g.Losange(5, 1, 2, 2)
rect = g.Rectangle(0, 0, 3, 3)
print(g.dist_losange_rectangle(los, rect))

cercle = g.Cercle(0, 0, 1)
print(g.dist_losange_cercle(los, cercle))
```

---

##  À ajouter dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_losange, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_rectangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_losange_losange, m)?)?;
```

---


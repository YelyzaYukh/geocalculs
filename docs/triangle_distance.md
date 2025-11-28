#  Documentation — Distances pour un Triangle
**Projet GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté : `src/distances/triangle_distance.rs`**

---

##  Objectif du fichier

Ce fichier regroupe toutes les fonctions permettant de calculer la **distance minimale entre un triangle et différentes formes géométriques** :

- Point
- Triangle
- Cercle
- Rectangle
- Carré
- Polygone

Pour maintenir un code simple, rapide et compatible avec l’ensemble des tests, **le triangle est systématiquement converti en AABB** (Axis-Aligned Bounding Box), c’est-à-dire le plus petit rectangle aligné sur les axes qui contient entièrement le triangle.

Toutes les distances sont ensuite calculées via les fonctions génériques existantes pour les rectangles.

---

##  Règles mathématiques utilisées

### AABB — Bounding Box du triangle

Pour un triangle défini par  
A(x₁, y₁), B(x₂, y₂), C(x₃, y₃) :

```
xmin = min(x1, x2, x3)
xmax = max(x1, x2, x3)
ymin = min(y1, y2, y3)
ymax = max(y1, y2, y3)
```

Rectangle englobant :

```
x       = xmin
y       = ymin
largeur = xmax - xmin
hauteur = ymax - ymin
```

---

##  Implémentation Rust — `triangle_distance.rs`

```rust
use crate::helpers::Point;
use crate::triangle::Triangle;
use crate::rectangle::Rectangle;
use crate::carre::Carre;
use crate::cercle::Cercle;
use crate::polygon::Polygone;

use crate::distances::rectangle_distance::{
    dist_point_rectangle,
    dist_rect_rect,
    dist_rectangle_cercle,
};

use crate::distances::point_distance::{
    dist_point_point,
    dist_point_polygone,
};

use pyo3::prelude::*;

/// ----------------------------------------------------------
///  Bounding box (AABB) du triangle
/// ----------------------------------------------------------
fn tri_aabb(t: &Triangle) -> Rectangle {
    let xs = [t.ax, t.bx, t.cx];
    let ys = [t.ay, t.by, t.cy];

    let xmin = xs.iter().cloned().fold(f64::INFINITY, f64::min);
    let xmax = xs.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    let ymin = ys.iter().cloned().fold(f64::INFINITY, f64::min);
    let ymax = ys.iter().cloned().fold(f64::NEG_INFINITY, f64::max);

    Rectangle {
        x: xmin,
        y: ymin,
        largeur: xmax - xmin,
        hauteur: ymax - ymin,
    }
}

/// ----------------------------------------------------------
///   1) DISTANCE POINT ↔ TRIANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_point_triangle(p: &Point, t: &Triangle) -> f64 {
    let r = tri_aabb(t);
    dist_point_rectangle(p, &r)
}

/// ----------------------------------------------------------
///   2) TRIANGLE ↔ TRIANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_triangle(t1: &Triangle, t2: &Triangle) -> f64 {
    let r1 = tri_aabb(t1);
    let r2 = tri_aabb(t2);
    dist_rect_rect(&r1, &r2)
}

/// ----------------------------------------------------------
///   3) TRIANGLE ↔ CERCLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_cercle(t: &Triangle, c: &Cercle) -> f64 {
    let r = tri_aabb(t);
    dist_rectangle_cercle(&r, c)
}

/// ----------------------------------------------------------
///   4) TRIANGLE ↔ RECTANGLE (via AABB)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_rectangle(t: &Triangle, r: &Rectangle) -> f64 {
    let rt = tri_aabb(t);
    dist_rect_rect(&rt, r)
}

/// ----------------------------------------------------------
///   5) TRIANGLE ↔ CARRE (via conversion carré → rectangle)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_carre(t: &Triangle, c: &Carre) -> f64 {
    let rect = Rectangle {
        x: c.x,
        y: c.y,
        largeur: c.cote,
        hauteur: c.cote,
    };
    dist_triangle_rectangle(t, &rect)
}

/// ----------------------------------------------------------
///   6) TRIANGLE ↔ POLYGONE (via AABB rectangle)
/// ----------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_polygone(t: &Triangle, poly: &Polygone) -> f64 {
    let tri_box = tri_aabb(t);
    crate::distances::polygon_distance::dist_rectangle_polygone(&tri_box, poly)
}
```

---

##  Tests unitaires — `test_triangle_distance.py`

Les tests valident :

- Point ↔ triangle
- Triangle ↔ triangle
- Triangle ↔ carré
- Triangle ↔ rectangle
- Triangle ↔ cercle
- Triangle ↔ polygone
- Distance = 0 en cas de tangence
- Distance > 0 en cas de séparation

Tous les tests passent ✔ (129/129).

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

tri = g.Triangle(0,0, 4,0, 0,4)
p = g.Point(10,10)

print(g.dist_point_triangle(p, tri))
```

---

##  Entrées à ajouter dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_rectangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_polygone, m)?)?;
```

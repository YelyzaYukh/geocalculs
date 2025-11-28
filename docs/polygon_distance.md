#  Documentation — Distances pour un Polygone
**Projet : GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté :** `src/distances/polygon_distance.rs`

---

##  Objectif du fichier
Ce fichier définit l’ensemble des **fonctions de calcul des distances** impliquant un **polygone** dans le projet *GeoCalculs*.

Formes géométriques couvertes :

- Point
- Carré
- Rectangle
- Cercle
- Triangle
- Polygone

Le calcul s'appuie sur :

- les **sommets** du polygone,
- un test d’inclusion (ray casting),
- et des distances point ↔ forme.

---

##  Règles et principes utilisés

###  1. Conversion Polygone → Liste de Points

```rust
fn points_polygone(poly: &Polygone) -> Vec<Point> {
    poly.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}
```

###  2. Détection d’inclusion (Ray Casting)

Un point est **à l’intérieur** si un rayon horizontal coupe un **nombre impair** d’arêtes.

###  3. Distance minimale

La distance entre formes =  
 distance minimale entre sommets  
️ ou `0` si recouvrement détecté

---

##  Implémentation Rust — `polygon_distance.rs`

```rust
use crate::helpers::Point;
use crate::polygon::Polygone;

use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::cercle::Cercle;
use crate::triangle::Triangle;

use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::cercle_distance::dist_point_cercle;
use crate::distances::point_distance::dist_point_point;

use pyo3::prelude::*;

/// Transforme un Polygone en liste de Points
fn points_polygone(poly: &Polygone) -> Vec<Point> {
    poly.points
        .iter()
        .map(|(x, y)| Point { x: *x, y: *y })
        .collect()
}

/// ---------------------------------------------------------
///   Test si un point est à l’intérieur d’un polygone (ray casting)
/// ---------------------------------------------------------
fn point_in_poly(px: f64, py: f64, pts: &[(f64, f64)]) -> bool {
    let mut inside = false;
    let n = pts.len();

    for i in 0..n {
        let (x1, y1) = pts[i];
        let (x2, y2) = pts[(i + 1) % n];

        let intersects = ((y1 > py) != (y2 > py))
            && (px < (x2 - x1) * (py - y1) / (y2 - y1 + 1e-12) + x1);

        if intersects {
            inside = !inside;
        }
    }

    inside
}

/// ---------------------------------------------------------
///   POLYGONE ↔ CARRE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_carre_polygone(carre: &Carre, poly: &Polygone) -> f64 {
    let rect = Rectangle {
        x: carre.x,
        y: carre.y,
        largeur: carre.cote,
        hauteur: carre.cote,
    };

    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, &rect))
        .fold(f64::INFINITY, f64::min)
}

/// ---------------------------------------------------------
///   POLYGONE ↔ RECTANGLE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_rectangle_polygone(rect: &Rectangle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_rectangle(p, rect))
        .fold(f64::INFINITY, f64::min)
}

/// ---------------------------------------------------------
///   POLYGONE ↔ CERCLE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_cercle_polygone(cercle: &Cercle, poly: &Polygone) -> f64 {
    points_polygone(poly)
        .iter()
        .map(|p| dist_point_cercle(p, cercle))
        .fold(f64::INFINITY, f64::min)
}

/// ---------------------------------------------------------
///   POLYGONE ↔ TRIANGLE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_triangle_polygone(tri: &Triangle, poly: &Polygone) -> f64 {
    let tri_pts = vec![
        Point { x: tri.ax, y: tri.ay },
        Point { x: tri.bx, y: tri.by },
        Point { x: tri.cx, y: tri.cy },
    ];

    let poly_pts = points_polygone(poly);

    let mut min = f64::INFINITY;

    for tp in &tri_pts {
        for pp in &poly_pts {
            let dx = tp.x - pp.x;
            let dy = tp.y - pp.y;
            let d = (dx * dx + dy * dy).sqrt();
            if d < min {
                min = d;
            }
        }
    }

    min
}

/// ---------------------------------------------------------
///   POLYGONE ↔ POLYGONE
/// ---------------------------------------------------------
#[pyfunction]
pub fn dist_poly_poly(p1: &Polygone, p2: &Polygone) -> f64 {
    let pts1 = points_polygone(p1);
    let pts2 = points_polygone(p2);

    // 1) Chevauchement ?
    for a in &p1.points {
        if point_in_poly(a.0, a.1, &p2.points) {
            return 0.0;
        }
    }
    for b in &p2.points {
        if point_in_poly(b.0, b.1, &p1.points) {
            return 0.0;
        }
    }

    // 2) Distance minimale
    let mut min = f64::INFINITY;
    for a in &pts1 {
        for b in &pts2 {
            let dx = a.x - b.x;
            let dy = a.y - b.y;
            let dist = (dx * dx + dy * dy).sqrt();
            if dist < min {
                min = dist;
            }
        }
    }

    min
}

/// ===============================================================
///   DISTANCE POINT → POLYGONE
/// ===============================================================
#[pyfunction]
pub fn dist_point_polygone(p: &Point, poly: &Polygone) -> f64 {
    if point_in_poly(p.x, p.y, &poly.points) {
        return 0.0;
    }

    let mut best = f64::INFINITY;
    for (x, y) in &poly.points {
        let q = Point { x: *x, y: *y };
        best = best.min(dist_point_point(p, &q));
    }

    best
}
```

---

##  Tests unitaires — `tests/test_polygon.py`

Tests couvrent :

- distances polygone ↔ rectangle
- polygone ↔ cercle
- polygone ↔ polygone
- cas tangents et séparés
- exactitude de `point_in_poly`

### Exemples :

```python
import geocalculs as g
import math

def test_dist_polygone_point_inside():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    p = g.Point(2, 2)
    assert g.dist_point_polygone(p, poly) == 0

def test_dist_polygone_rectangle_separe():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    rect = g.Rectangle(10, 10, 3, 3)
    d = g.dist_rectangle_polygone(rect, poly)
    attendu = math.sqrt((10 - 4)**2 + (10 - 4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)

def test_dist_polygone_polygone_overlap():
    p1 = g.Polygone([(0,0),(4,0),(4,4),(0,4)])
    p2 = g.Polygone([(2,2),(6,2),(6,6),(2,6)])
    assert g.dist_poly_poly(p1, p2) == 0
```

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
carre = g.Carre(5, 0, 2)

print(g.dist_carre_polygone(carre, poly))  # 1.0

p = g.Point(10, 10)
print(g.dist_point_polygone(p, poly))       # ≈ 8.48
```

---

##  Fonctions à exposer dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_carre_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_rectangle_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_triangle_polygone, m)?)?;
m.add_function(wrap_pyfunction!(dist_poly_poly, m)?)?;
```

---


#  Documentation — Distances pour un Cercle
**Projet : GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté : `src/distances/cercle_distance.rs`**

---

##  Objectif du fichier
Ce module regroupe toutes les fonctions permettant de **calculer la distance minimale entre un cercle et d’autres formes géométriques** du projet *GeoCalculs*.

Formes couvertes :

- Point
- Cercle
- Rectangle
- Carré
- Triangle
- Polygone

Chaque fonction retourne une **distance minimale positive**, ou `0.0` si les formes sont tangentes ou se chevauchent.

---

##  Principes mathématiques

###  1. Distance Point ↔ Cercle
```
d = max(0, sqrt((x - x_c)^2 + (y - y_c)^2) - r)
```

###  2. Distance Cercle ↔ Cercle
```
d = max(0, sqrt((x1 - x2)^2 + (y1 - y2)^2) - r1 - r2)
```

###  3. Distance Cercle ↔ Rectangle
On projette le centre du cercle sur le rectangle :

```
cx = clamp(x_centre, rect.x, rect.x + rect.largeur)
cy = clamp(y_centre, rect.y, rect.y + rect.hauteur)
```

```
d = max(0, sqrt((x_centre - cx)^2 + (y_centre - cy)^2) - r)
```

###  4. Distance Cercle ↔ Carré
Conversion du carré en rectangle équivalent, puis utilisation de la distance **carré ↔ cercle**.

###  5. Distance Cercle ↔ Triangle
Deux méthodes combinées :
- distance sommet–cercle
- distance centre–segment – rayon

###  6. Distance Cercle ↔ Polygone
Distance minimale entre les sommets du polygone et le cercle.

---

##  Implémentation Rust — `cercle_distance.rs`

```rust
use crate::helpers::Point;
use crate::cercle::Cercle;
use crate::carre::Carre;
use crate::rectangle::Rectangle;
use crate::triangle::Triangle;
use crate::polygon::Polygone;

use crate::distances::rectangle_distance::dist_point_rectangle;
use crate::distances::carre_distance::dist_carre_cercle;
use crate::distances::point_distance::dist_point_segment;

use pyo3::prelude::*;

/// Distance point ↔ cercle
#[pyfunction]
pub fn dist_point_cercle(p: &Point, c: &Cercle) -> f64 {
    let dx = p.x - c.centre_x;
    let dy = p.y - c.centre_y;
    let d = (dx*dx + dy*dy).sqrt();
    (d - c.rayon).max(0.0)
}

/// Distance cercle ↔ cercle
#[pyfunction]
pub fn dist_cercle_cercle(c1: &Cercle, c2: &Cercle) -> f64 {
    let dx = c1.centre_x - c2.centre_x;
    let dy = c1.centre_y - c2.centre_y;
    let d = (dx*dx + dy*dy).sqrt();
    (d - c1.rayon - c2.rayon).max(0.0)
}

/// Distance cercle ↔ rectangle
#[pyfunction]
pub fn dist_cercle_rectangle(c: &Cercle, r: &Rectangle) -> f64 {
    let cx = c.centre_x.clamp(r.x, r.x + r.largeur);
    let cy = c.centre_y.clamp(r.y, r.y + r.hauteur);

    let dx = c.centre_x - cx;
    let dy = c.centre_y - cy;

    let d = (dx*dx + dy*dy).sqrt();
    (d - c.rayon).max(0.0)
}

/// Distance cercle ↔ carré
#[pyfunction]
pub fn dist_cercle_carre(c: &Cercle, car: &Carre) -> f64 {
    dist_carre_cercle(car, c)
}

/// Distance cercle ↔ triangle
#[pyfunction]
pub fn dist_cercle_triangle(c: &Cercle, t: &Triangle) -> f64 {
    let a = Point { x: t.ax, y: t.ay };
    let b = Point { x: t.bx, y: t.by };
    let cc = Point { x: t.cx, y: t.cy };

    let centre = Point { x: c.centre_x, y: c.centre_y };
    let r = c.rayon;

    let mut best = dist_point_cercle(&a, c)
        .min(dist_point_cercle(&b, c))
        .min(dist_point_cercle(&cc, c));

    let d1 = dist_point_segment(&centre, &a, &b) - r;
    let d2 = dist_point_segment(&centre, &b, &cc) - r;
    let d3 = dist_point_segment(&centre, &cc, &a) - r;

    best = best.min(d1).min(d2).min(d3);

    if best < 0.0 {
        0.0
    } else {
        best
    }
}

/// Distance cercle ↔ polygone
#[pyfunction]
pub fn dist_cercle_polygone(c: &Cercle, p: &Polygone) -> f64 {
    let mut best = f64::INFINITY;

    for (x, y) in &p.points {
        let pt = Point { x: *x, y: *y };
        best = best.min(dist_point_cercle(&pt, c));
    }

    best
}
```

---

##  Tests unitaires — `tests/test_cercle.py`

Les tests couvrent :

- tangence (distance = 0)
- séparation (distance > 0)
- exactitude des valeurs attendues

### Exemples :

```python
import geocalculs as g
import math

def test_dist_point_cercle():
    c = g.Cercle(0, 0, 2)
    p = g.Point(4, 0)
    assert g.dist_point_cercle(p, c) == 2.0

def test_dist_cercle_cercle_tangent():
    c1 = g.Cercle(0, 0, 2)
    c2 = g.Cercle(4, 0, 2)
    assert g.dist_cercle_cercle(c1, c2) == 0

def test_dist_cercle_rectangle():
    c = g.Cercle(5, 5, 1)
    r = g.Rectangle(0, 0, 3, 3)
    assert g.dist_cercle_rectangle(c, r) > 0
```

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

c1 = g.Cercle(0, 0, 2)
c2 = g.Cercle(5, 0, 1)

print(g.dist_cercle_cercle(c1, c2))  # Résultat : 2.0

r = g.Rectangle(3, 0, 2, 2)
print(g.dist_cercle_rectangle(c1, r))  # Résultat : ~1.0
```

---

##  Fonctions à exposer dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_rectangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_cercle_polygone, m)?)?;
```

---


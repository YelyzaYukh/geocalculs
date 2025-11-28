#  Documentation — Distances pour un Rectangle
**Projet : GeoCalculs**  
**Auteur : Youssef Jemaa**  
**Fichier documenté :** `src/distances/rectangle_distance.rs`

---

##  Objectif du fichier
Ce module définit toutes les fonctions permettant de calculer la **distance minimale entre un rectangle et d’autres formes géométriques** dans le projet *GeoCalculs*.

Formes couvertes :

- Point
- Rectangle
- Carré
- Cercle
- Triangle
- Polygone

Chaque fonction retourne la **distance minimale**, et `0.0` lorsque les formes sont tangentes ou se chevauchent.

---

##  Principes mathématiques utilisés

###  Distance Point ↔ Rectangle

```
x_proche = clamp(px, x_rect, x_rect + largeur)
y_proche = clamp(py, y_rect, y_rect + hauteur)

distance = sqrt((px - x_proche)^2 + (py - y_proche)^2)
```

---

###  Distance Rectangle ↔ Rectangle

```
Si r1 est à droite de r2 → dx = r1.x - (r2.x + r2.largeur)
Si r2 est à droite de r1 → dx = r2.x - (r1.x + r1.largeur)
Sinon dx = 0

Même logique pour dy
```

```
distance = sqrt(dx^2 + dy^2)
```

---

###  Rectangle ↔ Cercle

On prend le point du rectangle le plus proche du centre :

```
cx = clamp(c_x, rx, rx + largeur)
cy = clamp(c_y, ry, ry + hauteur)

distance = max(0, sqrt((c_x - cx)^2 + (c_y - cy)^2) - rayon)
```

---

##  Tests unitaires — `tests/test_rectangle.py`

Tests vérifient :

- distances exactes pour tous les cas
- tangence (`== 0`)
- valeurs positives (`> 0`)

### Exemples :

```python
import geocalculs as g
import math

def test_dist_point_rectangle_inside():
    r = g.Rectangle(0, 0, 4, 3)
    p = g.Point(2, 1)
    assert g.dist_point_rectangle(p, r) == 0

def test_dist_rect_rect_tangent():
    r1 = g.Rectangle(0, 0, 2, 2)
    r2 = g.Rectangle(2, 0, 3, 2)
    assert g.dist_rect_rect(r1, r2) == 0

def test_dist_rectangle_cercle():
    r = g.Rectangle(0, 0, 2, 2)
    c = g.Cercle(5, 5, 1)
    d = g.dist_rectangle_cercle(r, c)
    attendu = math.sqrt((5 - 2)**2 + (5 - 2)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)
```

---

##  Exemple d’utilisation Python

```python
import geocalculs as g

r1 = g.Rectangle(0, 0, 4, 2)
r2 = g.Rectangle(6, 0, 2, 2)
print(g.dist_rect_rect(r1, r2))  # 2.0

p = g.Point(10, 10)
print(g.dist_point_rectangle(p, r1))  # ≈ 11.31
```

---

##  Fonctions à exposer dans `src/lib.rs`

```rust
m.add_function(wrap_pyfunction!(dist_point_rectangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_rect_rect, m)?)?;
m.add_function(wrap_pyfunction!(dist_rectangle_carre, m)?)?;
m.add_function(wrap_pyfunction!(dist_rectangle_cercle, m)?)?;
m.add_function(wrap_pyfunction!(dist_rectangle_triangle, m)?)?;
m.add_function(wrap_pyfunction!(dist_rectangle_polygone, m)?)?;
```

---


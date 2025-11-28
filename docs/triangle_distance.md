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

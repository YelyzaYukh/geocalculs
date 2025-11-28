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


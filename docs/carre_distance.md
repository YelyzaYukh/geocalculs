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

##  Tests unitaires — `tests/test_carre.py`

Les tests vérifient :

- les méthodes de base (périmètre, surface, création d’objet)
- la gestion des erreurs (valeurs négatives)
- toutes les distances entre carré et autres formes
- les cas de tangence et séparation


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



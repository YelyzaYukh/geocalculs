# Documentation : Classe `Polygone`

## 1. Vue d'ensemble

La classe `Polygone` permet de définir, valider et manipuler des **polygones géométriques arbitraires** en 2D.

Contrairement aux formes prédéfinies (Carré, Rectangle), un polygone est défini par une liste ordonnée de sommets $(x, y)$.

**Fichier source :** `src/polygon.rs`

---

## 2. Règles de Validation (Construction)

Lors de la création d'un `Polygone`, le constructeur effectue des vérifications mathématiques strictes pour garantir l'intégrité de la forme. Si une règle n'est pas respectée, une erreur `ValueError` est levée.

### A. Nombre de sommets
Un polygone doit être composé d'au moins **3 points**.
* **Erreur levée :** `"Un polygone doit avoir au moins 3 points."`

### B. Anti-Colinéarité
Trois points consécutifs ne peuvent pas être alignés sur la même droite. Cela créerait des côtés "plats" inutiles ou des formes dégénérées.
* **Erreur levée :** `"Points colinéaires détectés aux indices X, Y, Z."`

### C. Anti-Auto-Intersection (Polygone Simple)
Les côtés du polygone ne doivent jamais se croiser (exemple : forme en "8" ou en "sablier"). Le polygone doit être **simple**.
* **Algorithme :** Vérification croisée de tous les segments ($O(N^2)$).
* **Erreur levée :** `"Le polygone s'auto-intersecte (croisement de lignes)."`

---

## 3. API Python

### Constructeur
```python
def __init__(points: list[tuple[float, float]])
```

# Polygone — Référence API

## 1. Attributs

### `points`
Liste de tuples représentant les coordonnées \((x, y)\) des sommets.  
L'ordre est important (sens horaire ou anti-horaire).

- **Type :** `list[tuple[float, float]]`
- **Accès :** Lecture / Écriture

---

## 2. Méthodes

| Méthode               | Retour | Description                                                                 | Complexité |
|-----------------------|--------|-----------------------------------------------------------------------------|------------|
| `perimetre()`         | float  | Calcule la longueur totale du contour (somme des distances euclidiennes).  | \(O(N)\)   |
| `surface()`           | float  | Calcule l’aire via la Formule du Lacet.                                    | \(O(N)\)   |
| `nombre_de_sommets()` | int    | Retourne le nombre de points définissant le polygone.                      | \(O(1)\)   |

---

## 3. Formules Mathématiques

### A. Périmètre

Le périmètre est la somme des distances entre chaque point consécutif \(P_i\) et \(P_{i+1}\),  
avec retour au point de départ.

\[
P = \sum_{i=0}^{n-1} \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2}
\]

---

### B. Surface (Formule du Lacet)

L’aire est calculée en utilisant la méthode des déterminants (*Shoelace Formula*).  
Elle fonctionne pour tout polygone simple (convexe ou concave).

\[
A = \frac{1}{2} \left| \sum_{i=0}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|
\]

---

## 4. Exemples d'Utilisation

### Cas Valide : Hexagone

```python
import geocalculs as g

# Définition d'un hexagone
points = [
    (1.0, 0.0), (0.5, 0.866), (-0.5, 0.866),
    (-1.0, 0.0), (-0.5, -0.866), (0.5, -0.866)
]

poly = g.Polygone(points)

print(f"Périmètre : {poly.perimetre()}")
print(f"Surface   : {poly.surface()}")
```

# Cas Invalide : Auto-Intersection (Sablier)

```python
import geocalculs as g

# Forme croisée (invalide)
points_croises = [
    (0, 0), (10, 0),  # Bas
    (0, 10), (10, 10) # Haut croisé
]

try:
    p = g.Polygone(points_croises)
except ValueError as e:
    print(f"Erreur attrapée : {e}")
    # Sortie : Le polygone s'auto-intersecte (croisement de lignes).

```
# 5. Détails Techniques (Rust)

L’implémentation interne se trouve dans `src/polygon.rs`.  
Elle contient plusieurs algorithmes géométriques essentiels :

---

## `sont_colineaires`

Vérifie si trois points sont alignés en utilisant le **produit en croix**.

On considère que trois points forment un triangle plat si :

\[
\epsilon = 10^{-9}
\]

---

## `orientation`

Détermine si trois points tournent :

- dans le **sens horaire**
- dans le **sens anti-horaire**
- ou sont **alignés**

---

## `segments_se_croisent`

Détermine si deux segments s’intersectent proprement.

- Utilise l’orientation relative des triplets de points  
- Exclut les cas où les extrémités sont simplement connectées

---


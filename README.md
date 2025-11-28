# GeoCalculs 

**Bibliothèque de géométrie haute performance pour Python, propulsée par Rust.**

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Rust](https://img.shields.io/badge/backend-Rust-orange)]()

##  Présentation

**GeoCalculs** est une bibliothèque Python conçue pour les calculs géométriques intensifs et la physique 2D. Elle combine la **simplicité de Python** avec la **performance brute de Rust**.

Contrairement aux bibliothèques classiques, GeoCalculs implémente des algorithmes avancés pour garantir précision et rapidité :
- **Théorème des Axes Séparateurs (SAT)** pour la détection de collision ultra-rapide.
- **Triangulation (Ear Clipping)** pour gérer les formes concaves complexes sans erreur.

### Pourquoi utiliser GeoCalculs ?
* **Ultra-Rapide :** Le cœur mathématique est compilé en code machine (Rust).
* **Robuste :** Validation stricte des formes (anti-auto-intersection, anti-colinéarité).
* **Moteur Physique :** Détection de collision précise (pixel-perfect) et calcul de distances minimales.
* **Universel :** Gérez des interactions entre n'importe quelles formes (Cercle vs Polygone, Losange vs Triangle, etc.).

---

##  Installation

Vous pouvez installer la bibliothèque directement via le fichier `.whl` fourni :

```bash
pip install geocalculs-0.1.0-cp310-cp310-manylinux_x86_64.whl
```
(Pour les développeurs souhaitant compiler depuis la source) :

```bash
maturin develop --release
```

##  Fonctionnalités

### 1. Formes Supportées
Toutes les formes sont définies comme des objets manipulables avec validation intégrée.

* **Point** `(x, y)`
* **Cercle** `(centre_x, centre_y, rayon)`
* **Carré** `(x, y, côté)`
* **Rectangle** `(x, y, largeur, hauteur)`
* **Triangle** `(ax, ay, bx, by, cx, cy)`
* **Losange** `(x, y, largeur, hauteur)`
* **Polygone** `(liste de points)` — *Supporte les formes concaves et convexes.*

### 2. Calculs & Physique
* **Surface & Périmètre** (Formule de Héron, Formule du Lacet).
* **Intersection (`intersecte`)** : Détecte si deux objets se touchent ou se chevauchent.
    * Utilise le **SAT** pour les formes convexes.
    * Utilise la **Triangulation** pour les formes concaves.
* **Inclusion (`appartient`)** : Vérifie si un point est à l'intérieur d'une forme.
* **Distance Minimale** : Calcule la distance la plus courte entre les bords de deux formes quelconques.

---

##  Exemples d'Utilisation

### 1. Création et Calculs de base

```python
import geocalculs as g

# Création d'un rectangle
rect = g.Rectangle(0, 0, 10, 5) # x, y, w, h

print(f"Surface : {rect.surface()}")      # 50.0
print(f"Périmètre : {rect.perimetre()}")  # 30.0
```
# Création d'un polygone (Hexagone)
points = [(1,0), (0.5, 0.86), (-0.5, 0.86), (-1,0), (-0.5, -0.86), (0.5, -0.86)]
hexagone = g.Polygone(points)

### 2. Détection de Collision (Intersection)

Le moteur gère intelligemment les collisions, même pour des formes complexes.

```python
# Un Triangle qui "pique" dans un Rectangle
rect = g.Rectangle(0, 0, 4, 2)
tri  = g.Triangle(2, 1,  2, 4,  4, 4) # La pointe (2,1) est DANS le rectangle

if g.intersecte(rect, tri):
    print("BOUM ! Collision détectée ")
else:
    print("Les formes sont séparées.")

```
### 3. Gestion des Polygones Concaves (Forme en "U")

GeoCalculs sait qu'un polygone concave a des "trous". Il ne détectera pas de collision dans le vide.

```python
# Forme en "U" (Concave)
points_u = [(0,0), (4,0), (4,4), (3,4), (3,1), (1,1), (1,4), (0,4)]
forme_u = g.Polygone(points_u)

# Objet placé dans le "creux" du U (ne touche pas les murs)
objet_dans_le_vide = g.Carre(1.5, 2, 0.5)

# Résultat : False (Pas de collision, car on est dans le vide !)
print(g.intersecte(forme_u, objet_dans_le_vide))

### 4. Calcul de Distance

```python
# Distance entre un Cercle et un Carré
cercle = g.Cercle(0, 0, 1)  # Rayon 1, à l'origine
carre = g.Carre(10, 0, 2)   # Loin sur l'axe X

dist = g.dist_cercle_carre(cercle, carre)
print(f"Distance minimale : {dist}") # Résultat précis
```

## Architecture Technique

Ce projet utilise une architecture hybride pour maximiser la performance :

1.  **Frontend Python (`.pyi`)** : Fournit une interface claire et l'autocomplétion pour les IDE modernes.
2.  **Backend Rust** :
    * **Moteur SAT** : Algorithme d'intersection ultra-rapide basé sur les projections d'ombres.
    * **Ear Clipping** : Algorithme de décomposition qui découpe dynamiquement les polygones complexes en triangles simples pour des calculs fiables.

---

## Tests

La fiabilité est garantie par une suite de tests unitaires complète (Pytest).

```bash
# Lancer tous les tests
pytest

# Lancer les tests d'intersection spécifiques
pytest tests/test_intersection.py
```
   
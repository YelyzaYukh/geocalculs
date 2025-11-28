# Documentation des toutes les fonctions — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de **toutes les fonctions** développées dans le cadre du projet *GeoCalculs*.

Bibliothèque de fonctions géométriques écrites en **Rust** et exposées à **Python** via **PyO3**.
---
## Groupe d'auteurs : <br>
**Yelyzaveta YUKHNOVA** <br>
**Mohammed Djellouli** <br>
**Youssef Jemaa**  <br>
**Mohammed Achref Wassim**<br>
---

## Table des matières

1. [Validation](#validation)
2. [Formes géométriques](#formes-géométriques)
   - [Losange](#losange)
   - [Cercle](#cercle)
   - [Triangle](#triangle)
   - [Carré](#carré)
   - [Rectangle](#rectangle)
   - [Polygone](#polygone)
3. [Fonctions d'appartenance](#fonctions-dappartenance)
4. [Fonctions d'intersection](#fonctions-dinteresection)
5. [Distances entre points](#distances-entre-points)
6. [Distances entre formes](#distances-entre-formes)
7. [Fonctions utilitaires](#fonctions-utilitaires)

---

## Validation

### `valider_valeurs`
```rust
pub fn valider_valeurs(values: Vec<f64>) -> PyResult<bool>
```
Valide un vecteur de valeurs numériques.

**Paramètres:**
- `values`: Liste de nombres à valider

**Retour:** `bool` - Résultat de la validation

---

## Formes géométriques

### Losange

#### `new`
```rust
pub fn new(diagonale1: f64, diagonale2: f64, cote: f64) -> PyResult<Self>
```
Crée un nouveau losange.

**Paramètres:**
- `diagonale1`: Longueur de la première diagonale
- `diagonale2`: Longueur de la seconde diagonale
- `cote`: Longueur d'un côté

#### `perimetre`
```rust
pub fn perimetre(&self) -> f64
```
Calcule le périmètre du losange à partir de la longueur d'un côté.

**Retour:** Périmètre du losange

---

### Cercle

#### `new`
```rust
fn new(centre_x: f64, centre_y: f64, rayon: f64) -> PyResult<Self>
```
Crée un nouveau cercle.

**Paramètres:**
- `centre_x`: Coordonnée X du centre
- `centre_y`: Coordonnée Y du centre
- `rayon`: Rayon du cercle (doit être ≥ 0)

**Erreurs:** Lève `PyValueError` si le rayon est négatif

#### `perimetre`
```rust
pub fn perimetre(&self) -> f64
```
Calcule le périmètre (circonférence) du cercle.

**Formule:** `2π × rayon`

#### `surface`
```rust
pub fn surface(&self) -> f64
```
Calcule la surface du cercle.

**Formule:** `π × rayon²`

---

### Triangle

#### `new`
```rust
pub fn new(a: Point2D, b: Point2D, c: Point2D) -> Result<Self, &'static str>
```
Crée un nouveau triangle à partir de trois points.

**Paramètres:**
- `a`, `b`, `c`: Points 2D définissant le triangle

**Erreurs:**
- Points non distincts
- Points alignés (pas un triangle valide)

#### `definir_triangle`
```rust
pub fn definir_triangle(
    ax: f64, ay: f64,
    bx: f64, by: f64,
    cx: f64, cy: f64
) -> PyResult<String>
```
Définit un triangle à partir de coordonnées.

**Paramètres:**
- `ax, ay`: Coordonnées du point A
- `bx, by`: Coordonnées du point B
- `cx, cy`: Coordonnées du point C

**Retour:** Message de confirmation avec les coordonnées

#### `perimetre_triangle`
```rust
pub fn perimetre_triangle(a: f64, b: f64, c: f64) -> f64
```
Calcule le périmètre d'un triangle.

**Paramètres:**
- `a`, `b`, `c`: Longueurs des côtés

**Formule:** `a + b + c`

#### `surface_triangle`
```rust
pub fn surface_triangle(a: f64, b: f64, c: f64) -> f64
```
Calcule la surface d'un triangle avec la formule de Héron.

**Paramètres:**
- `a`, `b`, `c`: Longueurs des côtés

**Formule:** `√(p(p-a)(p-b)(p-c))` où `p = (a+b+c)/2`

---

### Carré

#### `new`
```rust
fn new(x: f64, y: f64, cote: f64) -> PyResult<Self>
```
Crée un nouveau carré.

**Paramètres:**
- `x`: Coordonnée X du coin supérieur gauche (doit être ≥ 0)
- `y`: Coordonnée Y du coin supérieur gauche (doit être ≥ 0)
- `cote`: Longueur du côté (doit être > 0)

**Erreurs:** Lève `PyValueError` si les contraintes ne sont pas respectées

#### `perimetre`
```rust
pub fn perimetre(&self) -> f64
```
Calcule le périmètre du carré.

**Formule:** `4 × côté`

#### `surface`
```rust
pub fn surface(&self) -> f64
```
Calcule la surface du carré.

**Formule:** `côté²`

---

### Rectangle

#### `new`
```rust
pub fn new(largeur: f64, hauteur: f64) -> Result<Self, &'static str>
```
Crée un nouveau rectangle.

**Paramètres:**
- `largeur`: Largeur (doit être > 0)
- `hauteur`: Hauteur (doit être > 0)

**Erreurs:** Message d'erreur si les dimensions ne sont pas strictement positives

#### `definir_rectangle`
```rust
pub fn definir_rectangle(largeur: f64, hauteur: f64) -> PyResult<String>
```
Définit un rectangle et retourne un message de confirmation.

**Paramètres:**
- `largeur`: Largeur du rectangle
- `hauteur`: Hauteur du rectangle

#### `perimetre`
```rust
pub fn perimetre(&self) -> f64
```
Calcule le périmètre du rectangle.

**Formule:** `2 × (largeur + hauteur)`

#### `surface`
```rust
pub fn surface(&self) -> f64
```
Calcule la surface du rectangle.

**Formule:** `largeur × hauteur`

---

### Polygone

#### `new`
```rust
fn new(points: Vec<(f64, f64)>) -> Self
```
Crée un nouveau polygone.

**Paramètres:**
- `points`: Liste de coordonnées (x, y) des sommets

#### `perimetre`
```rust
fn perimetre(&self) -> f64
```
Calcule le périmètre du polygone.

**Retour:** Somme des distances entre sommets consécutifs (retour à 0 si < 2 points)

#### `surface`
```rust
fn surface(&self) -> f64
```
Calcule la surface du polygone avec la formule du lacet (Shoelace).

**Formule:** `|Σ(x₁y₂) - Σ(x₂y₁)| / 2`

**Retour:** 0 si < 3 points

#### `nombre_de_sommets`
```rust
fn nombre_de_sommets(&self) -> usize
```
Retourne le nombre de sommets du polygone.

---

## Fonctions d'appartenance

### `appartient`
```rust
pub fn appartient(px: f64, py: f64, forme: &Bound<'_, PyAny>, _mode: &str) -> PyResult<bool>
```
Détermine si un point appartient à une forme géométrique.

**Paramètres:**
- `px`, `py`: Coordonnées du point
- `forme`: Objet forme géométrique
- `_mode`: Mode de test (paramètre réservé)

**Retour:** `true` si le point appartient à la forme

---

## Fonctions d'intersection

### Détection de collision

Le module **intersection** permet de détecter si deux formes géométriques se touchent ou se chevauchent.

**Points forts:**
- **Universel**: Fonctionne entre n'importe quelles formes (Triangle vs Cercle, Polygone vs Rectangle, etc.)
- **Robuste**: Gère les polygones convexes (Carré, Hexagone) et concaves (Forme en U, Étoile)
- **Performant**: Utilise des algorithmes d'élimination rapide (SAT) et des techniques de décomposition géométrique (triangulation)

### `intersecte`
```rust
pub fn intersecte(forme_a: &Bound<'_, PyAny>, forme_b: &Bound<'_, PyAny>, mode: &str) -> PyResult<bool>
```

Fonction principale de détection d'intersection entre deux formes géométriques.

**Paramètres:**
- `forme_a`: Première forme géométrique
- `forme_b`: Seconde forme géométrique
- `mode`: Mode de retour (par défaut "bool")

**Retour:** `true` si les formes se touchent ou se chevauchent

**Algorithmes utilisés:**

1. **Théorème des Axes Séparateurs (SAT)** - Pour formes convexes
   - Projette chaque forme sur des axes perpendiculaires à leurs côtés
   - Analyse si leurs projections se chevauchent
   - S'il existe un axe où les projections ne se recouvrent pas → pas de collision

2. **Triangulation "Ear Clipping"** - Pour formes concaves
   - Découpe le polygone concave en triangles
   - Teste chaque triangle individuellement via SAT
   - Si au moins un triangle touche l'autre objet → collision détectée

**Flux d'exécution:**
1. Extraction et conversion des formes Python en structures internes
2. Rectangle/Carré/Triangle → Liste de points (polygone convexe)
3. Polygone concave → Découpage en triangles
4. Comparaison via `sat_poly_poly()` ou `sat_poly_cercle()`

**Exemple 1 - Cas simple (Convexe):**
```python
import geocalculs as g

rect = g.Rectangle(0, 0, 4, 2)
tri  = g.Triangle(2, 1, 2, 4, 4, 4)

if g.intersecte(rect, tri):
    print("Collision détectée !")
```

**Exemple 2 - Cas complexe (Concave - Forme en U):**
```python
import geocalculs as g

# Création d'un U (Concave)
points_u = [(0,0), (4,0), (4,4), (3,4), (3,1), (1,1), (1,4), (0,4)]
forme_u = g.Polygone(points_u)

# Objet dans le creux du U
objet_dans_le_vide = g.Carre(1.5, 2, 0.5)

# Grâce à la triangulation, renvoie False
collision = g.intersecte(forme_u, objet_dans_le_vide)
```

### Fonctions auxiliaires d'intersection

#### `sat_poly_poly`
```rust
fn sat_poly_poly(poly_a: &[(f64, f64)], poly_b: &[(f64, f64)]) -> bool
```
Teste l'intersection entre deux polygones convexes via SAT.

#### `sat_poly_cercle`
```rust
fn sat_poly_cercle(poly: &[(f64, f64)], centre: (f64, f64), rayon: f64) -> bool
```
Teste l'intersection entre un polygone et un cercle.

#### `trianguler`
```rust
fn trianguler(points: &[(f64, f64)]) -> Vec<Vec<(f64, f64)>>
```
Découpe un polygone concave en triangles via l'algorithme "Ear Clipping".

**Retour:** Liste de triangles (chacun représenté par 3 points)

#### `extraire_forme`
```rust
fn extraire_forme(forme: &Bound<'_, PyAny>) -> PyResult<FormeInterne>
```
Convertit un objet Python (Rectangle, Triangle, etc.) en structure interne unifiée.

---

### Scénarios de test couverts

| Test | Description | Objectif |
|------|-------------|----------|
| **Le "U" (Concave)** | Objet dans le creux du U | Valider que la triangulation ne « bouche » pas les trous |
| **L'Étoile** | Collision avec forme étoilée complexe | Vérifier la robustesse de l'Ear Clipping |
| **Rectangle vs Triangle** | Triangle traversant un rectangle | Tester le SAT sur des axes inclinés |
| **Polygone vs Cercle** | Cercle touchant un bord ou sommet | Tester le mode hybride (courbe vs angulaire) |
| **Inclusion** | Objet complètement contenu | Vérifier que l'inclusion compte comme collision |

---

## Distances entre points

### `distance_2d`
```rust
pub fn distance_2d(x1: f64, y1: f64, x2: f64, y2: f64) -> f64
```
Calcule la distance euclidienne entre deux points en 2D.

**Paramètres:**
- `x1, y1`: Coordonnées du premier point
- `x2, y2`: Coordonnées du second point

**Formule:** `√((x₂-x₁)² + (y₂-y₁)²)`

---

## Distances entre formes

### Distances Point ↔ Formes

#### `dist_point_cercle`
```rust
pub fn dist_point_cercle(p: &Point, c: &Cercle) -> f64
```
Distance entre un point et un cercle (0 si le point est à l'intérieur).

#### `dist_point_rectangle`
```rust
pub fn dist_point_rectangle(p: &Point, r: &Rectangle) -> f64
```
Distance entre un point et un rectangle.

#### `dist_point_carre`
```rust
pub fn dist_point_carre(p: &Point, c: &Carre) -> f64
```
Distance entre un point et un carré.

#### `dist_point_triangle`
```rust
pub fn dist_point_triangle(p: &Point, t: &Triangle) -> f64
```
Distance entre un point et un triangle (via AABB).

#### `dist_point_losange`
```rust
pub fn dist_point_losange(p: &Point, l: &Losange) -> f64
```
Distance entre un point et un losange.

#### `dist_point_polygone`
```rust
pub fn dist_point_polygone(p: &Point, poly: &Polygone) -> f64
```
Distance entre un point et un polygone (0 si le point est à l'intérieur).

---

### Distances Cercle ↔ Formes

#### `dist_cercle_cercle`
```rust
pub fn dist_cercle_cercle(c1: &Cercle, c2: &Cercle) -> f64
```
Distance entre deux cercles.

#### `dist_cercle_rectangle`
```rust
pub fn dist_cercle_rectangle(c: &Cercle, r: &Rectangle) -> f64
```
Distance entre un cercle et un rectangle.

#### `dist_cercle_carre`
```rust
pub fn dist_cercle_carre(c: &Cercle, car: &Carre) -> f64
```
Distance entre un cercle et un carré.

#### `dist_cercle_triangle`
```rust
pub fn dist_cercle_triangle(c: &Cercle, t: &Triangle) -> f64
```
Distance entre un cercle et un triangle.

#### `dist_cercle_polygone`
```rust
pub fn dist_cercle_polygone(c: &Cercle, p: &Polygone) -> f64
```
Distance entre un cercle et un polygone.

---

### Distances Carré ↔ Formes

#### `dist_carre_carre`
```rust
pub fn dist_carre_carre(c1: &Carre, c2: &Carre) -> f64
```
Distance entre deux carrés.

#### `dist_carre_rectangle`
```rust
pub fn dist_carre_rectangle(c: &Carre, r: &Rectangle) -> f64
```
Distance entre un carré et un rectangle.

#### `dist_carre_cercle`
```rust
pub fn dist_carre_cercle(c: &Carre, cercle: &Cercle) -> f64
```
Distance entre un carré et un cercle.

#### `dist_carre_triangle`
```rust
pub fn dist_carre_triangle(c: &Carre, t: &Triangle) -> f64
```
Distance entre un carré et un triangle.

#### `dist_carre_polygone`
```rust
pub fn dist_carre_polygone(carre: &Carre, poly: &Polygone) -> f64
```
Distance entre un carré et un polygone.

---

### Distances Rectangle ↔ Formes

#### `dist_rect_rect`
```rust
pub fn dist_rect_rect(r1: &Rectangle, r2: &Rectangle) -> f64
```
Distance entre deux rectangles.

#### `dist_rectangle_cercle`
```rust
pub fn dist_rectangle_cercle(r: &Rectangle, c: &Cercle) -> f64
```
Distance entre un rectangle et un cercle.

#### `dist_rectangle_polygone`
```rust
pub fn dist_rectangle_polygone(rect: &Rectangle, poly: &Polygone) -> f64
```
Distance entre un rectangle et un polygone.

---

### Distances Triangle ↔ Formes

#### `dist_triangle_triangle`
```rust
pub fn dist_triangle_triangle(t1: &Triangle, t2: &Triangle) -> f64
```
Distance entre deux triangles (via AABB).

#### `dist_triangle_cercle`
```rust
pub fn dist_triangle_cercle(t: &Triangle, c: &Cercle) -> f64
```
Distance entre un triangle et un cercle (via AABB).

#### `dist_triangle_rectangle`
```rust
pub fn dist_triangle_rectangle(t: &Triangle, r: &Rectangle) -> f64
```
Distance entre un triangle et un rectangle (via AABB).

#### `dist_triangle_carre`
```rust
pub fn dist_triangle_carre(t: &Triangle, c: &Carre) -> f64
```
Distance entre un triangle et un carré.

#### `dist_triangle_polygone`
```rust
pub fn dist_triangle_polygone(tri: &Triangle, poly: &Polygone) -> f64
```
Distance entre un triangle et un polygone.

---

### Distances Losange ↔ Formes

#### `dist_losange_losange`
```rust
pub fn dist_losange_losange(l1: &Losange, l2: &Losange) -> f64
```
Distance entre deux losanges.

#### `dist_losange_cercle`
```rust
pub fn dist_losange_cercle(l: &Losange, c: &Cercle) -> f64
```
Distance entre un losange et un cercle.

#### `dist_losange_rectangle`
```rust
pub fn dist_losange_rectangle(l: &Losange, r: &Rectangle) -> f64
```
Distance entre un losange et un rectangle.

#### `dist_losange_carre`
```rust
pub fn dist_losange_carre(l: &Losange, c: &Carre) -> f64
```
Distance entre un losange et un carré.

#### `dist_losange_triangle`
```rust
pub fn dist_losange_triangle(l: &Losange, t: &Triangle) -> f64
```
Distance entre un losange et un triangle.

#### `dist_losange_polygone`
```rust
pub fn dist_losange_polygone(l: &Losange, p: &Polygone) -> f64
```
Distance entre un losange et un polygone.

---

### Distances Polygone ↔ Formes

#### `dist_poly_poly`
```rust
pub fn dist_poly_poly(p1: &Polygone, p2: &Polygone) -> f64
```
Distance entre deux polygones (0 en cas de chevauchement).

---

## Fonctions utilitaires

### Géométrie computationnelle

#### `orientation`
```rust
pub fn orientation(a: &Point, b: &Point, c: &Point) -> i32
```
Détermine l'orientation de trois points.

**Retour:**
- `0`: Points colinéaires
- `1`: Orientation horaire
- `2`: Orientation anti-horaire

#### `on_segment`
```rust
pub fn on_segment(a: &Point, b: &Point, c: &Point) -> bool
```
Vérifie si le point C appartient au segment AB.

**Retour:** `true` si C est sur le segment AB

---

### Boîtes englobantes (AABB)

#### `AABB::new`
```rust
fn new(p1: &Point, p2: &Point) -> Self
```
Crée une AABB (Axis-Aligned Bounding Box) à partir de deux points.

#### `contains`
```rust
pub fn contains(&self, p: &Point) -> bool
```
Vérifie si un point est contenu dans la AABB.

---

### Fonctions de conversion

#### `carre_to_rect`
```rust
pub fn carre_to_rect(c: &Carre) -> Rectangle
```
Convertit un carré en rectangle.

#### `losange_to_rect`
```rust
fn losange_to_rect(l: &Losange) -> Rectangle
```
Convertit un losange en rectangle englobant (AABB).

#### `points_polygone`
```rust
fn points_polygone(poly: &Polygone) -> Vec<Point>
```
Convertit un polygone en liste de points.

#### `tri_aabb`
```rust
fn tri_aabb(t: &Triangle) -> Rectangle
```
Calcule la boîte englobante (AABB) d'un triangle.

---

### Test d'appartenance

#### `point_in_poly`
```rust
fn point_in_poly(px: f64, py: f64, pts: &[(f64, f64)]) -> bool
```
Teste si un point est à l'intérieur d'un polygone (algorithme ray casting).

**Paramètres:**
- `px, py`: Coordonnées du point
- `pts`: Liste des sommets du polygone

**Retour:** `true` si le point est à l'intérieur

---

## Notes techniques

- Toutes les fonctions de distance retournent `0.0` lorsque les formes se chevauchent ou qu'un point est à l'intérieur
- Les calculs de distance pour les triangles utilisent des AABB pour l'optimisation
- Les losanges sont convertis en rectangles englobants pour les calculs de distance
- Précision numérique : `1e-9` pour les tests de colinéarité et `1e-12` pour éviter les divisions par zéro
# Documentation : Moteur de Collision & Intersection

## 1. Vue d'ensemble

Le module **intersection** est le cœur du système physique de **GeoCalculs**.  
Il permet de détecter si deux formes géométriques se touchent ou se chevauchent.

### Points forts :

- **Universel** : Fonctionne entre n'importe quelles formes  
  (ex : Triangle vs Cercle, Polygone vs Rectangle…)
- **Robuste** : Gère les polygones convexes  
  (Carré, Hexagone) et concaves  
  (Forme en U, Étoile).
- **Performant** : Utilise des algorithmes d’élimination rapide (SAT)  
  et des techniques de décomposition géométrique (triangulation).

---

## 2. Algorithmes Utilisés

### A. Théorème des Axes Séparateurs (SAT)

Le SAT (*Separating Axis Theorem*) est utilisé pour toutes les formes **convexes**.

**Principe :**
- On projette chaque forme sur des axes perpendiculaires à leurs côtés.
- On analyse si leurs projections se chevauchent.

**Règle :**
> S'il existe un axe où les projections ne se recouvrent pas,  
> alors les objets **ne sont pas en collision**.  
> Sinon, ils **sont en collision**.

---

### B. Triangulation "Ear Clipping" (Pour les Concaves)

Le SAT ne fonctionne pas directement sur les polygones **concaves** (formes en L, U, Étoile…).

**Solution :**
1. À la réception d’un polygone, l’algorithme **Ear Clipping** découpe la forme en triangles.
2. Chaque triangle est ensuite testé individuellement via le SAT.
3. Si au moins un triangle touche l’autre objet → **Collision détectée**.

---

## 3. Architecture Technique (`src/intersection.rs`)

### Unification des Données

Le moteur ne manipule pas directement les classes Python (`Rectangle`, `Triangle`, etc.).  
Il les convertit dans une structure interne unifiée :

```rust


### Flux d'exécution

1.  **Entrée** : `intersecte(forme_a, forme_b)` est appelée depuis Python.
2.  **Extraction** : `extraire_forme()` convertit les objets Python :
    * *Rectangle / Carré / Triangle* → Liste de points (1 polygone convexe).
    * *Polygone concave* → Découpage en N triangles via `trianguler()`.
3.  **Comparaison** : Une double boucle teste chaque sous-forme de A contre chaque sous-forme de B.
4.  **Calcul** :
    * Poly vs Poly → `sat_poly_poly()`
    * Poly vs Cercle → `sat_poly_cercle()`

---

## 4. Guide d'utilisation (Python)

### Fonction principale

```python
def intersecte(forme_a: object, forme_b: object, mode: str = "bool") -> bool

### Exemple 1 : Cas Simple (Convexe)

```python
import geocalculs as g

rect = g.Rectangle(0, 0, 4, 2)
tri  = g.Triangle(2, 1, 2, 4, 4, 4)

# Le triangle pique dans le rectangle
if g.intersecte(rect, tri):
    print("Collision détectée !")


###Exemple 2 : Cas Complexe (Concave - Forme en U)
```python
import geocalculs as g

# Création d'un U (Concave)
points_u = [(0,0), (4,0), (4,4), (3,4), (3,1), (1,1), (1,4), (0,4)]
forme_u = g.Polygone(points_u)

# Objet placé dans le "creux" du U (ne touche pas les murs)
objet_dans_le_vide = g.Carre(1.5, 2, 0.5)

# Grâce à la triangulation, ceci renvoie False
collision = g.intersecte(forme_u, objet_dans_le_vide)
print(f"Collision : {collision}")  # False

## 5. Stratégie de Tests (`tests/test_intersection.py`)

Les tests garantissent la fiabilité du moteur. Voici les scénarios critiques couverts :

| Test | Description | Objectif |
| :--- | :--- | :--- |
| **Le "U" (Concave)** | Un objet dans le creux du U | Valider que la triangulation ne « bouche » pas les trous |
| **L'Étoile** | Collision avec une forme étoilée complexe | Vérifier la robustesse de l’Ear Clipping |
| **Rectangle vs Triangle** | Triangle traversant un rectangle | Tester le SAT sur des axes inclinés |
| **Polygone vs Cercle** | Cercle touchant un bord ou un sommet | Tester le mode hybride (courbe vs angulaire) |
| **Inclusion** | Objet complètement contenu dans un autre | Vérifier que l’inclusion compte comme collision |




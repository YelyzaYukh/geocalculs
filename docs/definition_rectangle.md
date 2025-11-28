
#  Documentation — Fonction **définir un rectangle**

### Projet GeoCalculs

##  Objectif du document
Ce fichier décrit la fonction permettant de **définir et valider un rectangle** développée en Rust et exposée à Python via **PyO3**.

Chaque fonction documentée inclut :

- Objectif
- Règles mathématiques
- Implémentation Rust
- Exemple Python
- Tests unitaires

---

##  Auteur : **Youssef Jemaa**
### Fonction documentée : `definir_rectangle`

---
# Documentation : Structure `Rectangle`

La structure `Rectangle` représente un rectangle défini par un coin d’origine et deux dimensions strictement positives.  
Elle est exposée à Python via PyO3 dans le cadre du projet *GeoCalculs*.  
Elle permet :

- la création d’un rectangle
- le calcul du périmètre
- le calcul de la surface
- la construction d’un rectangle à partir de deux coins
- la construction d’un rectangle à partir de son centre

------------------------------------------------------------------------

# Définition

Un rectangle est défini par les valeurs :

- `x` — coordonnée X du coin d’origine
- `y` — coordonnée Y du coin d’origine
- `largeur` — largeur du rectangle (strictement positive)
- `hauteur` — hauteur du rectangle (strictement positive)

Toute tentative de création avec une dimension nulle ou négative renvoie une erreur :

ValueError("Les dimensions doivent être strictement positives.")

------------------------------------------------------------------------

# Constructeurs disponibles

## 1. Constructeur standard
Création classique d’un rectangle à partir des valeurs `(x, y, largeur, hauteur)`.

## 2. Constructeur par coins opposés
Permet de construire un rectangle à partir de deux points `(x1, y1)` et `(x2, y2)` :
- les coordonnées minimales donnent le coin d’origine
- la largeur/hauteur sont obtenues par valeurs absolues

Cas invalides (même point → largeur ou hauteur nulle) renvoient une erreur.

## 3. Constructeur par centre
Création d’un rectangle à partir de son centre `(cx, cy)` et de ses dimensions :
- le coin d’origine est calculé en retirant la moitié des dimensions
- les dimensions doivent être strictement positives

------------------------------------------------------------------------

# Méthodes disponibles

## 1. Calcul du périmètre

Le périmètre d’un rectangle est donné par :

P = 2 × (largeur + hauteur)



La méthode retourne cette valeur directement.

------------------------------------------------------------------------

## 2. Calcul de la surface

La surface d’un rectangle est définie par :

S = largeur × hauteur



La méthode fournit cette valeur sous forme de `f64`.

------------------------------------------------------------------------

# Fonction associée : `definir_rectangle`

Une fonction utilitaire permet depuis Python d’obtenir une description textuelle du rectangle construit :

"Rectangle en (x, y) : largeur × hauteur"

python
Copier le code

Elle effectue la même validation que le constructeur standard.

------------------------------------------------------------------------

# Exemple d’utilisation Python

```python
import geocalculs as g

r = g.Rectangle(0, 0, 4, 2)

print(r.perimetre())   # 12
print(r.surface())     # 8
print(r.x, r.y)        # 0 0

desc = g.definir_rectangle(1, 1, 3, 2)
print(desc)            # "Rectangle en (1, 1) : 3x2"
Tests réalisés
Les tests unitaires valident :

la création d’un rectangle valide

les erreurs sur les dimensions nulles ou négatives

la cohérence des valeurs retournées

les différents constructeurs (standard, from_corners, from_center)

le bon fonctionnement de perimetre() et surface()

le comportement de la fonction definir_rectangle

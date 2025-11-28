
## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

---

## Auteur : **Yelyzaveta YUKHNOVA**
### Class: Carre
### Méthodes : `perimetre` et `surface`

---

# Documentation : Structure `Carre`

La structure `Carre` représente un carré défini par son coin supérieur gauche et la longueur de son côté.  
Elle est exposée à Python via PyO3 dans le cadre du projet *GeoCalculs*.  
Elle fournit deux méthodes principales :

- périmètre
- surface

Ces fonctions permettent d'effectuer des calculs géométriques simples et fiables.

------------------------------------------------------------------------

# Définition

Un carré est défini par trois valeurs :

- `x` — coordonnée X du coin supérieur gauche
- `y` — coordonnée Y du coin supérieur gauche
- `cote` — longueur du côté (doit être **positive**)

Si `cote < 0`, la création de l’objet renvoie l’erreur :

ValueError("Le côté doit être positif.")

markdown
Copier le code

------------------------------------------------------------------------

# Méthodes disponibles

## 1. Périmètre

Le périmètre d’un carré est donné par :

P = 4 × cote

yaml
Copier le code

La méthode renvoie donc :

4.0 * cote

markdown
Copier le code

------------------------------------------------------------------------

## 2. Surface

La surface d’un carré est définie par :

S = cote²

yaml
Copier le code

La méthode renvoie la valeur :

cote.powi(2)

python
Copier le code

------------------------------------------------------------------------

# Exemple d’utilisation Python

```python
import geocalculs as g

c = g.Carre(0.0, 0.0, 5)

print(c.perimetre())  # 20.0
print(c.surface())    # 25.0
print(c.x, c.y)       # 0.0 0.0
```
Tests réalisés
Les tests unitaires vérifient :

le calcul du périmètre pour différents côtés

le calcul de la surface

le comportement avec des entiers et des flottants

la levée d’erreur pour les côtés négatifs

la bonne lecture des attributs x, y, cote

la justesse des méthodes perimetre() et surface()

Ces tests garantissent la stabilité et la précision de la structure.

Remarques
Les valeurs retournées sont de type f64.

Les coordonnées du coin supérieur gauche ne sont pas limitées (elles peuvent être négatives).

Le carré est utilisable directement depuis Python via geocalculs.Carre.

Cette structure s’intègre dans les formes géométriques du projet GeoCalculs.
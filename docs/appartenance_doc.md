# Documentation : Fonction `appartient`

Cette fonction détermine si un point de coordonnées `(px, py)`
appartient à une forme géométrique donnée.\
Elle est exposée à Python via PyO3 et gère les formes suivantes :

-   Carré\
-   Rectangle\
-   Cercle\
-   Losange\
-   Triangle\
-   Polygone

La fonction renvoie **True** si le point est à l'intérieur ou sur le
bord de la forme.\
Le paramètre `_mode` est présent pour compatibilité mais n'est pas
utilisé :\
le comportement combine automatiquement le mode strict et le mode bord.

------------------------------------------------------------------------

# Signature

    pub fn appartient(px: f64, py: f64, forme: &Bound<'_, PyAny>, _mode: &str) -> PyResult<bool>

------------------------------------------------------------------------

# Détail du comportement selon la forme

## 1. Carré

Défini par : - `x`, `y` : coordonnées du coin supérieur gauche\
- `cote` : longueur du côté

Le point appartient au carré si :

    x <= px <= x + cote
    y <= py <= y + cote

Un test strict est aussi effectué, mais le résultat final combine strict
et bord.

------------------------------------------------------------------------

## 2. Rectangle

Défini par : - `x`, `y` : coordonnées du coin supérieur gauche\
- `largeur`, `hauteur`

Le point appartient au rectangle si :

    x <= px <= x + largeur
    y <= py <= y + hauteur

------------------------------------------------------------------------

## 3. Cercle

Défini par : - `centre_x`, `centre_y` - `rayon`

Le point appartient au cercle si :

    (px - centre_x)^2 + (py - centre_y)^2 <= rayon^2

------------------------------------------------------------------------

## 4. Losange

Défini par : - centre `(x, y)` - largeur (grande diagonale) - hauteur
(petite diagonale)

Test effectué :

    |px - x| / (largeur/2) + |py - y| / (hauteur/2) <= 1

Ce test inclut naturellement l'intérieur et le bord.

------------------------------------------------------------------------

## 5. Triangle

Défini par trois points `(A, B, C)`.

Méthode utilisée :\
Somme des aires des sous-triangles égale à l'aire totale du triangle,
avec une tolérance numérique.

    area(ABC) == area(PAB) + area(PBC) + area(PCA)

------------------------------------------------------------------------

## 6. Polygone

Utilise deux tests :

1.  Test du bord :\
    Le point est vérifié sur chaque segment du polygone.

2.  Algorithme du rayon (ray casting) :

```{=html}
<!-- -->
```
    Si le rayon horizontal croise un nombre impair d’arêtes → point intérieur

Les points sont récupérés directement via :

    poly.points.clone()

------------------------------------------------------------------------

# Erreurs possibles

Si la forme envoyée n'est pas reconnue, la fonction renvoie :

    TypeError("Forme inconnue")

------------------------------------------------------------------------

# Exemple d'utilisation Python

``` python
import geocalculs as g

rect = g.Rectangle(0, 0, 4, 2)
print(g.appartient(1, 1, rect, "bord"))
# True
```

------------------------------------------------------------------------

# Remarques

-   La tolérance numérique utilisée est `1e-9`.
-   Le paramètre `mode` est ignoré : le test combine automatiquement
    bord + intérieur.
-   Le code utilise `extract::<Type>()` pour identifier la nature de la
    forme.

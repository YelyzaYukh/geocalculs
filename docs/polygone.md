# Module Polygone — Documentation Technique

## 1. Vue d'ensemble

Le module **Polygone** permet de définir et d'analyser des formes géométriques complexes définies par une série de points \((x, y)\).

Contrairement aux formes standards (cercle, rectangle) implémentées via des fonctions simples, le **Polygone** est implémenté sous forme de **Classe (Class)** afin de permettre une gestion dynamique des sommets.

**Fichiers concernés :**
- **Rust (Logique)** : `src/polygon.rs`
- **Python (Interface)** : `geocalculs.Polygone`

---

## 2. Formules Mathématiques

### A. Périmètre

Le périmètre est calculé en additionnant la distance euclidienne entre chaque point consécutif.  
Le dernier point est relié au premier pour fermer la forme.

\[
P = \sum_{i=0}^{n-1} \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2}
\]

> **Note :** L’indice \(n\) correspond au retour au point `0`.

---

### B. Surface (Aire)

Pour calculer l’aire d’un polygone irrégulier (non croisé), la **Formule du Lacet** (Shoelace Formula) est utilisée.

Cette méthode permet de calculer l’aire uniquement à partir des coordonnées, sans décomposition en triangles.

\[
A = \frac{1}{2} \left| \sum_{i=0}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|
\]

---

## 3. Guide d'utilisation (Python)

L'utilisateur doit instancier la classe `Polygone` en lui passant une liste de tuples représentant les coordonnées `(x, y)`.

---

### Exemple 1 : Un Triangle simple

```python
import geocalculs

# Définition des sommets (Triangle 3-4-5)
points_triangle = [
    (0.0, 0.0),
    (4.0, 0.0),
    (0.0, 3.0)
]

# Création de l'objet
poly = geocalculs.Polygone(points_triangle)

# Calculs
print(f"Périmètre : {poly.perimetre()}")  # Résultat : 12.0
print(f"Surface   : {poly.surface()}")    # Résultat : 6.0

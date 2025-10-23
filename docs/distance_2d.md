# Documentation des fonctions de calcul — Projet GeoCalculs

## Objectif du document
Ce fichier regroupe la documentation de toutes les **fonctions de calcul géométriques** développées dans le cadre du projet *GeoCalculs*.

Chaque membre de l’équipe y décrit sa ou ses fonctions :
- Objectif de la fonction  
- Formule mathématique utilisée  
- Code Rust correspondant  
- Exemple d’utilisation en Python  
- Test unitaire associé  

---

## Auteur : ARIOUI Mohamed Acharf Ouassim  
### Fonction : `distance_2d`

### 🎯 Objectif
Implémenter une fonction permettant de **calculer la distance entre deux points** dans un plan 2D, à partir de leurs coordonnées `(x1, y1)` et `(x2, y2)`.

---

### 🧮 Formule mathématique

La distance entre deux points \( A(x_1, y_1) \) et \( B(x_2, y_2) \) est donnée par la **formule de Pythagore** :

\[
D = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Où :
- \( x_1, y_1 \) : coordonnées du premier point  
- \( x_2, y_2 \) : coordonnées du second point  
- \( D \) : distance entre les deux points  

---

### 🦀 Implémentation (Rust)

**Fichier : `src/distance.rs`**
```rust
use pyo3::prelude::*;

/// Fonction qui calcule la distance entre deux points 2D.
/// 
/// # Arguments
/// * `x1` - Coordonnée X du premier point
/// * `y1` - Coordonnée Y du premier point
/// * `x2` - Coordonnée X du second point
/// * `y2` - Coordonnée Y du second point
///
/// # Retour
/// * `f64` - La distance euclidienne entre les deux points
#[pyfunction]
pub fn distance_2d(x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt()
}

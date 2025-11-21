#  Documentation du module `validation.rs`

##  Objectif du module

Le module `validation.rs` du projet **GeoCalculs** contient des fonctions de **validation des entrées numériques** utilisées dans les calculs géométriques.  
Il permet d’assurer la **cohérence** et la **sécurité** des données avant leur traitement dans les fonctions principales (distance, périmètre, surface, etc.).

Ces fonctions sont exposées à **Python** via la bibliothèque **PyO3**, ce qui les rend directement accessibles depuis un environnement Python après compilation du module Rust.

---

##  Détails des fonctions

###  Fonction `valider_valeurs(values: Vec<f64>) -> PyResult<bool>`

####  Objectif
Vérifie qu’une liste de valeurs numériques ne contient **aucune valeur invalide**, c’est-à-dire :
- ni **NaN** (Not a Number),
- ni **valeurs négatives**.

####  Prototype (Rust)
```rust
#[pyfunction]
pub fn valider_valeurs(values: Vec<f64>) -> PyResult<bool>
```

####  Paramètres
| Nom | Type | Description |
|------|------|-------------|
| `values` | `Vec<f64>` | Vecteur de nombres flottants à valider |

####  Valeur de retour
| Type | Description |
|------|-------------|
| `PyResult<bool>` | Retourne `Ok(true)` si toutes les valeurs sont valides, sinon lève une exception `ValueError` |

####  Exceptions levées
- `ValueError("Valeur NaN détectée")` si une des valeurs est `NaN`
- `ValueError("Valeur négative non autorisée : X")` si une valeur est négative

####  Exemple d’utilisation (Python)
```python
import geocalculs as g

# Cas valide
g.valider_valeurs([3.0, 4.5, 5.0])  #  True

# Cas invalide : valeur négative
g.valider_valeurs([-1.0, 2.0, 3.0])  #  ValueError: Valeur négative non autorisée : -1

# Cas invalide : valeur NaN
import math
g.valider_valeurs([math.nan, 2.0])  #  ValueError: Valeur NaN détectée
```

####  Exemple d’utilisation (Rust)
```rust
let result = valider_valeurs(vec![3.0, 4.0, 5.0]).unwrap();
assert_eq!(result, true);
```

---

###  Fonction `valider_triangle(a: f64, b: f64, c: f64) -> PyResult<bool>`

####  Objectif
Vérifie qu’un triangle défini par trois côtés est **géométriquement valide**.  
Cette validation repose sur deux critères :
1. Les longueurs des côtés doivent être **strictement positives** ;
2. Elles doivent respecter **l’inégalité triangulaire** :
   \[
   a + b > c, \quad a + c > b, \quad b + c > a
   \]

####  Prototype (Rust)
```rust
#[pyfunction]
pub fn valider_triangle(a: f64, b: f64, c: f64) -> PyResult<bool>
```

####  Paramètres
| Nom | Type | Description |
|------|------|-------------|
| `a` | `f64` | Longueur du premier côté |
| `b` | `f64` | Longueur du deuxième côté |
| `c` | `f64` | Longueur du troisième côté |

####  Valeur de retour
| Type | Description |
|------|-------------|
| `PyResult<bool>` | Retourne `Ok(true)` si le triangle est valide, sinon lève une exception `ValueError` |

####  Exceptions levées
- `ValueError("Les longueurs doivent être positives")` si l’un des côtés ≤ 0
- `ValueError("Les longueurs ne respectent pas l'inégalité triangulaire")` si le triangle est impossible

####  Exemple d’utilisation (Python)
```python
import geocalculs as g

# Cas valide
g.valider_triangle(3, 4, 5)  #  True

# Cas invalide : ne respecte pas l'inégalité triangulaire
g.valider_triangle(1, 2, 3)  #  ValueError: Les longueurs ne respectent pas l'inégalité triangulaire

# Cas invalide : longueur négative
g.valider_triangle(-1, 2, 3)  #  ValueError: Les longueurs doivent être positives
```

####  Exemple d’utilisation (Rust)
```rust
let ok = valider_triangle(3.0, 4.0, 5.0).unwrap();
assert_eq!(ok, true);
```

---

##  Tests unitaires associés

Les tests sont définis dans `tests/test_validation.py` et vérifient :
- les cas valides (`assert True`)
- les exceptions (`pytest.raises(ValueError)`)

Exemple :
```python
def test_valider_triangle_invalide():
    import pytest
    with pytest.raises(ValueError):
        g.valider_triangle(1, 2, 3)
```

---

##  Fichier concerné
 `src/validation.rs`

---

##  Auteur(s)
- **ARIOUI Mohamed Achraf Ouassim** — Validation des triangles  — Validation des valeurs numériques  
 
Projet réalisé dans le cadre du module **Processus du Développement Logiciel — M1 ILSEN, Université d’Avignon (CERI)**.

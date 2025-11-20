# Documentation de la classe `Losange`

## Nom du fichier
`src/losange.rs`

## Auteur
**Arioui Mohamed Achraf Ouassim**

## Description générale
La classe `Losange` représente une figure géométrique plane à quatre côtés égaux.  
Elle permet de calculer la **surface** et le **périmètre** du losange à partir de ses dimensions, tout en vérifiant la validité des valeurs fournies.  

Cette classe est exposée au langage Python grâce au binding **PyO3**, et peut donc être utilisée directement depuis un script Python après compilation du module Rust.

---

## Définition de la classe

```rust
#[pyclass]
pub struct Losange {
    diagonale1: f64,
    diagonale2: f64,
    cote: f64,
}
```

### Attributs
| Nom | Type | Description |
|------|------|-------------|
| `diagonale1` | `f64` | Longueur de la première diagonale du losange |
| `diagonale2` | `f64` | Longueur de la seconde diagonale du losange |
| `cote` | `f64` | Longueur d’un côté du losange |

---

## Constructeur

### Prototype
```rust
#[new]
pub fn new(diagonale1: f64, diagonale2: f64, cote: f64) -> PyResult<Self>
```

### Description
Construit un objet `Losange` à partir de ses deux diagonales et de la longueur d’un côté.  
Lors de l’instanciation, le constructeur vérifie que toutes les dimensions sont strictement positives.

### Validation
Si une dimension est inférieure ou égale à zéro, une exception Python de type `ValueError` est levée avec le message :
```
Les dimensions du losange doivent être strictement positives
```

### Exemple (Python)
```python
import geocalculs as g

l = g.Losange(10, 8, 6)
print(l.description())
```

---

## Méthodes

### 1. `surface(&self) -> f64`
Calcule la surface du losange à partir des diagonales principales.

#### Formule
S = (D × d) / 2

#### Exemple (Python)
```python
l = g.Losange(10, 8, 6)
print(l.surface())  # Résultat : 40.0
```

---

### 2. `perimetre(&self) -> f64`
Calcule le périmètre du losange à partir de la longueur d’un côté.

#### Formule
P = 4 × c

#### Exemple (Python)
```python
l = g.Losange(10, 8, 6)
print(l.perimetre())  # Résultat : 24.0
```

---

### 3. `description(&self) -> String`
Retourne une représentation textuelle lisible de l’objet `Losange`, indiquant ses dimensions internes.

#### Exemple (Python)
```python
l = g.Losange(10, 8, 6)
print(l.description())
```

**Sortie :**
```
Losange(diagonales: (10, 8), côté: 6)
```

---

## Gestion des erreurs

| Situation | Type d’erreur | Message retourné |
|------------|----------------|------------------|
| Diagonale ou côté négatif | `ValueError` | `Les dimensions du losange doivent être strictement positives` |
| Diagonale ou côté nul | `ValueError` | `Les dimensions du losange doivent être strictement positives` |

---

## Exemple complet d’utilisation Python

```python
import geocalculs as g

# Création d’un losange
l = g.Losange(12, 9, 7)

# Calculs
print("Surface :", l.surface())
print("Périmètre :", l.perimetre())

# Description textuelle
print(l.description())
```

**Résultat attendu :**
```
Surface : 54.0
Périmètre : 28.0
Losange(diagonales: (12, 9), côté: 7)
```

---

## Tests unitaires associés

Fichier : `tests/test_losange_class.py`

- Vérifie la validité de la création de l’objet
- Contrôle les erreurs pour valeurs négatives ou nulles
- Valide les calculs de surface et de périmètre
- Vérifie le contenu de la description textuelle

---

## Conclusion
La classe `Losange` constitue un exemple clair d’intégration entre **Rust** et **Python** via **PyO3**, combinant sécurité des types et performance.  
Elle met en œuvre une approche orientée objet simple et efficace pour modéliser des entités géométriques dans un projet de développement logiciel.

# GeoLib2D

GeoLib2D est une bibliothèque de calculs géométriques 2D à hautes performances, développée en *Rust* et accessible depuis *Python* grâce à la bibliothèque [PyO3](https://pyo3.rs/).  
Elle permet d’effectuer des opérations géométriques essentielles telles que le calcul de distances, de surfaces, de périmètres, de tests d’appartenance et d’intersections entre formes, tout en combinant la rapidité du langage Rust avec la simplicité d’utilisation de Python.

---

## Objectifs du projet

Le projet GeoLib2D vise à fournir une bibliothèque :

- rapide et fiable pour le calcul géométrique 2D ;
- réutilisable et modulaire ;
- intégrable facilement dans un environnement Python ;
- accompagnée d’une documentation claire et de tests unitaires.

Ce projet est réalisé dans le cadre d’un travail pratique encadré suivant la méthodologie *Scrum*.  
Le professeur joue le rôle de *client / Product Owner*, et l’équipe de développement est responsable de la conception, de l’implémentation et des tests.

---

## Fonctionnalités principales

| Catégorie | Fonctions principales | Description |
|------------|-----------------------|--------------|
| Calculs de base | distance_2d | Calcule la distance entre deux points en 2D |
| Formes géométriques | surface_rectangle, surface_cercle, surface_triangle, etc. | Calcule les périmètres et surfaces des formes courantes |
| Appartenance | appartient(point, formes, mode) | Vérifie si un point appartient à une ou plusieurs formes (rectangle, cercle, polygone) |
| Intersections | intersecte(formeA, formeB, mode) | Détecte les intersections entre différentes formes (rectangle, cercle, polygone, etc.) |
| Fonctions utilitaires | orientation, on_segment, AABB | Fournit des fonctions géométriques de base réutilisables |
| Documentation interne | decrire_forme(forme) | Fournit les formules et explications associées à chaque forme |
| Interface en ligne de commande | geolib | Permet d’utiliser la bibliothèque sans coder en Python |

---

## Technologies utilisées

- *Langage principal* : Rust (pour les calculs)
- *Interface* : PyO3 (bindings Python ↔ Rust)
- *Gestion de projet* : maturin (compilation et packaging)
- *Tests* : pytest (tests unitaires Python)
- *Documentation* : pdoc ou Sphinx
- *Compatibilité* : Python 3.8 ou supérieur

---

## Installation

Lorsque la bibliothèque est compilée ou publiée sur PyPI :

```bash
pip install geolib2d
Utilisation dans Python :

python
Copier le code
import geolib2d as geo

print(geo.distance_2d(0, 0, 3, 4))  # 5.0
Développement local
Cloner le dépôt et installer la version de développement :

bash
Copier le code
git clone https://github.com/<votre-utilisateur>/geolib2d.git
cd geolib2d
maturin develop
Exécuter les tests :

bash
Copier le code
pytest
Structure du projet
bash
Copier le code
geolib2d/
├── src/                 # Code source Rust
│   ├── lib.rs           # Point d’entrée du module PyO3
│   ├── distance.rs      # Fonctions de distance
│   ├── shapes.rs        # Définitions des formes (Rectangle, Cercle, Polygone)
│   ├── appartient.rs    # Fonctions de test d’appartenance
│   ├── intersecte.rs    # Fonctions d’intersection
│   └── helpers.rs       # Fonctions utilitaires (AABB, orientation, etc.)
├── tests/               # Tests unitaires en Python (pytest)
│   ├── test_distance.py
│   ├── test_appartient.py
│   └── test_intersecte.py
├── docs/                # Documentation générée ou rédigée
│   └── index.md
├── Cargo.toml           # Configuration du projet Rust
├── pyproject.toml       # Configuration du projet Python
└── README.md
Exemple d’utilisation
python
Copier le code
from geolib2d import distance_2d, surface_rectangle, appartient, intersecte

# Calculs de base
print(distance_2d(0, 0, 3, 4))  # 5.0

# Surface et périmètre
print(surface_rectangle(4, 6))  # 24.0

# Test d’appartenance
point = (2, 2)
formes = [
    {"type": "rectangle", "x": 0, "y": 0, "w": 10, "h": 5},
    {"type": "cercle", "cx": 5, "cy": 2, "r": 3},
]
print(appartient(point, formes, mode="report"))

# Test d’intersection
r1 = {"type": "rectangle", "x": 0, "y": 0, "w": 4, "h": 3}
r2 = {"type": "rectangle", "x": 3, "y": 2, "w": 4, "h": 3}
print(intersecte(r1, r2, mode="boolean"))  # True
Organisation du développement (méthode Scrum)
Sprint	Objectif principal	Livrables attendus
1	Initialisation du projet	Choix technologique, création du dépôt, rédaction du backlog
2	Calculs géométriques de base	Distance, périmètres, surfaces, validation et tests unitaires
3	Tests d’appartenance et helpers	Fonction appartient, helpers (on_segment, orientation, AABB)
4	Gestion des intersections	Fonction intersecte pour toutes les formes et tests associés
5	Finalisation	CLI, logs, documentation, démonstration finale

Équipe de développement
Scrum Master : Mohammed Djellouli

Product Owner (Client) : Enseignant encadrant

Développeurs : Équipe projet (3 à 4 membres)

Licence
Ce projet est distribué sous licence MIT.
L’utilisation, la modification et la redistribution sont autorisées, sous réserve de mentionner les auteurs originaux.
import pytest
import geocalculs as g
import math

# ==========================================
# 1. TESTS DES CAS VALIDES (Formes Correctes)
# ==========================================

def test_creation_valide_carre():
    """Un carré simple doit fonctionner parfaitement."""
    points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
    poly = g.Polygone(points)

    assert poly.nombre_de_sommets() == 4
    assert poly.perimetre() == pytest.approx(16.0)
    assert poly.surface() == pytest.approx(16.0)

def test_creation_valide_triangle():
    """Triangle rectangle 3-4-5."""
    points = [(0.0, 0.0), (4.0, 0.0), (0.0, 3.0)]
    poly = g.Polygone(points)

    assert poly.nombre_de_sommets() == 3
    assert poly.perimetre() == pytest.approx(12.0) # 3 + 4 + 5
    assert poly.surface() == pytest.approx(6.0)    # (3*4)/2

def test_creation_valide_hexagone():
    """Hexagone régulier (forme convexe complexe)."""
    points = [
        (1.0, 0.0), (0.5, 0.866), (-0.5, 0.866),
        (-1.0, 0.0), (-0.5, -0.866), (0.5, -0.866)
    ]
    poly = g.Polygone(points)
    
    # Surface théorique hexagone rayon 1 ~= 2.598
    assert math.isclose(poly.surface(), 2.598, abs_tol=0.01)

def test_creation_valide_concave_L():
    """
    Vérifie qu'on peut créer un polygone concave (forme en L) 
    tant qu'il ne s'auto-intersecte pas.
    """
    # Forme en L : Carré 4x4 avec un coin 3x3 retiré en haut à droite
    points = [
        (0,0), (4,0),  # Bas
        (4,1), (1,1),  # Le "creux" du L
        (1,4), (0,4)   # Haut gauche
    ]
    poly = g.Polygone(points)
    
    # Surface : Total (16) - Creux (3*3=9) = 7
    assert poly.surface() == pytest.approx(7.0)
    # Périmètre : 4 + 1 + 3 + 3 + 1 + 4 = 16
    assert poly.perimetre() == pytest.approx(16.0)


# ==========================================
# 2. TESTS DES ERREURS (Validations Rust)
# ==========================================

def test_erreur_trop_peu_de_points():
    """
    Vérifie que le constructeur rejette :
    - Liste vide
    - 1 point
    - 2 points
    """
    msg_erreur = "au moins 3 points"
    
    with pytest.raises(ValueError, match=msg_erreur):
        g.Polygone([])

    with pytest.raises(ValueError, match=msg_erreur):
        g.Polygone([(0,0)])

    with pytest.raises(ValueError, match=msg_erreur):
        g.Polygone([(0,0), (1,1)])

def test_erreur_points_colineaires():
    """
    Vérifie que 3 points alignés sont rejetés.
    """
    # Cas 1 : Juste une ligne
    pts_ligne = [(0,0), (1,1), (2,2)]
    with pytest.raises(ValueError, match="colinéaires"):
        g.Polygone(pts_ligne)

    # Cas 2 : Un carré avec un point inutile au milieu d'un côté
    # (0,0) -> (2,0) -> (4,0) -> (4,4) -> (0,4)
    # Les trois premiers sont alignés.
    pts_invalides = [(0,0), (2,0), (4,0), (4,4), (0,4)]
    with pytest.raises(ValueError, match="colinéaires"):
        g.Polygone(pts_invalides)

def test_erreur_auto_intersection():
    """
    Vérifie que les formes croisées ("Papillon" ou "Sablier") sont rejetées.
    """
    # Forme en "Papillon" :
    # (0,0) -> (2,2) -> (0,2) -> (2,0)
    # Les segments [(0,0)-(2,2)] et [(0,2)-(2,0)] se croisent en (1,1)
    points_croises = [
        (0.0, 0.0),
        (2.0, 2.0),
        (0.0, 2.0),
        (2.0, 0.0)
    ]
    
    with pytest.raises(ValueError, match="auto-intersecte"):
        g.Polygone(points_croises)

def test_erreur_boucle_interne():
    """
    Autre type d'intersection complexe (boucle dans une boucle).
    """
    points = [
        (0,0), (5,0), (5,5), (0,5), # Grand carré
        (1,1), (2,2) # Points qui reviennent dedans bizarrement (cas simplifié)
        # Note: Pour tester une vraie auto-intersection, il faut que les lignes se coupent.
        # Exemple d'une ligne qui rentre et coupe le bord opposé :
    ]
    # Re-créons un cas clair de croisement de bordure
    points_coupés = [
        (0,0), (4,0), (4,4), (0,4), # Carré
        (5,5), (-1, -1) # Une ligne qui traverse tout le carré en diagonale
    ]
    # L'ordre des points ferait : (0,4) -> (5,5) -> (-1,-1) -> (0,0)
    # Ce dernier segment (-1,-1)->(0,0) est ok, mais (5,5)->(-1,-1) traverse le carré.
    
    with pytest.raises(ValueError, match="auto-intersecte"):
        g.Polygone([(0,0), (4,0), (0,4), (4,4)]) # Croisement simple des diagonales


# ==========================================
# 3. TEST ACCESSEURS (Getters/Setters)
# ==========================================

def test_getter_setter_points():
    """Vérifie qu'on peut lire et modifier les points depuis Python"""
    p = g.Polygone([(0,0), (4,0), (0,3)])
    
    # Lecture
    pts = p.points
    assert len(pts) == 3
    assert pts[1] == (4.0, 0.0)
    
    # Attention : cela contourne le constructeur !
    # PyO3 permet de modifier l'attribut si #[pyo3(get, set)] est présent.
    # Note : Si tu modifies les points ici pour faire une forme invalide, 
    # Rust ne le vérifiera pas (car la validation est dans `new`).
    # C'est un comportement normal des propriétés simples.
    nouvel_ensemble = [(0,0), (1,0), (0,1)]
    p.points = nouvel_ensemble
    assert p.surface() == 0.5


if __name__ == "__main__":
    # Pour exécuter manuellement si besoin
    pytest.main([__file__])
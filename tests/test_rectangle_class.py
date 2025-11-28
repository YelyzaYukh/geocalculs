import pytest
import geocalculs as g

# --- 1. Test du constructeur classique (Standard) ---
def test_creation_standard():
    # Maintenant on doit donner x et y !
    # Rectangle en (10, 20) de taille 5x2
    r = g.Rectangle(10.0, 20.0, 5.0, 2.0)
    
    assert r.x == 10.0
    assert r.y == 20.0
    assert r.largeur == 5.0
    assert r.hauteur == 2.0
    assert r.surface() == 10.0

# --- 2. Test de la méthode "Depuis les coins" (from_corners) ---
def test_from_corners_normal():
    # On simule un clic de (0,0) vers (4,4)
    r = g.Rectangle.from_corners(0, 0, 4, 4)
    
    assert r.x == 0
    assert r.y == 0
    assert r.largeur == 4
    assert r.hauteur == 4

def test_from_corners_inversses():
    # C'est le test important !
    # On simule un clic inversé : de (10, 10) vers (6, 8)
    # Le code doit comprendre que le "début" (x,y) est le minimum (6, 8)
    r = g.Rectangle.from_corners(10, 10, 6, 8)
    
    assert r.x == 6.0        # Le plus petit X
    assert r.y == 8.0        # Le plus petit Y
    assert r.largeur == 4.0  # 10 - 6
    assert r.hauteur == 2.0  # 10 - 8

# --- 3. Test de la méthode "Depuis le centre" (from_center) ---
def test_from_center():
    # On veut un rectangle centré en (0,0) de taille 4x2
    # Mathématiquement, il doit commencer à x=-2 et y=-1
    r = g.Rectangle.from_center(0, 0, 4, 2)
    
    assert r.x == -2.0
    assert r.y == -1.0
    assert r.largeur == 4.0
    assert r.hauteur == 2.0
    
    # Vérification que le centre est bien conservé
    # Centre X = x + w/2 = -2 + 2 = 0
    assert (r.x + r.largeur / 2) == 0.0

# --- 4. Tests d'erreurs (Validation) ---
def test_dimensions_invalides():
    with pytest.raises(ValueError):
        g.Rectangle(0, 0, -5, 5) # Largeur négative
    
    with pytest.raises(ValueError):
        g.Rectangle.from_center(0, 0, 5, 0) # Hauteur nulle
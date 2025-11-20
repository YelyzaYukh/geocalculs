import pytest
import math
import geocalculs as g  # module PyO3

# --- Tests de base pour le périmètre et la surface du cercle ---
@pytest.mark.parametrize(
    "rayon,perimetre_attendu,surface_attendue",
    [
        (1, 2*math.pi, math.pi),         # cercle unité
        (0, 0.0, 0.0),                   # rayon nul
        (2.5, 2*math.pi*2.5, math.pi*2.5**2),  # décimal
        (10, 2*math.pi*10, math.pi*100),       # grand rayon
    ],
)
def test_perimetre_et_surface_cercle(rayon, perimetre_attendu, surface_attendue):
    c = g.Cercle(0.0, 0.0, rayon)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)

# --- Tests pour vérifier les types acceptés (int et float) ---
def test_types_acceptes():
    c1 = g.Cercle(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 2*math.pi*3, rel_tol=1e-12)

    c2 = g.Cercle(0.0, 0.0, 3.5)
    assert math.isclose(c2.surface(), math.pi*3.5**2, rel_tol=1e-12)

# --- Tests pour les rayons négatifs ---
def test_cercle_new_negatif():
    with pytest.raises(ValueError, match="Le rayon ne peut pas être négatif."):
        g.Cercle(0.0, 0.0, -3.0)

# --- Tests de la classe Cercle ---
def test_cercle_struct():
    c = g.Cercle(3.0, 4.0, 5.0)
    assert c.centre_x == 3.0
    assert c.centre_y == 4.0
    assert c.rayon == 5.0

def test_cercle_perimetre_method():
    c = g.Cercle(0.0, 0.0, 1.0)
    assert math.isclose(c.perimetre(), 2.0 * math.pi, rel_tol=1e-12)

def test_cercle_surface_method():
    c = g.Cercle(0.0, 0.0, 2.0)
    assert math.isclose(c.surface(), math.pi * 4.0, rel_tol=1e-12)
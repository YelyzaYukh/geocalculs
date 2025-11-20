import pytest
import math
import geocalculs as g  # module PyO3

# --- Tests de base pour le périmètre et la surface du carré ---
@pytest.mark.parametrize(
    "cote,perimetre_attendu,surface_attendue",
    [
        (1, 4, 1),          # carré unité
        (0, 0, 0),          # côté nul
        (2.5, 10, 6.25),    # côté décimal
        (10, 40, 100),      # grand carré
    ],
)
def test_perimetre_et_surface_carre(cote, perimetre_attendu, surface_attendue):
    c = g.Carre(0.0, 0.0, cote)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)

# --- Tests pour vérifier les types acceptés (int et float) ---
def test_types_acceptes():
    c1 = g.Carre(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 12, rel_tol=1e-12)
    assert math.isclose(c1.surface(), 9, rel_tol=1e-12)

    c2 = g.Carre(0.0, 0.0, 3.5)
    assert math.isclose(c2.perimetre(), 14, rel_tol=1e-12)
    assert math.isclose(c2.surface(), 12.25, rel_tol=1e-12)

# --- Tests pour les côtés négatifs ---
def test_carre_new_negatif():
    with pytest.raises(ValueError, match="Le côté doit être positif."):
        g.Carre(0.0, 0.0, -3.0)

# --- Tests de la structure Carré ---
def test_carre_struct():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0
    assert c.cote == 5.0

def test_carre_perimetre_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.perimetre(), 16.0, rel_tol=1e-12)

def test_carre_surface_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.surface(), 16.0, rel_tol=1e-12)

def test_carre_coordonnees():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0

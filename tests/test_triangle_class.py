import geocalculs as geo
import pytest
import math

# --- Tests de création valide ---
def test_triangle_valide():
    # Triangle rectangle classique (3-4-5)
    # A=(0,0), B=(3,0), C=(0,4)
    t = geo.Triangle(0, 0, 3, 0, 0, 4)

    # Vérification des attributs
    assert t.ax == 0.0
    assert t.ay == 0.0

    # Vérification des calculs
    # Périmètre = 3 + 4 + 5 = 12
    assert math.isclose(t.perimetre(), 12.0, rel_tol=1e-9)
    # Surface = (3 * 4) / 2 = 6
    assert math.isclose(t.surface(), 6.0, rel_tol=1e-9)

# --- Tests d'erreurs (Validation) ---

def test_points_identiques():
    """Vérifie qu'on ne peut pas créer un triangle avec des points confondus"""
    with pytest.raises(ValueError, match="points.*distincts"):
        # A et B sont identiques (0,0)
        geo.Triangle(0, 0, 0, 0, 5, 5)

def test_points_alignes():
    """Vérifie qu'on ne peut pas créer un triangle plat"""
    with pytest.raises(ValueError, match="alignés"):
        # Points alignés sur la diagonale (0,0) -> (1,1) -> (2,2)
        geo.Triangle(0, 0, 1, 1, 2, 2)
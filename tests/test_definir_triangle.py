import geocalculs as geo
import pytest

def test_definir_triangle_valide():
    """Triangle normal : doit être accepté."""
    result = geo.definir_triangle(0, 0, 3, 0, 2, 4)
    assert "Triangle défini" in result
    assert "A(0,0)" in result
    assert "B(3,0)" in result
    assert "C(2,4)" in result


def test_definir_triangle_points_identiques():
    """Deux points identiques -> erreur Python."""
    with pytest.raises(ValueError):
        geo.definir_triangle(0, 0, 0, 0, 2, 3)


def test_definir_triangle_points_alignes():
    """
    Trois points alignés -> erreur.
    Exemple : A(0,0), B(1,1), C(2,2) sont alignés (droite y=x)
    """
    with pytest.raises(ValueError):
        geo.definir_triangle(0, 0, 1, 1, 2, 2)


def test_definir_triangle_symetrie_valid():
    """Autre triangle valide pour être sûr."""
    result = geo.definir_triangle(-1, 0, 1, 0, 0, 2)
    assert "Triangle défini" in result


def test_definir_triangle_decimaux():
    """Tester les valeurs décimales."""
    result = geo.definir_triangle(0.5, 1.2, 2.4, 3.3, 4.2, -1.1)
    assert "Triangle défini" in result

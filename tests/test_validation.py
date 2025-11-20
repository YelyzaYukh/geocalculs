import pytest
import geocalculs as g

def test_valider_valeurs_ok():
    assert g.valider_valeurs([3, 4, 5]) is True

def test_valider_valeurs_negative():
    with pytest.raises(ValueError):
        g.valider_valeurs([-1, 2, 3])

def test_valider_valeurs_nan():
    import math
    with pytest.raises(ValueError):
        g.valider_valeurs([math.nan, 2])

def test_valider_triangle_ok():
    assert g.valider_triangle(3, 4, 5) is True

def test_valider_triangle_invalide():
    with pytest.raises(ValueError):
        g.valider_triangle(1, 2, 3)

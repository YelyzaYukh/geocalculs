import geocalculs as geo
import pytest

def test_rectangle_valide():
    result = geo.definir_rectangle(4, 2)
    assert "Rectangle défini" in result

def test_largeur_negative():
    with pytest.raises(ValueError):
        geo.definir_rectangle(-3, 2)

def test_hauteur_negative():
    with pytest.raises(ValueError):
        geo.definir_rectangle(3, -1)

def test_dimensions_nulles():
    with pytest.raises(ValueError):
        geo.definir_rectangle(0, 5)

    with pytest.raises(ValueError):
        geo.definir_rectangle(5, 0)

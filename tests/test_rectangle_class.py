import geocalculs as geo
import pytest

def test_rectangle_valide():
    # Ajout de x=0, y=0
    result = geo.definir_rectangle(0, 0, 4, 2)
    assert "Rectangle" in result

def test_largeur_negative():
    with pytest.raises(ValueError):
        # Ajout de x=0, y=0
        geo.definir_rectangle(0, 0, -3, 2)

def test_hauteur_negative():
    with pytest.raises(ValueError):
        # Ajout de x=0, y=0
        geo.definir_rectangle(0, 0, 3, -1)

def test_dimensions_nulles():
    with pytest.raises(ValueError):
        geo.definir_rectangle(0, 0, 0, 5)

    with pytest.raises(ValueError):
        geo.definir_rectangle(0, 0, 5, 0)
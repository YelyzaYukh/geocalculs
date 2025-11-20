import pytest
import geocalculs as g


#  Test de création valide
def test_creation_valide():
    l = g.Losange(10, 8, 6)
    assert isinstance(l, g.Losange)
    assert l.surface() == pytest.approx(40.0)
    assert l.perimetre() == pytest.approx(24.0)
    assert "Losange" in l.description()


#  Test d'erreur lors de la création avec valeurs négatives
def test_creation_invalide_negatif():
    with pytest.raises(ValueError) as excinfo:
        g.Losange(-10, 8, 6)
    assert "strictement positives" in str(excinfo.value)


#  Test d'erreur lors de la création avec zéro
def test_creation_invalide_zero():
    with pytest.raises(ValueError) as excinfo:
        g.Losange(0, 10, 5)
    assert "strictement positives" in str(excinfo.value)


#  Test surface correcte
def test_surface_correcte():
    l = g.Losange(12, 5, 4)
    assert l.surface() == pytest.approx(30.0)


#  Test périmètre correct
def test_perimetre_correct():
    l = g.Losange(6, 8, 5)
    assert l.perimetre() == pytest.approx(20.0)


#  Test de description lisible
def test_description_contenu():
    l = g.Losange(10, 8, 6)
    desc = l.description()
    assert "Losange" in desc
    assert "(10" in desc and "8" in desc and "6" in desc

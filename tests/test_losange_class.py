import pytest
import geocalculs as g
import math

#  Test de création valide
def test_creation_valide():
    l = g.Losange(0, 0, 10, 8)   # largeur=10, hauteur=8
    assert isinstance(l, g.Losange)
    assert l.surface() == pytest.approx(40.0)  # 10*8/2 = 40

    cote = math.sqrt((10/2)**2 + (8/2)**2)
    assert l.perimetre() == pytest.approx(4 * cote)

    assert "Losange" in l.description()

#  Test d'erreur lors de la création avec valeurs négatives
def test_creation_invalide_negatif():
    with pytest.raises(ValueError):
        g.Losange(0, 0, -10, 8)

#  Test d'erreur lors de la création avec zéro
def test_creation_invalide_zero():
    with pytest.raises(ValueError):
        g.Losange(0, 0, 0, 5)

#  Test surface correcte
def test_surface_correcte():
    l = g.Losange(0, 0, 12, 5)
    assert l.surface() == pytest.approx(30.0)

#  Test périmètre correct
def test_perimetre_correct():
    l = g.Losange(0, 0, 6, 8)
    cote = math.sqrt((6/2)**2 + (8/2)**2)
    assert l.perimetre() == pytest.approx(4 * cote)

#  Test de description lisible
def test_description_contenu():
    l = g.Losange(1, 2, 10, 8)
    desc = l.description()
    assert "Losange" in desc
    assert "(1" in desc and "2" in desc and "10" in desc and "8" in desc

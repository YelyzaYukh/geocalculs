import pytest
import geocalculs as g

# --- Tests de base pour le périmètre et la surface ---
@pytest.mark.parametrize(
    "largeur,hauteur,perimetre_attendu,surface_attendue",
    [
        (5, 3, 16.0, 15.0),
        (10, 2, 24.0, 20.0),
        (0, 7, 14.0, 0.0),          # largeur nulle
        (7, 0, 14.0, 0.0),          # hauteur nulle
        (2.5, 4.2, 13.4, 10.5),     # valeurs décimales
    ],
)
def test_perimetre_et_surface_rectangle(largeur, hauteur, perimetre_attendu, surface_attendue):
    # Vérifie le périmètre
    assert g.perimetre_rectangle(largeur, hauteur) == pytest.approx(perimetre_attendu)
    # Vérifie la surface
    assert g.surface_rectangle(largeur, hauteur) == pytest.approx(surface_attendue)

def test_types_acceptes():
    """Les fonctions doivent accepter à la fois des entiers et des flottants"""
    assert g.perimetre_rectangle(2, 3) == 10.0
    assert g.surface_rectangle(2, 3.5) == 7.0

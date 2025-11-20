import pytest
import geocalculs as g  

# --- Tests de base pour le périmètre et la surface du cercle ---
@pytest.mark.parametrize(
    "rayon,perimetre_attendu,surface_attendue",
    [
        (1, 2*3.141592653589793, 3.141592653589793),  # cercle unité
        (0, 0.0, 0.0),                                # rayon nul
        (2.5, 2*3.141592653589793*2.5, 3.141592653589793*2.5**2),  # décimal
        (10, 2*3.141592653589793*10, 3.141592653589793*100),       # grand rayon
    ],
)
def test_perimetre_et_surface_cercle(rayon, perimetre_attendu, surface_attendue):
    # Vérifie le périmètre
    assert g.perimetre_cercle(rayon) == pytest.approx(perimetre_attendu)
    # Vérifie la surface
    assert g.surface_cercle(rayon) == pytest.approx(surface_attendue)

def test_types_acceptes():
    """Les fonctions doivent accepter à la fois des entiers et des flottants"""
    assert g.perimetre_cercle(3) == pytest.approx(2*3.141592653589793*3)
    assert g.surface_cercle(3.5) == pytest.approx(3.141592653589793*3.5**2)
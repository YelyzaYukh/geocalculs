import pytest
import geocalculs
import math

def test_polygone_carre():
    # Un carré de 4x4 défini manuellement point par point
    # (0,0) -> (4,0) -> (4,4) -> (0,4)
    points = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
    poly = geocalculs.Polygone(points)

    assert poly.perimetre() == pytest.approx(16.0)
    assert poly.surface() == pytest.approx(16.0)
    assert poly.nombre_de_sommets() == 4

def test_polygone_triangle_rectangle():
    # Triangle 3-4-5
    points = [(0.0, 0.0), (4.0, 0.0), (0.0, 3.0)]
    poly = geocalculs.Polygone(points)

    # Périmètre = 3 + 4 + 5 = 12
    assert poly.perimetre() == pytest.approx(12.0)
    # Surface = (3 * 4) / 2 = 6
    assert poly.surface() == pytest.approx(6.0)

def test_polygone_vide_ou_point():
    """Vérifie que le code ne crash pas avec des formes invalides"""
    poly_vide = geocalculs.Polygone([])
    assert poly_vide.surface() == 0.0
    
    poly_point = geocalculs.Polygone([(1.0, 1.0)])
    assert poly_point.perimetre() == 0.0

def test_hexagone_regulier():
    # Hexagone approximatif de rayon 1
    # On vérifie si la formule du lacet gère bien 6 points
    points = [
        (1.0, 0.0), (0.5, 0.866), (-0.5, 0.866),
        (-1.0, 0.0), (-0.5, -0.866), (0.5, -0.866)
    ]
    poly = geocalculs.Polygone(points)
    
    # Surface théorique hexagone rayon 1 ~= 2.598
    assert math.isclose(poly.surface(), 2.598, abs_tol=0.01)
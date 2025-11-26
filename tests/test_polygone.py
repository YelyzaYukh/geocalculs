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

# ============================================================
#     TESTS DE DISTANCE — POLYGONE ↔ AUTRES FORMES
# ============================================================

import geocalculs as g
import math

# --- Polygone ↔ Point ---
def test_dist_polygone_point_inside():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    p = g.Point(2, 2)
    assert g.dist_point_polygone(p, poly) == 0


def test_dist_polygone_point_outside():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    p = g.Point(10, 10)
    d = g.dist_point_polygone(p, poly)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Polygone ↔ Carré ---
def test_dist_polygone_carre_tangent():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    car = g.Carre(4, 0, 2)
    assert g.dist_carre_polygone(car, poly) == 0


def test_dist_polygone_carre_separe():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    car = g.Carre(10, 10, 2)
    d = g.dist_carre_polygone(car, poly)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Polygone ↔ Rectangle ---
def test_dist_polygone_rectangle_tangent():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    rect = g.Rectangle(4, 0, 3, 3)
    assert g.dist_rectangle_polygone(rect, poly) == 0


def test_dist_polygone_rectangle_separe():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    rect = g.Rectangle(10, 10, 3, 3)
    d = g.dist_rectangle_polygone(rect, poly)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Polygone ↔ Cercle ---
def test_dist_polygone_cercle_tangent():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    cercle = g.Cercle(4, 2, 2)
    assert g.dist_cercle_polygone(cercle, poly) == 0


def test_dist_polygone_cercle_separe():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    cercle = g.Cercle(10, 10, 1)
    d = g.dist_cercle_polygone(cercle, poly)
    attendu = math.sqrt((10-4)**2 + (10-4)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Polygone ↔ Triangle ---
def test_dist_polygone_triangle():
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    tri = g.Triangle(10,0, 10,1, 10,2)
    d = g.dist_triangle_polygone(tri, poly)
    assert math.isclose(d, 6, rel_tol=1e-9)


# --- Polygone ↔ Polygone ---
def test_dist_polygone_polygone_overlap():
    p1 = g.Polygone([(0,0),(4,0),(4,4),(0,4)])
    p2 = g.Polygone([(2,2),(6,2),(6,6),(2,6)])
    assert g.dist_poly_poly(p1, p2) == 0


def test_dist_polygone_polygone_separe():
    p1 = g.Polygone([(0,0),(4,0),(4,4),(0,4)])
    p2 = g.Polygone([(10,10),(12,10),(12,12),(10,12)])
    d = g.dist_poly_poly(p1, p2)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Polygone ↔ Losange ---
def test_dist_polygone_losange():
    poly = g.Polygone([(0,0),(4,0),(4,4),(0,4)])
    los = g.Losange(10, 10, 4, 4)
    d = g.dist_losange_polygone(los, poly)
    assert d > 0

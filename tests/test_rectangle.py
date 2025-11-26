import pytest
import math
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

# ============================================================
#     TESTS DE DISTANCE — RECTANGLE ↔ AUTRES FORMES
# ============================================================

def test_distance_rectangle_point_inside():
    rect = g.Rectangle(0, 0, 4, 4)
    p = g.Point(2, 2)
    assert g.dist_point_rectangle(p, rect) == 0


def test_distance_rectangle_point_outside():
    rect = g.Rectangle(0, 0, 4, 4)
    p = g.Point(10, 10)
    d = g.dist_point_rectangle(p, rect)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Rectangle ↔ Rectangle ---
def test_rect_rect_tangent():
    r1 = g.Rectangle(0, 0, 4, 4)
    r2 = g.Rectangle(4, 0, 4, 4)
    assert g.dist_rect_rect(r1, r2) == 0


def test_rect_rect_separe():
    r1 = g.Rectangle(0, 0, 4, 4)
    r2 = g.Rectangle(10, 10, 3, 3)
    d = g.dist_rect_rect(r1, r2)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Rectangle ↔ Carré ---
def test_distance_rectangle_carre_tangent():
    rect = g.Rectangle(0, 0, 4, 4)
    car = g.Carre(4, 1, 2)
    assert g.dist_rectangle_carre(rect, car) == 0


def test_distance_rectangle_carre_separe():
    rect = g.Rectangle(0, 0, 4, 4)
    car = g.Carre(10, 10, 2)
    d = g.dist_rectangle_carre(rect, car)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Rectangle ↔ Cercle ---
def test_distance_rectangle_cercle_tangent():
    rect = g.Rectangle(0, 0, 4, 4)
    cercle = g.Cercle(4, 2, 2)
    assert g.dist_rectangle_cercle(rect, cercle) == 0


def test_distance_rectangle_cercle_separe():
    rect = g.Rectangle(0, 0, 4, 4)
    cercle = g.Cercle(10, 10, 1)
    d = g.dist_rectangle_cercle(rect, cercle)
    attendu = math.sqrt((10-4)**2 + (10-4)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Rectangle ↔ Triangle ---
def test_distance_rectangle_triangle():
    rect = g.Rectangle(0, 0, 4, 4)
    tri = g.Triangle(10, 0, 10, 2, 10, 4)
    d = g.dist_rectangle_triangle(rect, tri)
    assert math.isclose(d, 6, rel_tol=1e-9)


# --- Rectangle ↔ Polygone ---
def test_distance_rectangle_polygone_tangent():
    rect = g.Rectangle(0, 0, 4, 4)
    poly = g.Polygone([(4,0), (6,0), (6,2), (4,2)])
    assert g.dist_rectangle_polygone(rect, poly) == 0


def test_distance_rectangle_polygone_separe():
    rect = g.Rectangle(0, 0, 4, 4)
    poly = g.Polygone([(10,10), (12,10), (12,12), (10,12)])
    d = g.dist_rectangle_polygone(rect, poly)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Rectangle ↔ Losange ---
def test_distance_rectangle_losange():
    rect = g.Rectangle(0, 0, 4, 4)
    los = g.Losange(10, 10, 4, 4)
    d = g.dist_losange_rectangle(los, rect)
    assert d > 0

import pytest
import math
import geocalculs as g  # module PyO3


# ============================================================
#   TESTS PÉRIMÈTRE / SURFACE
# ============================================================

@pytest.mark.parametrize(
    "cote,perimetre_attendu,surface_attendue",
    [
        (1, 4, 1),          # carré unité
        (0, 0, 0),          # côté nul
        (2.5, 10, 6.25),    # côté décimal
        (10, 40, 100),      # grand carré
    ],
)
def test_perimetre_et_surface_carre(cote, perimetre_attendu, surface_attendue):
    c = g.Carre(0.0, 0.0, cote)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)


def test_types_acceptes():
    c1 = g.Carre(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 12)
    assert math.isclose(c1.surface(), 9)

    c2 = g.Carre(0.0, 0.0, 3.5)
    assert math.isclose(c2.perimetre(), 14)
    assert math.isclose(c2.surface(), 12.25)


def test_carre_new_negatif():
    with pytest.raises(ValueError, match="positif"):
        g.Carre(0.0, 0.0, -3.0)


def test_carre_struct():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0
    assert c.cote == 5.0


def test_carre_perimetre_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.perimetre(), 16.0)


def test_carre_surface_method():
    c = g.Carre(0.0, 0.0, 4.0)
    assert math.isclose(c.surface(), 16.0)


def test_carre_coordonnees():
    c = g.Carre(2.0, 3.0, 5.0)
    assert c.x == 2.0
    assert c.y == 3.0


# ============================================================
#   TESTS DISTANCE — CARRÉ ↔ AUTRES FORMES
# ============================================================

# --- Carré ↔ Cercle ---
def test_dist_carre_cercle_tangent():
    carre = g.Carre(0, 0, 2)
    cercle = g.Cercle(3, 1, 1)
    assert g.dist_carre_cercle(carre, cercle) == 0


def test_dist_carre_cercle_separe():
    carre = g.Carre(0, 0, 2)
    cercle = g.Cercle(5, 5, 1)
    d = g.dist_carre_cercle(carre, cercle)
    attendu = math.sqrt((5 - 2)**2 + (5 - 2)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Carré ↔ Carré ---
def test_dist_carre_carre_tangent():
    c1 = g.Carre(0, 0, 2)
    c2 = g.Carre(2, 0, 2)
    assert g.dist_carre_carre(c1, c2) == 0


def test_dist_carre_carre_separe():
    c1 = g.Carre(0, 0, 2)
    c2 = g.Carre(5, 0, 2)
    assert g.dist_carre_carre(c1, c2) == 3


# --- Carré ↔ Triangle ---
def test_dist_carre_triangle():
    carre = g.Carre(0, 0, 2)
    tri = g.Triangle(5, 0, 5, 1, 5, 2)
    d = g.dist_carre_triangle(carre, tri)
    assert d == 3


# --- Carré ↔ Rectangle ---
def test_dist_carre_rectangle_tangent():
    carre = g.Carre(0, 0, 2)
    rect = g.Rectangle(2, 0, 3, 2)
    assert g.dist_carre_rectangle(carre, rect) == 0


def test_dist_carre_rectangle_separe():
    carre = g.Carre(0, 0, 2)
    rect = g.Rectangle(10, 10, 3, 4)
    d = g.dist_carre_rectangle(carre, rect)
    attendu = math.sqrt((10 - 2)**2 + (10 - 2)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Carré ↔ Polygone ---
def test_dist_carre_polygone():
    carre = g.Carre(0, 0, 2)
    poly = g.Polygone([(5, 0), (6, 1), (5, 2)])
    d = g.dist_carre_polygone(carre, poly)
    assert d == 3


# --- Carré ↔ Losange ---
def test_dist_carre_losange():
    carre = g.Carre(0, 0, 2)
    los = g.Losange(5, 1, 2, 2)
    d = g.dist_losange_carre(los, carre)
    assert d > 0  # simple test : forme séparée


# --- Carré ↔ Point ---
def test_dist_carre_point_inside():
    carre = g.Carre(0, 0, 4)
    p = g.Point(1, 1)
    assert g.dist_point_carre(p, carre) == 0


def test_dist_carre_point_outside():
    carre = g.Carre(0, 0, 2)
    p = g.Point(5, 5)
    d = g.dist_point_carre(p, carre)
    attendu = math.sqrt((5 - 2)**2 + (5 - 2)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)

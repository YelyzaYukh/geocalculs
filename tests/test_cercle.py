import pytest
import math
import geocalculs as g  # module PyO3

# --- Tests de base pour le périmètre et la surface du cercle ---
@pytest.mark.parametrize(
    "rayon,perimetre_attendu,surface_attendue",
    [
        (1, 2*math.pi, math.pi),         # cercle unité
        (0, 0.0, 0.0),                   # rayon nul
        (2.5, 2*math.pi*2.5, math.pi*2.5**2),  # décimal
        (10, 2*math.pi*10, math.pi*100),       # grand rayon
    ],
)
def test_perimetre_et_surface_cercle(rayon, perimetre_attendu, surface_attendue):
    c = g.Cercle(0.0, 0.0, rayon)
    assert math.isclose(c.perimetre(), perimetre_attendu, rel_tol=1e-12)
    assert math.isclose(c.surface(), surface_attendue, rel_tol=1e-12)

# --- Tests pour vérifier les types acceptés (int et float) ---
def test_types_acceptes():
    c1 = g.Cercle(0.0, 0.0, 3)
    assert math.isclose(c1.perimetre(), 2*math.pi*3, rel_tol=1e-12)

    c2 = g.Cercle(0.0, 0.0, 3.5)
    assert math.isclose(c2.surface(), math.pi*3.5**2, rel_tol=1e-12)

# --- Tests pour les rayons négatifs ---
def test_cercle_new_negatif():
    with pytest.raises(ValueError, match="Le rayon ne peut pas être négatif."):
        g.Cercle(0.0, 0.0, -3.0)

# --- Tests de la classe Cercle ---
def test_cercle_struct():
    c = g.Cercle(3.0, 4.0, 5.0)
    assert c.centre_x == 3.0
    assert c.centre_y == 4.0
    assert c.rayon == 5.0

def test_cercle_perimetre_method():
    c = g.Cercle(0.0, 0.0, 1.0)
    assert math.isclose(c.perimetre(), 2.0 * math.pi, rel_tol=1e-12)

def test_cercle_surface_method():
    c = g.Cercle(0.0, 0.0, 2.0)
    assert math.isclose(c.surface(), math.pi * 4.0, rel_tol=1e-12)

# ============================================================
#   TESTS DISTANCE — CERCLE ↔ AUTRES FORMES
# ============================================================

# --- Cercle ↔ Point ---
def test_dist_cercle_point_inside():
    c = g.Cercle(0, 0, 5)
    p = g.Point(1, 1)
    assert g.dist_point_cercle(p, c) == 0  # point à l’intérieur


def test_dist_cercle_point_outside():
    c = g.Cercle(0, 0, 1)
    p = g.Point(5, 0)
    assert g.dist_point_cercle(p, c) == 4  # 5 - 1


# --- Cercle ↔ Cercle ---
def test_dist_cercle_cercle_tangent():
    c1 = g.Cercle(0, 0, 2)
    c2 = g.Cercle(4, 0, 2)
    assert g.dist_cercle_cercle(c1, c2) == 0


def test_dist_cercle_cercle_separe():
    c1 = g.Cercle(0, 0, 2)
    c2 = g.Cercle(10, 0, 3)
    d = g.dist_cercle_cercle(c1, c2)
    assert math.isclose(d, 10 - 2 - 3)  # distance centres - rayons


# --- Cercle ↔ Rectangle ---
def test_dist_cercle_rectangle_tangent():
    rect = g.Rectangle(0, 0, 3, 3)
    c = g.Cercle(3, 1.5, 1.5)
    assert g.dist_cercle_rectangle(c, rect) == 0


def test_dist_cercle_rectangle_separe():
    rect = g.Rectangle(0, 0, 2, 2)
    c = g.Cercle(10, 10, 1)
    d = g.dist_cercle_rectangle(c, rect)
    attendu = math.sqrt((10 - 2)**2 + (10 - 2)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Cercle ↔ Carré ---
def test_dist_cercle_carre_tangent():
    carre = g.Carre(0, 0, 2)
    c = g.Cercle(2, 1, 1)
    assert g.dist_cercle_carre(c, carre) == 0


def test_dist_cercle_carre_separe():
    carre = g.Carre(0, 0, 2)
    c = g.Cercle(6, 6, 1)
    d = g.dist_cercle_carre(c, carre)
    attendu = math.sqrt((6 - 2)**2 + (6 - 2)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)


# --- Cercle ↔ Triangle ---
def test_dist_cercle_triangle():
    tri = g.Triangle(5, 0, 5, 2, 5, 4)
    c = g.Cercle(0, 0, 1)
    d = g.dist_cercle_triangle(c, tri)
    assert math.isclose(d, 4, rel_tol=1e-9)  # distance du point (5,0) au cercle


# --- Cercle ↔ Polygone ---
def test_dist_cercle_polygone():
    poly = g.Polygone([(5, 0), (6, 1), (5, 2)])
    c = g.Cercle(0, 0, 1)
    d = g.dist_cercle_polygone(c, poly)
    assert math.isclose(d, 4, rel_tol=1e-9)  # point le plus proche (5,0)


# --- Cercle ↔ Losange ---
def test_dist_cercle_losange():
    los = g.Losange(10, 10, 4, 4)
    c = g.Cercle(0, 0, 1)
    d = g.dist_losange_cercle(los, c)
    assert d > 0  # juste vérifier séparation

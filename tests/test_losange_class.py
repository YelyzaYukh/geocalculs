import pytest
import geocalculs as g
import math


#  Test de création valide
def test_creation_valide():
    l = g.Losange(10, 8, 6, 4)
    assert isinstance(l, g.Losange)
    assert l.surface() == pytest.approx((6 * 4) / 2)
    assert l.perimetre() > 0
    assert "Losange" in l.description()

#  Test d'erreur valeurs négatives
def test_creation_invalide_negatif():
    with pytest.raises(ValueError):
        g.Losange(10, 8, -6, 4)

#  Test d'erreur largeur ou hauteur = 0
def test_creation_invalide_zero():
    with pytest.raises(ValueError):
        g.Losange(10, 8, 0, 4)

#  Surface correcte
def test_surface_correcte():
    l = g.Losange(0, 0, 12, 5)
    assert l.surface() == pytest.approx((12 * 5) / 2)

#  Perimetre correct (approximation)
def test_perimetre_correct():
    l = g.Losange(0, 0, 6, 8)
    assert l.perimetre() == pytest.approx(4 * ((3**2 + 4**2)**0.5))

# Description
def test_description_contenu():
    l = g.Losange(10, 8, 6, 4)
    desc = l.description()
    assert "Losange" in desc
    assert "(10" in desc and "8" in desc and "6" in desc and "4" in desc

# ============================================================
#   LOSANGE ↔ POINT
# ============================================================

def test_distance_losange_point_inside():
    los = g.Losange(0, 0, 4, 4)
    p = g.Point(0, 0)
    assert g.dist_point_losange(p, los) == 0


def test_distance_losange_point_separe():
    los = g.Losange(0, 0, 4, 4)
    p = g.Point(10, 10)
    d = g.dist_point_losange(p, los)
    assert d > 0


# ============================================================
#   LOSANGE ↔ CARRE
# ============================================================

def test_distance_losange_carre_tangent():
    los = g.Losange(4, 2, 4, 4)
    carre = g.Carre(0, 0, 4)
    # Ils se touchent
    assert g.dist_losange_carre(los, carre) == 0


def test_distance_losange_carre_separe():
    los = g.Losange(10, 10, 4, 4)
    carre = g.Carre(0, 0, 4)
    d = g.dist_losange_carre(los, carre)
    assert d > 0


# ============================================================
#   LOSANGE ↔ RECTANGLE
# ============================================================

def test_distance_losange_rectangle_tangent():
    los = g.Losange(4, 2, 4, 4)
    rect = g.Rectangle(0, 0, 4, 4)
    assert g.dist_losange_rectangle(los, rect) == 0


def test_distance_losange_rectangle_separe():
    los = g.Losange(10, 10, 4, 4)
    rect = g.Rectangle(0, 0, 4, 4)
    d = g.dist_losange_rectangle(los, rect)
    assert d > 0


# ============================================================
#   LOSANGE ↔ CERCLE
# ============================================================

def test_distance_losange_cercle_tangent():
    los = g.Losange(0, 0, 4, 4)
    cercle = g.Cercle(4, 0, 2)
    assert g.dist_losange_cercle(los, cercle) == 0


def test_distance_losange_cercle_separe():
    los = g.Losange(0, 0, 4, 4)
    cercle = g.Cercle(10, 10, 1)
    d = g.dist_losange_cercle(los, cercle)
    assert d > 0


# ============================================================
#   LOSANGE ↔ TRIANGLE
# ============================================================

def test_distance_losange_triangle_tangent():
    los = g.Losange(4, 2, 4, 4)
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    assert g.dist_losange_triangle(los, tri) == 0


def test_distance_losange_triangle_separe():
    los = g.Losange(10, 10, 4, 4)
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    d = g.dist_losange_triangle(los, tri)
    assert d > 0


# ============================================================
#   LOSANGE ↔ POLYGONE
# ============================================================

def test_distance_losange_polygone_tangent():
    los = g.Losange(4, 2, 4, 4)
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    assert g.dist_losange_polygone(los, poly) == 0


def test_distance_losange_polygone_separe():
    los = g.Losange(10, 10, 4, 4)
    poly = g.Polygone([(0,0), (4,0), (4,4), (0,4)])
    d = g.dist_losange_polygone(los, poly)
    assert d > 0


# ============================================================
#   LOSANGE ↔ LOSANGE
# ============================================================

def test_distance_losange_losange_tangent():
    los1 = g.Losange(0, 0, 4, 4)
    los2 = g.Losange(4, 0, 4, 4)
    assert g.dist_losange_losange(los1, los2) == 0


def test_distance_losange_losange_separe():
    los1 = g.Losange(0, 0, 4, 4)
    los2 = g.Losange(10, 10, 4, 4)
    d = g.dist_losange_losange(los1, los2)
    assert d > 0


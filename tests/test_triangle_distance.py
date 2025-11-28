import geocalculs as g
import math

# ============================================================
#     TESTS — TRIANGLE ↔ POINT
# ============================================================

def test_point_triangle_tangent():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    p = g.Point(2, 0)
    assert g.dist_point_triangle(p, tri) == 0


def test_point_triangle_outside():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    p = g.Point(10, 10)
    d = g.dist_point_triangle(p, tri)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)

# ============================================================
#     TESTS — TRIANGLE ↔ TRIANGLE
# ============================================================

def test_triangle_triangle_tangent():
    t1 = g.Triangle(0, 0, 4, 0, 0, 4)
    t2 = g.Triangle(4, 0, 6, 1, 4, 2)
    assert g.dist_triangle_triangle(t1, t2) == 0


def test_triangle_triangle_separe():
    t1 = g.Triangle(0, 0, 4, 0, 0, 4)
    t2 = g.Triangle(10, 10, 12, 10, 10, 12)
    d = g.dist_triangle_triangle(t1, t2)
    attendu = math.sqrt((10-4)**2 + (10-4)**2)
    assert math.isclose(d, attendu, rel_tol=1e-9)

# ============================================================
#     TESTS — TRIANGLE ↔ CARRÉ
# ============================================================

def test_triangle_carre_tangent():
    tri = g.Triangle(4, 1, 6, 1, 5, 3)
    carre = g.Carre(0, 0, 4)
    assert g.dist_triangle_carre(tri, carre) == 0


def test_triangle_carre_separe():
    tri = g.Triangle(10, 0, 12, 1, 10, 2)
    carre = g.Carre(0, 0, 4)
    d = g.dist_triangle_carre(tri, carre)
    attendu = math.sqrt((10-4)**2 + (0-2)**2)
    assert d > 0

# ============================================================
#     TESTS — TRIANGLE ↔ RECTANGLE
# ============================================================

def test_triangle_rectangle_tangent():
    tri = g.Triangle(4, 2, 6, 2, 5, 4)
    rect = g.Rectangle(0, 0, 4, 4)
    assert g.dist_triangle_rectangle(tri, rect) == 0


def test_triangle_rectangle_separe():
    tri = g.Triangle(10, 0, 12, 1, 10, 2)
    rect = g.Rectangle(0, 0, 4, 4)
    d = g.dist_triangle_rectangle(tri, rect)
    assert d > 0

# ============================================================
#     TESTS — TRIANGLE ↔ CERCLE
# ============================================================

def test_triangle_cercle_tangent():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    cercle = g.Cercle(2, 2, math.sqrt(2))
    assert g.dist_triangle_cercle(tri, cercle) == 0


def test_triangle_cercle_separe():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    cercle = g.Cercle(10, 10, 1)
    d = g.dist_triangle_cercle(tri, cercle)
    attendu = math.sqrt((10-4)**2 + (10-4)**2) - 1
    assert math.isclose(d, attendu, rel_tol=1e-9)

# ============================================================
#     TESTS — TRIANGLE ↔ POLYGONE
# ============================================================

def test_triangle_polygone_tangent():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    poly = g.Polygone([(4,0), (6,0), (6,2), (4,2)])
    assert g.dist_triangle_polygone(tri, poly) == 0


def test_triangle_polygone_separe():
    tri = g.Triangle(0, 0, 4, 0, 0, 4)
    poly = g.Polygone([(10,10), (12,10), (12,12), (10,12)])

    d = g.dist_triangle_polygone(tri, poly)

    assert d > 0


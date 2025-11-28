import geocalculs as g

# ============================================================
#  TEST : CARRÉ
# ============================================================
def test_appartenance_carre():
    c = g.Carre(2, 3, 4)   # carré coin (2,3), cote 4

    # Intérieur
    assert g.appartient(3, 4, c, "bord") is True
    assert g.appartient(5, 6, c, "bord") is True

    # Bord
    assert g.appartient(2, 4, c, "bord") is True
    assert g.appartient(6, 5, c, "bord") is True

    # Extérieur
    assert g.appartient(1, 5, c, "bord") is False
    assert g.appartient(8, 10, c, "bord") is False


# ============================================================
#  TEST : RECTANGLE
# ============================================================
def test_appartenance_rectangle():
    r = g.Rectangle(2, 3, 6, 4)   # rectangle coin (2,3), largeur=6 hauteur=4

    # Intérieur
    assert g.appartient(3, 4, r, "bord") is True
    assert g.appartient(7, 6, r, "bord") is True

    # Bord
    assert g.appartient(2, 5, r, "bord") is True
    assert g.appartient(8, 4, r, "bord") is True

    # Extérieur
    assert g.appartient(1, 5, r, "bord") is False
    assert g.appartient(4, 8, r, "bord") is False


# ============================================================
#  TEST : CERCLE
# ============================================================
def test_appartenance_cercle():
    c = g.Cercle(0, 0, 5)

    # Intérieur
    assert g.appartient(2, 2, c, "bord") is True

    # Bord
    assert g.appartient(5, 0, c, "bord") is True

    # Extérieur
    assert g.appartient(6, 0, c, "bord") is False


# ============================================================
#  TEST : LOSANGE
# ============================================================
def test_appartenance_losange():
    l = g.Losange(0, 0, 6, 4)   # centre, largeur=6 hauteur=4

    # Intérieur
    assert g.appartient(0, 0, l, "bord") is True
    assert g.appartient(1, 0.5, l, "bord") is True

    # Bord
    assert g.appartient(3, 0, l, "bord") is True   # sommet droit

    # Extérieur
    assert g.appartient(4, 0, l, "bord") is False


# ============================================================
#  TEST : TRIANGLE
# ============================================================
def test_appartenance_triangle():
    t = g.Triangle(0, 0, 4, 0, 2, 4)

    # Intérieur
    assert g.appartient(2, 1, t, "bord") is True

    # Bord
    assert g.appartient(0, 0, t, "bord") is True

    # Extérieur
    assert g.appartient(5, 5, t, "bord") is False


# ============================================================
#  TEST : POLYGONE
# ============================================================
def test_appartenance_polygone():
    # Polygone carré classique
    pts = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
    p = g.Polygone(pts)

    # Point intérieur
    assert g.appartient(2.0, 2.0, p, "bord") == True

    # Point sur un bord
    assert g.appartient(0.0, 2.0, p, "bord") == True

    # Point sur un sommet
    assert g.appartient(0.0, 0.0, p, "bord") == True

    # Point extérieur
    assert g.appartient(6.0, 6.0, p, "bord") == False

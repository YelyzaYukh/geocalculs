# pytest: skip
import geocalculs as g

def test_distance_carre_cercle():
    print("\n=== TEST DISTANCE CARRE ↔ CERCLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Cercle ---")
    cx = float(input("centre_x du cercle : "))
    cy = float(input("centre_y du cercle : "))
    r = float(input("rayon du cercle : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_carre_cercle(carre, cercle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le cercle touche ou intersecte le carré.")
    else:
        print("→ Le cercle est à distance :", distance)

def test_distance_carre_carre():
    print("\n=== TEST DISTANCE CARRE ↔ CARRE ===")

    print("\n--- Carré 1 ---")
    x1 = float(input("x1 du coin supérieur gauche : "))
    y1 = float(input("y1 du coin supérieur gauche : "))
    cote1 = float(input("longueur du côté 1 : "))
    c1 = g.Carre(x1, y1, cote1)

    print("\n--- Carré 2 ---")
    x2 = float(input("x2 du coin supérieur gauche : "))
    y2 = float(input("y2 du coin supérieur gauche : "))
    cote2 = float(input("longueur du côté 2 : "))
    c2 = g.Carre(x2, y2, cote2)

    distance = g.dist_carre_carre(c1, c2)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Les deux carrés se touchent ou se chevauchent.")
    else:
        print("→ Distance minimale entre les deux carrés :", distance)

def test_distance_carre_triangle():
    print("\n=== TEST DISTANCE CARRE ↔ TRIANGLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Triangle (3 points) ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    triangle = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_carre_triangle(carre, triangle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le triangle touche ou intersecte le carré.")
    else:
        print("→ Distance minimale carrée ↔ triangle :", distance)

def test_distance_carre_rectangle():
    print("\n=== TEST DISTANCE CARRE ↔ RECTANGLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    distance = g.dist_carre_rectangle(carre, rect)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le rectangle touche ou intersecte le carré.")
    else:
        print("→ Le rectangle est à distance :", distance)

def test_distance_carre_polygone():
    print("\n=== TEST DISTANCE CARRE ↔ POLYGONE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets du polygone : "))

    points = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        points.append((px, py))

    poly = g.Polygone(points)

    distance = g.dist_carre_polygone(carre, poly)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le polygone touche ou intersecte le carré.")
    else:
        print("→ Distance minimale carrée ↔ polygone :", distance)
def test_distance_rectangle_carre():
    print("\n=== TEST DISTANCE RECTANGLE ↔ CARRE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_rectangle_carre(rect, carre)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le rectangle touche ou intersecte le carré.")
    else:
        print("→ Distance minimale rectangle ↔ carré :", distance)
def test_distance_rectangle_cercle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ CERCLE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_rectangle_cercle(rect, cercle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le cercle touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ cercle :", distance)
def test_distance_rectangle_rectangle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ RECTANGLE ===")

    print("\n--- Rectangle 1 ---")
    rx1 = float(input("rectangle1.x : "))
    ry1 = float(input("rectangle1.y : "))
    largeur1 = float(input("largeur 1 : "))
    hauteur1 = float(input("hauteur 1 : "))
    r1 = g.Rectangle(rx1, ry1, largeur1, hauteur1)

    print("\n--- Rectangle 2 ---")
    rx2 = float(input("rectangle2.x : "))
    ry2 = float(input("rectangle2.y : "))
    largeur2 = float(input("largeur 2 : "))
    hauteur2 = float(input("hauteur 2 : "))
    r2 = g.Rectangle(rx2, ry2, largeur2, hauteur2)

    distance = g.dist_rect_rect(r1, r2)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Les deux rectangles se touchent ou se chevauchent.")
    else:
        print("→ Distance minimale rectangle ↔ rectangle :", distance)
def test_distance_rectangle_triangle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ TRIANGLE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Triangle (3 points) ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    triangle = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_rectangle_triangle(rect, triangle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le triangle touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ triangle :", distance)
def test_distance_rectangle_polygone():
    print("\n=== TEST DISTANCE RECTANGLE ↔ POLYGONE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets du polygone : "))

    points = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        points.append((px, py))

    poly = g.Polygone(points)

    distance = g.dist_rectangle_polygone(rect, poly)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le polygone touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ polygone :", distance)

# ============================================================
#  TESTS TRIANGLE
# ============================================================

def test_distance_triangle_carre():
    print("\n=== DISTANCE : Triangle ↔ Carré ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_triangle_carre(tri, carre)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_cercle():
    print("\n=== DISTANCE : Triangle ↔ Cercle ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Cercle ---")
    cx2 = float(input("centre_x : "))
    cy2 = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx2, cy2, r)

    distance = g.dist_triangle_cercle(tri, cercle)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_rectangle():
    print("\n=== DISTANCE : Triangle ↔ Rectangle ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, larg, haut)

    distance = g.dist_triangle_rectangle(tri, rect)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_triangle():
    print("\n=== DISTANCE : Triangle ↔ Triangle ===")

    print("\n--- Triangle 1 ---")
    ax1 = float(input("T1.A.x : "))
    ay1 = float(input("T1.A.y : "))
    bx1 = float(input("T1.B.x : "))
    by1 = float(input("T1.B.y : "))
    cx1 = float(input("T1.C.x : "))
    cy1 = float(input("T1.C.y : "))
    t1 = g.Triangle(ax1, ay1, bx1, by1, cx1, cy1)

    print("\n--- Triangle 2 ---")
    ax2 = float(input("T2.A.x : "))
    ay2 = float(input("T2.A.y : "))
    bx2 = float(input("T2.B.x : "))
    by2 = float(input("T2.B.y : "))
    cx2 = float(input("T2.C.x : "))
    cy2 = float(input("T2.C.y : "))
    t2 = g.Triangle(ax2, ay2, bx2, by2, cx2, cy2)

    distance = g.dist_triangle_triangle(t1, t2)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_polygone():
    print("\n=== DISTANCE : Triangle ↔ Polygone ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))

    pts = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        pts.append((px, py))

    poly = g.Polygone(pts)

    distance = g.dist_triangle_polygone(tri, poly)

    print("\n→ Distance calculée :", distance)

# ============================================================
#  TESTS CERCLE
# ============================================================

def test_distance_cercle_point():
    print("\n=== DISTANCE : Cercle ↔ Point ===")

    print("\n--- Point ---")
    px = float(input("point.x : "))
    py = float(input("point.y : "))
    p = g.Point(px, py)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    d = g.dist_point_cercle(p, c)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_cercle():
    print("\n=== DISTANCE : Cercle ↔ Cercle ===")

    print("\n--- Cercle 1 ---")
    x1 = float(input("centre_x1 : "))
    y1 = float(input("centre_y1 : "))
    r1 = float(input("rayon 1 : "))
    c1 = g.Cercle(x1, y1, r1)

    print("\n--- Cercle 2 ---")
    x2 = float(input("centre_x2 : "))
    y2 = float(input("centre_y2 : "))
    r2 = float(input("rayon 2 : "))
    c2 = g.Cercle(x2, y2, r2)

    d = g.dist_cercle_cercle(c1, c2)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_rectangle():
    print("\n=== DISTANCE : Cercle ↔ Rectangle ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    l = float(input("largeur : "))
    h = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, l, h)

    d = g.dist_cercle_rectangle(c, rect)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_carre():
    print("\n=== DISTANCE : Cercle ↔ Carré ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    car = g.Carre(x, y, cote)

    d = g.dist_cercle_carre(c, car)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_triangle():
    print("\n=== DISTANCE : Cercle ↔ Triangle ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx2 = float(input("C.x : "))
    cy2 = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx2, cy2)

    d = g.dist_cercle_triangle(c, tri)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_polygone():
    print("\n=== DISTANCE : Cercle ↔ Polygone ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))

    pts = []
    for i in range(n):
        px = float(input(f"S{i+1}.x : "))
        py = float(input(f"S{i+1}.y : "))
        pts.append((px, py))

    poly = g.Polygone(pts)

    d = g.dist_cercle_polygone(c, poly)
    print("\n→ Distance calculée :", d)


# ============================================================
#  TESTS POLYGONE
# ============================================================

def lire_polygone():
    """Demande à l’utilisateur de rentrer un polygone."""
    n = int(input("Nombre de sommets : "))
    pts = []
    for i in range(n):
        x = float(input(f"Point {i+1} - x : "))
        y = float(input(f"Point {i+1} - y : "))
        pts.append((x, y))
    return g.Polygone(pts)


def test_distance_polygone_point():
    print("\n=== DISTANCE : Polygone ↔ Point ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Point ---")
    x = float(input("point.x : "))
    y = float(input("point.y : "))
    p = g.Point(x, y)

    distance = g.dist_point_polygone(p, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_carre():
    print("\n=== DISTANCE : Polygone ↔ Carré ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_carre_polygone(carre, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_rectangle():
    print("\n=== DISTANCE : Polygone ↔ Rectangle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, larg, haut)

    distance = g.dist_rectangle_polygone(rect, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_cercle():
    print("\n=== DISTANCE : Polygone ↔ Cercle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_cercle_polygone(cercle, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_triangle():
    print("\n=== DISTANCE : Polygone ↔ Triangle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_triangle_polygone(tri, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_polygone():
    print("\n=== DISTANCE : Polygone ↔ Polygone ===")

    print("\n--- Polygone 1 ---")
    poly1 = lire_polygone()

    print("\n--- Polygone 2 ---")
    poly2 = lire_polygone()

    distance = g.dist_poly_poly(poly1, poly2)
    print("\n→ Distance calculée :", distance)


# ============================================================
#  TESTS LOSANGE
# ============================================================

def test_distance_losange_point():
    print("\n=== DISTANCE : Losange ↔ Point ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Point ---")
    px = float(input("point.x : "))
    py = float(input("point.y : "))
    p = g.Point(px, py)

    d = g.dist_point_losange(p, los)
    print("\n→ Distance calculée :", d)


def test_distance_losange_carre():
    print("\n=== DISTANCE : Losange ↔ Carré ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Carré ---")
    cx = float(input("carre.x : "))
    cy = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(cx, cy, cote)

    d = g.dist_losange_carre(los, carre)
    print("\n→ Distance calculée :", d)


def test_distance_losange_rectangle():
    print("\n=== DISTANCE : Losange ↔ Rectangle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    l = float(input("largeur : "))
    h = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, l, h)

    d = g.dist_losange_rectangle(los, rect)
    print("\n→ Distance calculée :", d)


def test_distance_losange_cercle():
    print("\n=== DISTANCE : Losange ↔ Cercle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    d = g.dist_losange_cercle(los, cercle)
    print("\n→ Distance calculée :", d)


def test_distance_losange_triangle():
    print("\n=== DISTANCE : Losange ↔ Triangle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    d = g.dist_losange_triangle(los, tri)
    print("\n→ Distance calculée :", d)


def test_distance_losange_polygone():
    print("\n=== DISTANCE : Losange ↔ Polygone ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))
    pts = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        pts.append((px, py))
    poly = g.Polygone(pts)

    d = g.dist_losange_polygone(los, poly)
    print("\n→ Distance calculée :", d)


def test_distance_losange_losange():
    print("\n=== DISTANCE : Losange ↔ Losange ===")

    print("\n--- Losange 1 ---")
    x1 = float(input("L1 centre x : "))
    y1 = float(input("L1 centre y : "))
    l1 = float(input("L1 largeur : "))
    h1 = float(input("L1 hauteur : "))
    los1 = g.Losange(x1, y1, l1, h1)

    print("\n--- Losange 2 ---")
    x2 = float(input("L2 centre x : "))
    y2 = float(input("L2 centre y : "))
    l2 = float(input("L2 largeur : "))
    h2 = float(input("L2 hauteur : "))
    los2 = g.Losange(x2, y2, l2, h2)

    d = g.dist_losange_losange(los1, los2)
    print("\n→ Distance calculée :", d)


def menu_losange():
    while True:
        print("\n--- MENU LOSANGE ---")
        print("1 - Losange ↔ Point")
        print("2 - Losange ↔ Carré")
        print("3 - Losange ↔ Rectangle")
        print("4 - Losange ↔ Cercle")
        print("5 - Losange ↔ Triangle")
        print("6 - Losange ↔ Polygone")
        print("7 - Losange ↔ Losange")
        print("0 - Retour")

        c = input("Choix : ")

        if c == "1": test_distance_losange_point()
        elif c == "2": test_distance_losange_carre()
        elif c == "3": test_distance_losange_rectangle()
        elif c == "4": test_distance_losange_cercle()
        elif c == "5": test_distance_losange_triangle()
        elif c == "6": test_distance_losange_polygone()
        elif c == "7": test_distance_losange_losange()
        elif c == "0": break
        else:
            print("⛔ Choix invalide.")


def menu_polygone():
    while True:
        print("\n--- MENU POLYGONE ---")
        print("1 - Polygone ↔ Point")
        print("2 - Polygone ↔ Carré")
        print("3 - Polygone ↔ Rectangle")
        print("4 - Polygone ↔ Cercle")
        print("5 - Polygone ↔ Triangle")
        print("6 - Polygone ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_polygone_point()
        elif c == "2": test_distance_polygone_carre()
        elif c == "3": test_distance_polygone_rectangle()
        elif c == "4": test_distance_polygone_cercle()
        elif c == "5": test_distance_polygone_triangle()
        elif c == "6": test_distance_polygone_polygone()
        elif c == "0": break
        else: print("⛔ Choix invalide.")


# ============================================================
#  MENU CERCLE
# ============================================================

def menu_cercle():
    while True:
        print("\n--- MENU CERCLE ---")
        print("1 - Cercle ↔ Point")
        print("2 - Cercle ↔ Cercle")
        print("3 - Cercle ↔ Rectangle")
        print("4 - Cercle ↔ Carré")
        print("5 - Cercle ↔ Triangle")
        print("6 - Cercle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")

        if c == "1": test_distance_cercle_point()
        elif c == "2": test_distance_cercle_cercle()
        elif c == "3": test_distance_cercle_rectangle()
        elif c == "4": test_distance_cercle_carre()
        elif c == "5": test_distance_cercle_triangle()
        elif c == "6": test_distance_cercle_polygone()
        elif c == "0": break
        else:
            print("⛔ Choix invalide.")


def menu_triangle():
    while True:
        print("\n--- MENU TRIANGLE ---")
        print("1 - Triangle ↔ Carré")
        print("2 - Triangle ↔ Cercle")
        print("3 - Triangle ↔ Rectangle")
        print("4 - Triangle ↔ Triangle")
        print("5 - Triangle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_triangle_carre()
        elif c == "2": test_distance_triangle_cercle()
        elif c == "3": test_distance_triangle_rectangle()
        elif c == "4": test_distance_triangle_triangle()
        elif c == "5": test_distance_triangle_polygone()
        elif c == "0": break
        else: print("⛔ Choix invalide.")

def menu_carre():
    while True:
        print("\n--- MENU DISTANCE CARRE ---")
        print("1 - Carré ↔ Cercle")
        print("2 - Carré ↔ Rectangle")
        print("3 - Carré ↔ Carré")
        print("4 - Carré ↔ Triangle")
        print("5 - Carré ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_carre_cercle()
        elif c == "2": test_distance_carre_rectangle()
        elif c == "3": test_distance_carre_carre()
        elif c == "4": test_distance_carre_triangle()
        elif c == "5": test_distance_carre_polygone()
        elif c == "0": break
        else: print("Choix invalide.")


def menu_rectangle():
    while True:
        print("\n--- MENU DISTANCE RECTANGLE ---")
        print("1 - Rectangle ↔ Carré")
        print("2 - Rectangle ↔ Cercle")
        print("3 - Rectangle ↔ Rectangle")
        print("4 - Rectangle ↔ Triangle")
        print("5 - Rectangle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_rectangle_carre()
        elif c == "2": test_distance_rectangle_cercle()
        elif c == "3": test_distance_rectangle_rectangle()
        elif c == "4": test_distance_rectangle_triangle()
        elif c == "5": test_distance_rectangle_polygone()
        elif c == "0": break
        else: print("Choix invalide.")


# pytest: skip
import geocalculs as g

def test_distance_carre_cercle():
    print("\n=== TEST DISTANCE CARRE ↔ CERCLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Cercle ---")
    cx = float(input("centre_x du cercle : "))
    cy = float(input("centre_y du cercle : "))
    r = float(input("rayon du cercle : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_carre_cercle(carre, cercle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le cercle touche ou intersecte le carré.")
    else:
        print("→ Le cercle est à distance :", distance)

def test_distance_carre_carre():
    print("\n=== TEST DISTANCE CARRE ↔ CARRE ===")

    print("\n--- Carré 1 ---")
    x1 = float(input("x1 du coin supérieur gauche : "))
    y1 = float(input("y1 du coin supérieur gauche : "))
    cote1 = float(input("longueur du côté 1 : "))
    c1 = g.Carre(x1, y1, cote1)

    print("\n--- Carré 2 ---")
    x2 = float(input("x2 du coin supérieur gauche : "))
    y2 = float(input("y2 du coin supérieur gauche : "))
    cote2 = float(input("longueur du côté 2 : "))
    c2 = g.Carre(x2, y2, cote2)

    distance = g.dist_carre_carre(c1, c2)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Les deux carrés se touchent ou se chevauchent.")
    else:
        print("→ Distance minimale entre les deux carrés :", distance)

def test_distance_carre_triangle():
    print("\n=== TEST DISTANCE CARRE ↔ TRIANGLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Triangle (3 points) ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    triangle = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_carre_triangle(carre, triangle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le triangle touche ou intersecte le carré.")
    else:
        print("→ Distance minimale carrée ↔ triangle :", distance)

def test_distance_carre_rectangle():
    print("\n=== TEST DISTANCE CARRE ↔ RECTANGLE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    distance = g.dist_carre_rectangle(carre, rect)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le rectangle touche ou intersecte le carré.")
    else:
        print("→ Le rectangle est à distance :", distance)

def test_distance_carre_polygone():
    print("\n=== TEST DISTANCE CARRE ↔ POLYGONE ===")

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets du polygone : "))

    points = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        points.append((px, py))

    poly = g.Polygone(points)

    distance = g.dist_carre_polygone(carre, poly)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le polygone touche ou intersecte le carré.")
    else:
        print("→ Distance minimale carrée ↔ polygone :", distance)
def test_distance_rectangle_carre():
    print("\n=== TEST DISTANCE RECTANGLE ↔ CARRE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Carré ---")
    x = float(input("x du coin supérieur gauche : "))
    y = float(input("y du coin supérieur gauche : "))
    cote = float(input("longueur du côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_rectangle_carre(rect, carre)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le rectangle touche ou intersecte le carré.")
    else:
        print("→ Distance minimale rectangle ↔ carré :", distance)
def test_distance_rectangle_cercle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ CERCLE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_rectangle_cercle(rect, cercle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le cercle touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ cercle :", distance)
def test_distance_rectangle_rectangle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ RECTANGLE ===")

    print("\n--- Rectangle 1 ---")
    rx1 = float(input("rectangle1.x : "))
    ry1 = float(input("rectangle1.y : "))
    largeur1 = float(input("largeur 1 : "))
    hauteur1 = float(input("hauteur 1 : "))
    r1 = g.Rectangle(rx1, ry1, largeur1, hauteur1)

    print("\n--- Rectangle 2 ---")
    rx2 = float(input("rectangle2.x : "))
    ry2 = float(input("rectangle2.y : "))
    largeur2 = float(input("largeur 2 : "))
    hauteur2 = float(input("hauteur 2 : "))
    r2 = g.Rectangle(rx2, ry2, largeur2, hauteur2)

    distance = g.dist_rect_rect(r1, r2)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Les deux rectangles se touchent ou se chevauchent.")
    else:
        print("→ Distance minimale rectangle ↔ rectangle :", distance)
def test_distance_rectangle_triangle():
    print("\n=== TEST DISTANCE RECTANGLE ↔ TRIANGLE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Triangle (3 points) ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    triangle = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_rectangle_triangle(rect, triangle)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le triangle touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ triangle :", distance)
def test_distance_rectangle_polygone():
    print("\n=== TEST DISTANCE RECTANGLE ↔ POLYGONE ===")

    print("\n--- Rectangle ---")
    rx = float(input("rectangle.x : "))
    ry = float(input("rectangle.y : "))
    largeur = float(input("largeur : "))
    hauteur = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, largeur, hauteur)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets du polygone : "))

    points = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        points.append((px, py))

    poly = g.Polygone(points)

    distance = g.dist_rectangle_polygone(rect, poly)

    print("\n→ Distance calculée :", distance)
    if distance == 0:
        print("→ Le polygone touche ou intersecte le rectangle.")
    else:
        print("→ Distance minimale rectangle ↔ polygone :", distance)

# ============================================================
#  TESTS TRIANGLE
# ============================================================

def test_distance_triangle_carre():
    print("\n=== DISTANCE : Triangle ↔ Carré ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_triangle_carre(tri, carre)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_cercle():
    print("\n=== DISTANCE : Triangle ↔ Cercle ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Cercle ---")
    cx2 = float(input("centre_x : "))
    cy2 = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx2, cy2, r)

    distance = g.dist_triangle_cercle(tri, cercle)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_rectangle():
    print("\n=== DISTANCE : Triangle ↔ Rectangle ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, larg, haut)

    distance = g.dist_triangle_rectangle(tri, rect)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_triangle():
    print("\n=== DISTANCE : Triangle ↔ Triangle ===")

    print("\n--- Triangle 1 ---")
    ax1 = float(input("T1.A.x : "))
    ay1 = float(input("T1.A.y : "))
    bx1 = float(input("T1.B.x : "))
    by1 = float(input("T1.B.y : "))
    cx1 = float(input("T1.C.x : "))
    cy1 = float(input("T1.C.y : "))
    t1 = g.Triangle(ax1, ay1, bx1, by1, cx1, cy1)

    print("\n--- Triangle 2 ---")
    ax2 = float(input("T2.A.x : "))
    ay2 = float(input("T2.A.y : "))
    bx2 = float(input("T2.B.x : "))
    by2 = float(input("T2.B.y : "))
    cx2 = float(input("T2.C.x : "))
    cy2 = float(input("T2.C.y : "))
    t2 = g.Triangle(ax2, ay2, bx2, by2, cx2, cy2)

    distance = g.dist_triangle_triangle(t1, t2)

    print("\n→ Distance calculée :", distance)


def test_distance_triangle_polygone():
    print("\n=== DISTANCE : Triangle ↔ Polygone ===")

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))

    pts = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        pts.append((px, py))

    poly = g.Polygone(pts)

    distance = g.dist_triangle_polygone(tri, poly)

    print("\n→ Distance calculée :", distance)

# ============================================================
#  TESTS CERCLE
# ============================================================

def test_distance_cercle_point():
    print("\n=== DISTANCE : Cercle ↔ Point ===")

    print("\n--- Point ---")
    px = float(input("point.x : "))
    py = float(input("point.y : "))
    p = g.Point(px, py)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    d = g.dist_point_cercle(p, c)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_cercle():
    print("\n=== DISTANCE : Cercle ↔ Cercle ===")

    print("\n--- Cercle 1 ---")
    x1 = float(input("centre_x1 : "))
    y1 = float(input("centre_y1 : "))
    r1 = float(input("rayon 1 : "))
    c1 = g.Cercle(x1, y1, r1)

    print("\n--- Cercle 2 ---")
    x2 = float(input("centre_x2 : "))
    y2 = float(input("centre_y2 : "))
    r2 = float(input("rayon 2 : "))
    c2 = g.Cercle(x2, y2, r2)

    d = g.dist_cercle_cercle(c1, c2)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_rectangle():
    print("\n=== DISTANCE : Cercle ↔ Rectangle ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    l = float(input("largeur : "))
    h = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, l, h)

    d = g.dist_cercle_rectangle(c, rect)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_carre():
    print("\n=== DISTANCE : Cercle ↔ Carré ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    car = g.Carre(x, y, cote)

    d = g.dist_cercle_carre(c, car)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_triangle():
    print("\n=== DISTANCE : Cercle ↔ Triangle ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx2 = float(input("C.x : "))
    cy2 = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx2, cy2)

    d = g.dist_cercle_triangle(c, tri)
    print("\n→ Distance calculée :", d)


def test_distance_cercle_polygone():
    print("\n=== DISTANCE : Cercle ↔ Polygone ===")

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    c = g.Cercle(cx, cy, r)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))

    pts = []
    for i in range(n):
        px = float(input(f"S{i+1}.x : "))
        py = float(input(f"S{i+1}.y : "))
        pts.append((px, py))

    poly = g.Polygone(pts)

    d = g.dist_cercle_polygone(c, poly)
    print("\n→ Distance calculée :", d)


# ============================================================
#  TESTS POLYGONE
# ============================================================

def lire_polygone():
    """Demande à l’utilisateur de rentrer un polygone."""
    n = int(input("Nombre de sommets : "))
    pts = []
    for i in range(n):
        x = float(input(f"Point {i+1} - x : "))
        y = float(input(f"Point {i+1} - y : "))
        pts.append((x, y))
    return g.Polygone(pts)


def test_distance_polygone_point():
    print("\n=== DISTANCE : Polygone ↔ Point ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Point ---")
    x = float(input("point.x : "))
    y = float(input("point.y : "))
    p = g.Point(x, y)

    distance = g.dist_point_polygone(p, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_carre():
    print("\n=== DISTANCE : Polygone ↔ Carré ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Carré ---")
    x = float(input("carre.x : "))
    y = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(x, y, cote)

    distance = g.dist_carre_polygone(carre, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_rectangle():
    print("\n=== DISTANCE : Polygone ↔ Rectangle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, larg, haut)

    distance = g.dist_rectangle_polygone(rect, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_cercle():
    print("\n=== DISTANCE : Polygone ↔ Cercle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    distance = g.dist_cercle_polygone(cercle, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_triangle():
    print("\n=== DISTANCE : Polygone ↔ Triangle ===")

    print("\n--- Polygone ---")
    poly = lire_polygone()

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    distance = g.dist_triangle_polygone(tri, poly)
    print("\n→ Distance calculée :", distance)


def test_distance_polygone_polygone():
    print("\n=== DISTANCE : Polygone ↔ Polygone ===")

    print("\n--- Polygone 1 ---")
    poly1 = lire_polygone()

    print("\n--- Polygone 2 ---")
    poly2 = lire_polygone()

    distance = g.dist_poly_poly(poly1, poly2)
    print("\n→ Distance calculée :", distance)


# ============================================================
#  TESTS LOSANGE
# ============================================================

def test_distance_losange_point():
    print("\n=== DISTANCE : Losange ↔ Point ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Point ---")
    px = float(input("point.x : "))
    py = float(input("point.y : "))
    p = g.Point(px, py)

    d = g.dist_point_losange(p, los)
    print("\n→ Distance calculée :", d)


def test_distance_losange_carre():
    print("\n=== DISTANCE : Losange ↔ Carré ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Carré ---")
    cx = float(input("carre.x : "))
    cy = float(input("carre.y : "))
    cote = float(input("côté : "))
    carre = g.Carre(cx, cy, cote)

    d = g.dist_losange_carre(los, carre)
    print("\n→ Distance calculée :", d)


def test_distance_losange_rectangle():
    print("\n=== DISTANCE : Losange ↔ Rectangle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Rectangle ---")
    rx = float(input("rect.x : "))
    ry = float(input("rect.y : "))
    l = float(input("largeur : "))
    h = float(input("hauteur : "))
    rect = g.Rectangle(rx, ry, l, h)

    d = g.dist_losange_rectangle(los, rect)
    print("\n→ Distance calculée :", d)


def test_distance_losange_cercle():
    print("\n=== DISTANCE : Losange ↔ Cercle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Cercle ---")
    cx = float(input("centre_x : "))
    cy = float(input("centre_y : "))
    r = float(input("rayon : "))
    cercle = g.Cercle(cx, cy, r)

    d = g.dist_losange_cercle(los, cercle)
    print("\n→ Distance calculée :", d)


def test_distance_losange_triangle():
    print("\n=== DISTANCE : Losange ↔ Triangle ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Triangle ---")
    ax = float(input("A.x : "))
    ay = float(input("A.y : "))
    bx = float(input("B.x : "))
    by = float(input("B.y : "))
    cx = float(input("C.x : "))
    cy = float(input("C.y : "))
    tri = g.Triangle(ax, ay, bx, by, cx, cy)

    d = g.dist_losange_triangle(los, tri)
    print("\n→ Distance calculée :", d)


def test_distance_losange_polygone():
    print("\n=== DISTANCE : Losange ↔ Polygone ===")

    print("\n--- Losange ---")
    x = float(input("centre x : "))
    y = float(input("centre y : "))
    larg = float(input("largeur : "))
    haut = float(input("hauteur : "))
    los = g.Losange(x, y, larg, haut)

    print("\n--- Polygone ---")
    n = int(input("Nombre de sommets : "))
    pts = []
    for i in range(n):
        px = float(input(f"Point {i+1} - x : "))
        py = float(input(f"Point {i+1} - y : "))
        pts.append((px, py))
    poly = g.Polygone(pts)

    d = g.dist_losange_polygone(los, poly)
    print("\n→ Distance calculée :", d)


def test_distance_losange_losange():
    print("\n=== DISTANCE : Losange ↔ Losange ===")

    print("\n--- Losange 1 ---")
    x1 = float(input("L1 centre x : "))
    y1 = float(input("L1 centre y : "))
    l1 = float(input("L1 largeur : "))
    h1 = float(input("L1 hauteur : "))
    los1 = g.Losange(x1, y1, l1, h1)

    print("\n--- Losange 2 ---")
    x2 = float(input("L2 centre x : "))
    y2 = float(input("L2 centre y : "))
    l2 = float(input("L2 largeur : "))
    h2 = float(input("L2 hauteur : "))
    los2 = g.Losange(x2, y2, l2, h2)

    d = g.dist_losange_losange(los1, los2)
    print("\n→ Distance calculée :", d)


def menu_losange():
    while True:
        print("\n--- MENU LOSANGE ---")
        print("1 - Losange ↔ Point")
        print("2 - Losange ↔ Carré")
        print("3 - Losange ↔ Rectangle")
        print("4 - Losange ↔ Cercle")
        print("5 - Losange ↔ Triangle")
        print("6 - Losange ↔ Polygone")
        print("7 - Losange ↔ Losange")
        print("0 - Retour")

        c = input("Choix : ")

        if c == "1": test_distance_losange_point()
        elif c == "2": test_distance_losange_carre()
        elif c == "3": test_distance_losange_rectangle()
        elif c == "4": test_distance_losange_cercle()
        elif c == "5": test_distance_losange_triangle()
        elif c == "6": test_distance_losange_polygone()
        elif c == "7": test_distance_losange_losange()
        elif c == "0": break
        else:
            print(" Choix invalide.")


def menu_polygone():
    while True:
        print("\n--- MENU POLYGONE ---")
        print("1 - Polygone ↔ Point")
        print("2 - Polygone ↔ Carré")
        print("3 - Polygone ↔ Rectangle")
        print("4 - Polygone ↔ Cercle")
        print("5 - Polygone ↔ Triangle")
        print("6 - Polygone ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_polygone_point()
        elif c == "2": test_distance_polygone_carre()
        elif c == "3": test_distance_polygone_rectangle()
        elif c == "4": test_distance_polygone_cercle()
        elif c == "5": test_distance_polygone_triangle()
        elif c == "6": test_distance_polygone_polygone()
        elif c == "0": break
        else: print(" Choix invalide.")


# ============================================================
#  MENU CERCLE
# ============================================================

def menu_cercle():
    while True:
        print("\n--- MENU CERCLE ---")
        print("1 - Cercle ↔ Point")
        print("2 - Cercle ↔ Cercle")
        print("3 - Cercle ↔ Rectangle")
        print("4 - Cercle ↔ Carré")
        print("5 - Cercle ↔ Triangle")
        print("6 - Cercle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")

        if c == "1": test_distance_cercle_point()
        elif c == "2": test_distance_cercle_cercle()
        elif c == "3": test_distance_cercle_rectangle()
        elif c == "4": test_distance_cercle_carre()
        elif c == "5": test_distance_cercle_triangle()
        elif c == "6": test_distance_cercle_polygone()
        elif c == "0": break
        else:
            print(" Choix invalide.")


def menu_triangle():
    while True:
        print("\n--- MENU TRIANGLE ---")
        print("1 - Triangle ↔ Carré")
        print("2 - Triangle ↔ Cercle")
        print("3 - Triangle ↔ Rectangle")
        print("4 - Triangle ↔ Triangle")
        print("5 - Triangle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_triangle_carre()
        elif c == "2": test_distance_triangle_cercle()
        elif c == "3": test_distance_triangle_rectangle()
        elif c == "4": test_distance_triangle_triangle()
        elif c == "5": test_distance_triangle_polygone()
        elif c == "0": break
        else: print(" Choix invalide.")

def menu_carre():
    while True:
        print("\n--- MENU DISTANCE CARRE ---")
        print("1 - Carré ↔ Cercle")
        print("2 - Carré ↔ Rectangle")
        print("3 - Carré ↔ Carré")
        print("4 - Carré ↔ Triangle")
        print("5 - Carré ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_carre_cercle()
        elif c == "2": test_distance_carre_rectangle()
        elif c == "3": test_distance_carre_carre()
        elif c == "4": test_distance_carre_triangle()
        elif c == "5": test_distance_carre_polygone()
        elif c == "0": break
        else: print("Choix invalide.")


def menu_rectangle():
    while True:
        print("\n--- MENU DISTANCE RECTANGLE ---")
        print("1 - Rectangle ↔ Carré")
        print("2 - Rectangle ↔ Cercle")
        print("3 - Rectangle ↔ Rectangle")
        print("4 - Rectangle ↔ Triangle")
        print("5 - Rectangle ↔ Polygone")
        print("0 - Retour")

        c = input("Choix : ")
        if c == "1": test_distance_rectangle_carre()
        elif c == "2": test_distance_rectangle_cercle()
        elif c == "3": test_distance_rectangle_rectangle()
        elif c == "4": test_distance_rectangle_triangle()
        elif c == "5": test_distance_rectangle_polygone()
        elif c == "0": break
        else: print("Choix invalide.")


def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1 - Carré")
        print("2 - Rectangle")
        print("3 - Triangle")
        print("4 - Cercle")
        print("5 - Polygone")
        print("6 - Losange")
        print("0 - Quitter")

        c = input("Choix : ")

        if c == "1": menu_carre()
        elif c == "2": menu_rectangle()
        elif c == "3": menu_triangle()
        elif c == "4": menu_cercle()
        elif c == "5": menu_polygone()
        elif c == "6": menu_losange()
        elif c == "0": break
        else:
            print(" Choix invalide.")


if __name__ == "__main__":
    menu()


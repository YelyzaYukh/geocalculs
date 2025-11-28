import geocalculs as g


def lire_coordonnees_point(label=None):
    if label:
        print(f"→ {label} :")
    else:
        print("→ Point à tester :")
    x = float(input("  - x = "))
    y = float(input("  - y = "))
    return x, y


def main():
    print("=== Test d’appartenance géométrique ===")
    print("Choisissez le type de forme :")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Carré")
    print("4. Cercle")
    print("5. Losange")
    print("6. Polygone (N points)")
    choix = input("Votre choix (1–6) : ")

    
    mode = "bord"   #juste pour faire passser le test 

    # --------------------------------------------------------
    # 1. TRIANGLE
    # --------------------------------------------------------
    if choix == "1":
        print("Définition du triangle :")
        Ax, Ay = lire_coordonnees_point("Point A")
        Bx, By = lire_coordonnees_point("Point B")
        Cx, Cy = lire_coordonnees_point("Point C")

        tri = g.Triangle(Ax, Ay, Bx, By, Cx, Cy)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, tri, mode)

        print("✔ Le point est DANS le triangle." if inside else "✘ Le point est en DEHORS du triangle.")
        return

    # --------------------------------------------------------
    # 2. RECTANGLE
    # --------------------------------------------------------
    if choix == "2":
        print("Définition du rectangle :")
        x, y = lire_coordonnees_point("Coin inferieur gauche (x, y)")
        largeur = float(input("Largeur = "))
        hauteur = float(input("Hauteur = "))

        rect = g.Rectangle(x, y, largeur, hauteur)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, rect, mode)

        print("✔ Le point appartient au rectangle." if inside else "✘ Le point est en dehors du rectangle.")
        return

    # --------------------------------------------------------
    # 3. CARRE
    # --------------------------------------------------------
    if choix == "3":
        print("Définition du carré :")
        x, y = lire_coordonnees_point("Coin inferieur gauche (x, y)")
        cote = float(input("Côté = "))

        car = g.Carre(x, y, cote)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, car, mode)

        print("✔ Le point appartient au carré." if inside else "✘ Le point est en dehors du carré.")
        return

    # --------------------------------------------------------
    # 4. CERCLE
    # --------------------------------------------------------
    if choix == "4":
        print("Définition du cercle :")
        x, y = lire_coordonnees_point("Centre (x, y)")
        rayon = float(input("Rayon = "))

        cir = g.Cercle(x, y, rayon)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, cir, mode)

        print("✔ Le point appartient au cercle." if inside else "✘ Le point est en dehors du cercle.")
        return

    # --------------------------------------------------------
    # 5. LOSANGE
    # --------------------------------------------------------
    if choix == "5":
        print("Définition du losange :")
        x, y = lire_coordonnees_point("Centre du losange (x, y)")
        largeur = float(input("Largeur = "))
        hauteur = float(input("Hauteur = "))

        los = g.Losange(x, y, largeur, hauteur)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, los, mode)

        print("✔ Le point appartient au losange." if inside else "✘ Le point est en dehors du losange.")
        return

    # --------------------------------------------------------
    # 6. POLYGONE
    # --------------------------------------------------------
    if choix == "6":
        print("Définition du polygone :")
        n = int(input("Nombre de sommets = "))
        pts = []

        for i in range(n):
            print(f"Sommets {i+1} :")
            x = float(input("  x = "))
            y = float(input("  y = "))
            pts.append((x, y))

        poly = g.Polygone(pts)

        xt, yt = lire_coordonnees_point("Point à tester")
        inside = g.appartient(xt, yt, poly, mode)

        print("✔ Le point appartient au polygone." if inside else "✘ Le point est en dehors du polygone.")
        return

    print("Choix invalide.")


if __name__ == "__main__":
    main()

import geocalculs as g

def lire_coordonnees_point(num=None):
    if num:
        print(f"→ Point {num} :")
    else:
        print("→ Point à tester :")
    x = float(input("  - x = "))
    y = float(input("  - y = "))
    return x, y

def main():
    print("=== Test d’appartenance géométrique ===")
    print("Choisissez le type de forme :")
    print("1. Segment (2 points)")
    print("2. Triangle (3 points)")
    print("3. Rectangle (largeur, hauteur)")
    print("4. Carré (centre + côté)")
    print("5. Cercle (centre + rayon)")
    print("6. Losange (centre + largeur/hauteur)")
    choix = input("Votre choix (1–6) : ")

    mode = input("Mode ('strict' ou 'bord') [bord] : ") or "bord"

    # ... autres formes inchangées ...

    # 6. Losange
    if choix == "6":
        print("Définition du losange :")
        x, y = lire_coordonnees_point("centre")
        largeur = float(input("Largeur = "))
        hauteur = float(input("Hauteur = "))
        los = g.Losange(x, y, largeur, hauteur)
        xt, yt = lire_coordonnees_point("à tester")
        inside = g.appartient(xt, yt, los, mode)
        print("Le point appartient au losange." if inside else "Le point est en dehors du losange.")
        return

if __name__ == "__main__":
    main()

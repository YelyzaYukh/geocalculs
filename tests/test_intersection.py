import pytest
import geocalculs as g

# ==========================================
# 1. TEST CRITIQUE : POLYGONE CONCAVE (Le "U")
# ==========================================
def test_polygone_concave_forme_en_u():
    """
    On dessine un "U" ou un "Pot de fleur".
    Il est plein sur les bords, mais vide au milieu.
    
    Structure du U (4x4) :
    Largeur des murs : 1
    Vide central : entre x=1 et x=3, à partir de y=1
    
      (0,4)       (1,4)       (3,4)       (4,4)
        +-----------+           +-----------+
        |   MUR G   |   VIDE    |   MUR D   |
        |           | (Pas de   |           |
        |   (0,1)   | collision)|   (4,1)   |
        +---+-------+-----------+-------+---+
        |   | (1,1)               (3,1) |   |
        |   +---------------------------+   |
        |             BASE (4,0)            |
        +-----------------------------------+
      (0,0)
    """
    points_u = [
        (0,0), (4,0),  # Bas total
        (4,4), (3,4),  # Mur Droit (Haut puis retour)
        (3,1), (1,1),  # Le fond du creux
        (1,4), (0,4)   # Mur Gauche (Haut puis retour)
    ]
    forme_u = g.Polygone(points_u)

    # --- A. Collision DANS le mur (Doit être VRAI) ---
    # Un petit carré placé dans le mur de gauche
    objet_dans_mur = g.Carre(0.2, 2, 0.5) 
    assert g.intersecte(forme_u, objet_dans_mur) is True, \
        "ÉCHEC: L'objet est dans le mur gauche, il devrait être détecté."

    # --- B. Collision DANS le vide (Doit être FAUX) ---
    # C'est LE test qui prouve que ta triangulation fonctionne.
    # Un petit carré placé au milieu du U (x=2, y=2)
    objet_dans_vide = g.Carre(1.8, 2, 0.4) 
    assert g.intersecte(forme_u, objet_dans_vide) is False, \
        "ÉCHEC: L'objet est dans le vide du U, il NE devrait PAS être détecté (Problème de triangulation ?)."

    # --- C. Collision AVEC le fond (Doit être VRAI) ---
    # Un carré qui touche le fond du U
    objet_fond = g.Carre(2, 0.5, 0.5)
    assert g.intersecte(forme_u, objet_fond) is True, \
        "ÉCHEC: L'objet touche le fond du U."


# ==========================================
# 2. TEST POLYGONE vs CERCLE
# ==========================================
def test_polygone_vs_cercle():
    # Triangle rectangle simple (0,0) -> (4,0) -> (0,3)
    tri = g.Triangle(0, 0, 4, 0, 0, 3)

    # 1. Cercle qui mord le coin (0,0)
    c1 = g.Cercle(0, 0, 0.5)
    assert g.intersecte(tri, c1) is True

    # 2. Cercle qui touche l'hypoténuse (le côté en biais)
    # Le milieu de l'hypoténuse est (2, 1.5). On place un cercle juste dessus.
    c2 = g.Cercle(2, 1.5, 0.1)
    assert g.intersecte(tri, c2) is True

    # 3. Cercle juste à côté de l'hypoténuse (Dehors)
    c3 = g.Cercle(2.2, 1.7, 0.1)
    assert g.intersecte(tri, c3) is False


# ==========================================
# 3. TEST DE REGRESSION (Formes Simples)
# ==========================================
def test_formes_simples():
    """Vérifie que les rectangles et carrés marchent toujours"""
    
    # Rectangle vs Rectangle
    r1 = g.Rectangle(0, 0, 10, 10)
    r2 = g.Rectangle(5, 5, 10, 10) # Chevauchement
    r3 = g.Rectangle(20, 20, 10, 10) # Loin

    assert g.intersecte(r1, r2) is True
    assert g.intersecte(r1, r3) is False

    # Carré vs Cercle
    c = g.Carre(0, 0, 2) # Centre (1,1)
    # Cercle centré en (1,1) -> Dedans
    cercle = g.Cercle(1, 1, 0.5)
    assert g.intersecte(c, cercle) is True


# ==========================================
# 4. TEST INCLUSION TOTALE
# ==========================================
def test_inclusion():
    """Un petit objet entièrement dans un grand"""
    grand = g.Rectangle(0, 0, 100, 100)
    petit = g.Triangle(10, 10, 20, 10, 15, 20)
    
    assert g.intersecte(grand, petit) is True
    assert g.intersecte(petit, grand) is True # Symétrie

# ==========================================
# 5. TEST TRIANGLE vs TRIANGLE (Spécifique SAT)
# ==========================================
def test_triangle_vs_triangle_sat():
    """
    Test spécifique pour vérifier que les axes normaux des triangles
    sont bien calculés par le SAT.
    """
    # Triangle A (Base 0-4, Sommet 2,3)
    t1 = g.Triangle(0, 0, 4, 0, 2, 3)

    # Triangle B (Inversé, pointe vers le bas)
    # Sommet (2, -1) -> Il rentre dans la base de T1
    t2 = g.Triangle(0, 2, 4, 2, 2, -1)

    # Ils forment une étoile de David, ils se croisent au milieu
    assert g.intersecte(t1, t2) is True

    # Triangle C (Loin à droite)
    t3 = g.Triangle(10, 0, 14, 0, 12, 3)
    assert g.intersecte(t1, t3) is False


# ==========================================
# 6. TEST CAS LIMITES (TOUCHER JUSTE)
# ==========================================
def test_toucher_juste():
    """
    Deux objets qui partagent exactement une ligne commune.
    Doit être True (contact = collision).
    """
    # Carré gauche [0,0] -> [2,2]
    c1 = g.Carre(0, 0, 2)
    
    # Carré droite [2,0] -> [4,2]
    # Ils partagent la ligne x=2
    c2 = g.Carre(2, 0, 2)
    
    assert g.intersecte(c1, c2) is True


# ==========================================
# 7. TEST ÉTOILE (CONCAVE COMPLEXE)
# ==========================================
def test_etoile_concave():
    """
    Une étoile est une forme concave complexe.
    Si la triangulation marche, on peut passer entre les branches.
    """
    # Étoile simplifiée à 4 branches (comme une rose des vents)
    # Sommets externes : (2,0), (0,2), (-2,0), (0,-2)
    # Sommets internes (creux) : (0.5, 0.5), (-0.5, 0.5)...
    points = [
        (2,0), (0.5, 0.5), # Branche Droite
        (0,2), (-0.5, 0.5), # Branche Haut
        (-2,0), (-0.5, -0.5), # Branche Gauche
        (0,-2), (0.5, -0.5)  # Branche Bas
    ]
    etoile = g.Polygone(points)

    # 1. Collision au centre
    c_centre = g.Cercle(0, 0, 0.2)
    assert g.intersecte(etoile, c_centre) is True

    # 2. Collision dans une branche (Pointe Droite)
    c_branche = g.Cercle(1.5, 0, 0.2)
    assert g.intersecte(etoile, c_branche) is True

    # 3. PAS de collision entre les branches (Le vide)
    # Point (1, 1) -> C'est dans le coin, hors de l'étoile
    c_vide = g.Cercle(1, 1, 0.1)
    assert g.intersecte(etoile, c_vide) is False


if __name__ == "__main__":
    print("🚀 Lancement des tests complets d'intersection...")
    
    try:
        test_polygone_concave_forme_en_u()
        print("Test Concave (Forme en U) : SUCCÈS")
        
        test_polygone_vs_cercle()
        print("Test Polygone vs Cercle : SUCCÈS")
        
        test_formes_simples()
        print("Test Formes Simples : SUCCÈS")
        
        test_inclusion()
        print("Test Inclusion : SUCCÈS")

        test_triangle_vs_triangle_sat()
        print("Test triange vs triangle (sat algo) : SUCCÈS")

        test_toucher_juste()
        print("Test toucher juste : SUCCÈS")

        test_etoile_concave()
        print("Test etoile concave : SUCCÈS")

        
        print("\nTOUS LES TESTS SONT PASSÉS ! Ton moteur est robuste.")
        
    except AssertionError as e:
        print(f"\néCHEC : {e}")
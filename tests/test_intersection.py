import geocalculs as g
import pytest

def test_intersection_carres():
    # Deux carrés qui se touchent
    c1 = g.Carre(0, 0, 10)   # De (0,0) à (10,10)
    c2 = g.Carre(5, 5, 10)   # De (5,5) à (15,15)
    assert g.intersecte(c1, c2, "bool") == True

    # Deux carrés loin l'un de l'autre
    c3 = g.Carre(100, 100, 10)
    assert g.intersecte(c1, c3) == False # mode par défaut

def test_intersection_cercle_rectangle():
    rect = g.Rectangle(0, 0, 10, 5) # (0,0) -> (10,5)
    
    # Cercle qui tape dans le rectangle
    cercle_in = g.Cercle(5, 2, 1)
    assert g.intersecte(rect, cercle_in) == True

    # Cercle juste à côté (à x=11, r=0.5 -> touche pas 10)
    cercle_out = g.Cercle(12, 2, 1)
    assert g.intersecte(cercle_out, rect) == False

def test_intersection_cercle_cercle():
    c1 = g.Cercle(0, 0, 5)
    c2 = g.Cercle(8, 0, 5) # Distance centres = 8, Rayons somme = 10 -> Touche
    assert g.intersecte(c1, c2) == True
    
    c3 = g.Cercle(20, 0, 5)
    assert g.intersecte(c1, c3) == False

if __name__ == "__main__":
    test_intersection_carres()
    test_intersection_cercle_rectangle()
    print("Tests intersection : OK")
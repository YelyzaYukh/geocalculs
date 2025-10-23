import geocalculs
import math



def test_perimetre_triangle():
    assert geocalculs.perimetre_triangle(3, 4, 5) == 12.0
    assert geocalculs.perimetre_triangle(2, 2, 2) == 6.0

def test_surface_triangle():
    assert math.isclose(geocalculs.surface_triangle(3, 4, 5), 6.0, rel_tol=1e-9)
    assert math.isclose(geocalculs.surface_triangle(5, 5, 8), 12.0, rel_tol=1e-9)

if __name__ == "__main__":
    test_perimetre_triangle()
    test_surface_triangle()
    print("Tous les tests unitaires sont passés avec succès !")

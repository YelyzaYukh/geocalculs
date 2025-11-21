import geocalculs
import math

def test_distance_2d_classique():
    d = geocalculs.distance_2d(0, 0, 3, 4)
    attendu = 5.0
    assert abs(d - attendu) < 1e-10, f"Distance attendue : {attendu}, obtenue : {d}"

def test_distance_2d_zero():
    d = geocalculs.distance_2d(2.5, 2.5, 2.5, 2.5)
    attendu = 0.0
    assert d == attendu, "Les deux points sont identiques, distance = 0"

def test_distance_2d_flottant():
    d = geocalculs.distance_2d(1.2, 3.4, 5.6, 7.8)
    attendu = math.sqrt((5.6 - 1.2)**2 + (7.8 - 3.4)**2)
    assert abs(d - attendu) < 1e-10, f"Distance attendue : {attendu}, obtenue : {d}"

def test_distance_2d_symetrique():
    ab = geocalculs.distance_2d(1, 2, 4, 6)
    ba = geocalculs.distance_2d(4, 6, 1, 2)
    assert ab == ba, f"La distance doit être symétrique : AB={ab}, BA={ba}"

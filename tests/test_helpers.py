import geocalculs as g

def test_orientation():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    C = g.Point(1, 2)

    # anti-horaire
    assert g.orientation(A, B, C) == 2


def test_on_segment():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    C = g.Point(2, 2)

    assert g.on_segment(A, B, C) is True


def test_aabb_contains():
    A = g.Point(0, 0)
    B = g.Point(4, 4)
    box = g.AABB(A, B)

    P_inside = g.Point(2, 1)
    P_outside = g.Point(10, 10)

    assert box.contains(P_inside)
    assert not box.contains(P_outside)

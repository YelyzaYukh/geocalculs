    # pytest: skip
    import geocalculs as g

    def test_orientation():
        print("\n=== TEST ORIENTATION ===")
        x1, y1 = map(float, input("Point A (x y): ").split())
        x2, y2 = map(float, input("Point B (x y): ").split())
        x3, y3 = map(float, input("Point C (x y): ").split())

        A = g.Point(x1, y1)
        B = g.Point(x2, y2)
        C = g.Point(x3, y3)

        result = g.orientation(A, B, C)
        print("Résultat orientation :", result)
        if result == 0:
            print("→ Colinéaire")
        elif result == 1:
            print("→ Horaire (clockwise)")
        else:
            print("→ Anti-horaire (counter-clockwise)")


    def test_on_segment():
        print("\n=== TEST ON_SEGMENT ===")
        A = g.Point(*map(float, input("Point A (x y): ").split()))
        B = g.Point(*map(float, input("Point B (x y): ").split()))
        C = g.Point(*map(float, input("Point C (x y): ").split()))

        print("C est sur AB :", g.on_segment(A, B, C))


    def test_aabb():
        print("\n=== TEST AABB ===")
        A = g.Point(*map(float, input("Point A (x y): ").split()))
        B = g.Point(*map(float, input("Point B (x y): ").split()))

        box = g.AABB(A, B)

        print(f"AABB = min({box.min_x}, {box.min_y}), max({box.max_x}, {box.max_y})")

        P = g.Point(*map(float, input("Point à tester P (x y): ").split()))
        print("P est dans la box :", box.contains(P))


    def menu():
        while True:
            print("\n====== MENU TEST MANUEL ======")
            print("1 - Tester orientation")
            print("2 - Tester on_segment")
            print("3 - Tester AABB")
            print("0 - Quitter")

            choice = input("Choix : ")

            if choice == "1":
                test_orientation()
            elif choice == "2":
                test_on_segment()
            elif choice == "3":
                test_aabb()
            elif choice == "0":
                break
            else:
                print("Choix invalide.")


    if __name__ == "__main__":
        menu()

"""
Phuvisa Chotphan
683040157-7
P1
"""

from rooms import Bedroom, Kitchen

def main():
    # Test Bedroom
    bedroom = Bedroom(length=12, width=10, bed_size=5)
    print(bedroom.describe_room())
    print("Bed size (ft):", bedroom.bed_size)
    print("Area:", bedroom.calculate_area(), "sq ft")
    print("Recommended lighting:", bedroom.get_recommended_lighting(), "lumens/sq ft")
    print()

    # Test Kitchen with island
    kitchen1 = Kitchen(length=15, width=12)
    print(kitchen1.describe_room())
    print("Has island:", kitchen1.has_island)
    island, wall = kitchen1.calculate_counter_space()
    print("Island counter area:", island, "sq ft")
    print("Wall counter area:", wall, "sq ft")
    print("Recommended lighting:", kitchen1.get_recommended_lighting(), "lumens/sq ft")
    print()

    # Test Kitchen without island
    kitchen2 = Kitchen(length=15, width=12, has_island=False)
    print(kitchen2.describe_room())
    print("Has island:", kitchen2.has_island)
    island, wall = kitchen2.calculate_counter_space()
    print("Island counter area:", island, "sq ft")
    print("Wall counter area:", wall, "sq ft")
    print("Recommended lighting:", kitchen2.get_recommended_lighting(), "lumens/sq ft")


if __name__ == "__main__":
    main()


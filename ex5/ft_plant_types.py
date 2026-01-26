#! python3

class Plant:
    """Base Plant class."""
    def __init__(self, name: str, start_age: int, start_height: int) -> None:
        """Initialize Plant with name, starting age, and starting height."""
        self.name = name
        self.age = start_age
        self.height = start_height

    def grow(self, amount=1) -> None:
        """Increase the height of the plant by a given amount."""
        self.height += amount

    def age_by(self, day_count=1) -> None:
        """Increase the age of the plant by a given number of days."""
        self.age += day_count

    def show(self) -> str:
        return f'{self.name}'


class Flower(Plant):
    """Flower class inheriting from Plant."""
    def __init__(self, name: str, height: int, age: int, color_attribute: str):
        """Initialize Flower with name, height, age, and color attribute."""
        super().__init__(name, height, age)
        self.color_attribute = color_attribute

    def bloom(self) -> None:
        """Simulate the blooming of the flower."""
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> str:
        """Display information about the flower."""
        return f"{super().show()} (Flower): {self.height}cm, " +\
               f"{self.age} days, {self.color_attribute} color"


class Tree(Plant):
    """Tree class inheriting from Plant."""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize Tree with name, height, age, and trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Simulate the production of shade by the tree."""
        print(f"{self.name} provides " +
              f"{int(self.trunk_diameter/100 * 8.6 * self.height/100)} " +
              "square meters of shade")

    def show(self) -> str:
        """Display information about the tree."""
        return f"{super().show()} (Tree): {self.height}cm, {self.age} days," +\
               f" {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Vegetable class inheriting from Plant."""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutitional_value: int):
        """Initialize Vegetable with name, height, age, harvest season, and
         nutritional value."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutitional_value = nutitional_value

    def nutrition(self) -> None:
        """Display the nutritional value of the vegetable."""
        word = "poor"
        if (self.nutitional_value > 10):
            word = "rich"
        print(f"{self.name} is {word} in vitamin C")

    def show(self) -> str:
        """Display information about the vegetable."""
        return f"{super().show()} (Vegetable): {self.height}cm, " +\
               f"{self.age} days, {self.harvest_season} summer"


def ft_plant_types() -> None:
    """Demonstrate the Plant types: Flower, Tree, and Vegetable."""
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    print(flower1.show())
    flower1.bloom()
    print("")
    flower2 = Flower("Lily", 35, 15, "white")
    print(flower2.show())
    flower2.bloom()
    print("\n----------------------------------------\n")
    tree1 = Tree("Oak", 500, 1825, 50)
    print(tree1.show())
    tree1.produce_shade()
    print("")
    tree2 = Tree("Pine", 300, 1200, 40)
    print(tree2.show())
    tree2.produce_shade()
    print("\n----------------------------------------\n")
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", 17)
    print(vegetable1.show())
    vegetable1.nutrition()
    print("")
    vegetable2 = Vegetable("Carrot", 30, 120, "autumn", 6)
    print(vegetable2.show())
    vegetable2.nutrition()


if __name__ == "__main__":
    ft_plant_types()
    print("=== End of Program ===")

#! python3

class Plant:
    def __init__(self, name: str, start_age: int, start_height: int) -> None:
        self.name = name
        self.age = start_age
        self.height = start_height

    def grow(self, amount=1) -> None:
        self.height += amount

    def age_by(self, day_count=1) -> None:
        self.age += day_count


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color_attribute: str):
        super().__init__(name, height, age)
        self.color_attribute = color_attribute

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days," +
              f" {self.color_attribute} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides " +
              f"{int(self.trunk_diameter/100 * 8.6 * self.height/100)} " +
              "square meters of shade")

    def show(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days," +
              f" {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutitional_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutitional_value = nutitional_value

    def nutrition(self) -> None:
        word = "poor"
        if (self.nutitional_value > 10):
            word = "rich"
        print(f"{self.name} is {word} in vitamin C")

    def show(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days," +
              f" {self.harvest_season} summer")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("Rose", 25, 30, "red")
    flower1.show()
    flower1.bloom()
    print("")
    flower2 = Flower("Lily", 35, 15, "white")
    flower2.show()
    flower2.bloom()
    print("\n----------------------------------------\n")
    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.show()
    tree1.produce_shade()
    print("")
    tree2 = Tree("Pine", 300, 1200, 40)
    tree2.show()
    tree2.produce_shade()
    print("\n----------------------------------------\n")
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", 17)
    vegetable1.show()
    vegetable1.nutrition()
    print("")
    vegetable2 = Vegetable("Carrot", 30, 120, "autumn", 6)
    vegetable2.show()
    vegetable2.nutrition()


ft_plant_types()

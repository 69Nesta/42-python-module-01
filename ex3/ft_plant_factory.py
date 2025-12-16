#! python3

class Plant:
    def __init__(self, name, start_age, start_height) -> None:
        self.name = name
        self.age = start_age
        self.height = start_height


class Factory:
    def __init__(self):
        self.plant_created = 0

    def create_plant(self, name, start_age, start_height):
        plant = Plant(name, start_age, start_height)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        self.plant_created += 1

    def get_total_created(self) -> int:
        return self.plant_created


def plant_factory():
    factory = Factory()

    print("=== Plant Factory Output ===")
    factory.create_plant("Rpse", 30, 25)
    factory.create_plant("Oak", 365, 200)
    factory.create_plant("Cactus", 90, 5)
    factory.create_plant("Sunflower", 80, 80)
    factory.create_plant("Fern", 120, 15)
    print(f"\nTotal plants created: {factory.get_total_created()}")


plant_factory()

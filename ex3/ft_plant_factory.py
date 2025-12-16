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


class Factory:
    def __init__(self):
        self.plant_created = 0

    def create_plant(self, name, age, height):
        plant = Plant(name, 1, 1)
        plant.grow(height - 1)
        plant.age_by(age - 1)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        self.plant_created += 1

    def get_total_created(self) -> int:
        return self.plant_created


def plant_factory():
    factory = Factory()

    print("=== Plant Factory Output ===")
    factory.create_plant("Rose", 30, 25)
    factory.create_plant("Oak", 365, 200)
    factory.create_plant("Cactus", 90, 5)
    factory.create_plant("Sunflower", 80, 80)
    factory.create_plant("Fern", 120, 15)
    print(f"\nTotal plants created: {factory.get_total_created()}")


plant_factory()

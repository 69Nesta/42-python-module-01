#! python3

class Plant:
    """Base Plant class."""
    def __init__(self, name: str, start_age: int, start_height: int) -> None:
        """Initialize Plant with name, starting age, and starting height."""
        self.name = name
        self.age = start_age
        self.height = start_height

    def grow(self, amount=1) -> None:
        """Increase the height of the plant by the specified amount."""
        self.height += amount

    def age_by(self, day_count=1) -> None:
        """Increase the age of the plant by the specified number of days."""
        self.age += day_count


class Factory:
    """Factory class to create Plant instances and track total created."""
    def __init__(self):
        """Initialize Factory with a counter for created plants."""
        self.plant_created = 0

    def create_plant(self, name, age, height) -> Plant:
        """Create a Plant instance with given name, age, and height."""
        plant = Plant(name, 1, 1)
        plant.grow(height - 1)
        plant.age_by(age - 1)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        self.plant_created += 1
        return (plant)

    def get_total_created(self) -> int:
        """Get the total number of plants created by the factory."""
        return self.plant_created


def plant_factory():
    """Demonstrate the Factory class by creating various Plant instances."""
    factory = Factory()

    print("=== Plant Factory Output ===")
    factory.create_plant("Rose", 30, 25)
    factory.create_plant("Oak", 365, 200)
    factory.create_plant("Cactus", 90, 5)
    factory.create_plant("Sunflower", 80, 80)
    factory.create_plant("Fern", 120, 15)
    print(f"\nTotal plants created: {factory.get_total_created()}")


if __name__ == "__main__":
    plant_factory()

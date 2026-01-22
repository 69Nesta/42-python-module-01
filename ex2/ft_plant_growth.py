#! python3

class Plant:
    """Plant class to simulate growth over time."""
    def __init__(
                self,
                name: str,
                height: int,
                age: int,
                grow_speed: int
            ) -> None:
        """Initialize Plant with name, height, age, and growth speed."""
        self.name = name
        self.height = height
        self.height_start = height
        self._age = age
        self.grow_speed = grow_speed

    def grow(self, amount=1) -> None:
        """Increase the height of the plant by a given amount."""
        self.height += amount

    def age(self, day_count=1) -> None:
        """Increase the age of the plant by a given number of days and grow
         accordingly."""
        self._age += day_count
        self.grow(day_count * self.grow_speed)

    def show(self) -> None:
        """Display the current state of the plant."""
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def get_info(self) -> int:
        """Get the growth of the plant since initialization."""
        return (self.height - self.height_start)


def main() -> None:
    """Demonstrate the Plant class growth over a week."""
    plant = Plant("Rose", 25, 30, 1)
    print("=== Day 1 ===")
    plant.show()
    plant.age(6)
    print("=== Day 7 ===")
    plant.show()
    print(f"Growth this week: +{plant.get_info()}cm")


if __name__ == "__main__":
    main()

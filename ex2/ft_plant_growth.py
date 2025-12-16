#! python3

class Plant:
    def __init__(self, name: str, height: int, age: int, grow_speed: int):
        self.name = name
        self.height = height
        self.height_start = height
        self._age = age
        self.grow_speed = grow_speed

    def grow(self, amount=1) -> None:
        self.height += amount

    def age(self, day_count=1) -> None:
        self._age += day_count
        self.grow(day_count * self.grow_speed)

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self._age} days old")

    def get_info(self) -> int:
        return (self.height - self.height_start)


def main() -> None:
    plant = Plant("Rose", 25, 30, 1)
    print("=== Day 1 ===")
    plant.show()
    plant.age(6)
    print("=== Day 7 ===")
    plant.show()
    print(f"Growth this week: +{plant.get_info()}cm")


main()

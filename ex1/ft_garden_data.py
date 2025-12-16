#! python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 40).show()
    Plant("Cactus", 15, 120).show()


print("===  Garden Plant Registry  ===")
main()
print("=== End of Program ===")

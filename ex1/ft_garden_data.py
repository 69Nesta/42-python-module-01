#! python3

class Plant:
    """Simple Plant class."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Display the plant's information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Create and display plants in the garden."""
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 40).show()
    Plant("Cactus", 15, 120).show()


if __name__ == "__main__":
    print("===  Garden Plant Registry  ===")
    main()
    print("=== End of Program ===")

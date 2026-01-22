#! python3

class SecurePlant:
    """Plant class with security checks for age and height."""
    def __init__(self, name, height, age):
        print(f"Plant created: {name}")
        self.name = name
        self.__age = 0
        self.set_age(age)
        self.__height = 0
        self.set_height(height)

    def set_age(self, age):
        """Set the age of the plant with validation."""
        if (age < 0):
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print('Security: negative age rejected')
        else:
            print(f"Age updated: {age} [OK]")
            self.__age = age

    def set_height(self, height):
        """Set the height of the plant with validation."""
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print('Security: negative height rejected')
        else:
            print(f"Height updated: {height}cm [OK]")
            self.__height = height

    def get_age(self) -> int:
        """Get the age of the plant."""
        return (self.__age)

    def get_height(self) -> int:
        """Get the height of the plant."""
        return (self.__height)


def ft_garden_security() -> None:
    """Demonstrate the SecurePlant class with security checks."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print('')
    plant.set_height(-5)
    print('')
    print(f"Current plant: {plant.name} ({plant.get_height()}cm" +
          f", {plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()

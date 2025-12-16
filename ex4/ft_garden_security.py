#! python3

class SecurePlant:
    def __init__(self, name, height, age):
        print(f"Plant created: {name}")
        self.name = name
        self.__age = 0
        self.set_age(age)
        self.__height = 0
        self.set_height(height)

    def set_age(self, age):
        if (age < 0):
            print(f"Invalid operation attempted: age {age} [REJECTED]")
        else:
            print(f"Age updated: {age} [OK]")
            self.__age = age

    def set_height(self, height):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
        else:
            print(f"Height updated: {height}cm [OK]")
            self.__height = height

    def get_age(self) -> int:
        return (self.__age)

    def get_height(self) -> int:
        return (self.__height)


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", -25, -30)
    plant.set_height(-5)
    print(f"Current plant: {plant.name} ({plant.get_height()}cm" +
          f", {plant.get_age()} days)")


ft_garden_security()

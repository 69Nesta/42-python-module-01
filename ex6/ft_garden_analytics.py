#! python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.type = 'regular'
        self.set_name(name)
        self.set_height(height)
        self.grow = 0

    def set_name(self, name: str) -> None:
        if (name):
            self.name = name.title()

    def get_name(self) -> str:
        return self.name

    def set_height(self, height: int) -> None:
        self.height = height

    def get_height(self) -> int:
        return self.height + self.get_grow()

    def get_plant(self) -> str:
        return f'{self.name}: {self.get_height()}cm'

    def grow(self, grow=1) -> None:
        self.grow += grow
        print(f'{self.name} grew {grow}cm')

    def get_grow(self) -> int:
        return self.grow

    def get_type(self) -> str:
        return self.type


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.type = 'flowering'
        self.blooming = True

    def set_color(self, color: str) -> None:
        if (color):
            self.color = color.lower()

    def toggle_blooming(self):
        self.blooming = not self.blooming

    def get_plant(self):
        return super().get_plant() + f', {self.color} flowers{
            ' (blooming)' if self.blooming else ''}'


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.type = 'prize flowers'
        self.prize = prize

    def get_prize(self, prize) -> None:
        self.prize = prize

    def get_plant(self):
        return super().get_plant() + f', Prize Points: {self.prize}'


class GardenManager:
    def __init__(self):
        #
        print("Hello")

    def create_garden_network():
        print("")


class Garden:
    def __init__(self, name: str) -> None:
        self.set_name(name)
        self.plants: list[Plant | FloweringPlant | PrizeFlower] = []

    def set_name(self, name: str) -> None:
        if (name):
            self.name = name.title()

    def get_name(self) -> str:
        return self.name

    def add(self, plant: Plant | FloweringPlant | PrizeFlower) -> None:
        print(f'Added {plant.get_name()} to {self.get_name()}\'s garden')
        self.plants.append(plant)

    def grow(self, grow=1) -> None:
        print(f'{self.get_name()} is helping all plants grow...')
        for plant in self.plants:
            plant.grow(grow)

    # def garden_stats()
    # def get_score()


if __name__ == '__main__':
    print(FloweringPlant("Hello", "red").type)

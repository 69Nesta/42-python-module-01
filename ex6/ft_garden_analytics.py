#! python3

class GardenManager:
    def __init__(self):
        #
        print("Hello")

    def create_garden_network():
        print("")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []

    # def add(self, ):
        # print("Adding plant")

    # def garden_stats()
    # def get_score()


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.type = 'regular'
        self.set_name(name)
        self.set_height(height)
        self.grow = 0

    def set_name(self, name: str) -> None:
        if (name):
            self.name = name.title()

    def set_height(self, height: int) -> None:
        self.height = height

    def get_height(self) -> int:
        return self.height + self.get_grow()

    def get_plant(self) -> str:
        return f'{self.name}: {self.get_height()}cm'

    def grow(self, grow: int) -> None:
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
        self.blooming = False

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


if __name__ == '__main__':
    print(FloweringPlant("Hello", "red").type)

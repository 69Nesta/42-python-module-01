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

    def add(self, ):
        print("Adding plant")

    # def garden_stats()
    # def get_score()


class Plant:
    def __init__(self, name: str):
        self.type = 'regular'
        self.set_name(name)

    def set_name(self, name: str):
        if (name):
            self.name = name


class FloweringPlant(Plant):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.type = "flowering"

    def set_color(self, color: str):
        if (color):
            self.color = color


if __name__ == '__main__':
    print(FloweringPlant("Hello", "red").type)

#! python3

class Utility:
    @staticmethod
    def name_to_id(name: str):
        return name.lower().replace(' ', '_')

    @staticmethod
    def print_error(str: str):
        print("Error: " + str)

    @staticmethod
    def format_dict_int(values: dict[str, int]) -> str:
        formatted = ''
        index = 0
        for k, v in values.items():
            if index != 0:
                formatted += ', '
            index += 1
            formatted += f'{v} {k}'
        return formatted


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self._type = 'regular'
        self.set_name(name)
        self.set_height(height)
        self._grow = 0

    def set_name(self, name: str) -> None:
        if (name):
            self._name = name.title()

    def get_name(self) -> str:
        return self._name

    def set_height(self, height: int) -> None:
        if (height >= 0):
            self._height = height
        else:
            Utility.print_error('Height can\'t be negaive !')

    def get_height(self) -> int:
        return self._height + self.get_grow()

    def height_validation(self) -> bool:
        return self.get_grow() + self._height == self.get_height()

    def get_plant(self) -> str:
        return f'{self._name}: {self.get_height()}cm'

    def grow(self, grow=1) -> None:
        self._grow += grow
        print(f'{self._name} grew {grow}cm')

    def get_grow(self) -> int:
        return self._grow

    def get_type(self) -> str:
        return self._type


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self._type = 'flowering'
        self._blooming = True
        self.set_color(color)

    def set_color(self, color: str) -> None:
        if (color):
            self.color = color.lower()

    def toggle_blooming(self):
        self._blooming = not self._blooming

    def get_blooming(self) -> bool:
        return self._blooming

    def get_plant(self):
        blooming = ' (blooming)' if self._blooming else ''
        return super().get_plant() + f', {self.color} flowers{blooming}'


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self._type = 'prize flowers'
        self.set_prize(prize)

    def set_prize(self, prize) -> None:
        self._prize = prize

    def get_prize(self) -> int:
        return self._prize

    def get_plant(self):
        return super().get_plant() + f', Prize Points: {self._prize}'


class Garden:
    def __init__(self, name: str) -> None:
        self.set_name(name)
        self._plants: list[Plant | FloweringPlant | PrizeFlower] = []

    def set_name(self, name: str) -> None:
        if (name and not name.isspace()):
            self._name = name.title()

    def get_name(self) -> str:
        return self._name

    def get_plants(self):
        return self._plants

    def add(self, plant: Plant | FloweringPlant | PrizeFlower) -> None:
        print(f'Added {plant.get_name()} to {self.get_name()}\'s garden')
        self._plants.append(plant)

    def grow(self, grow=1) -> None:
        print(f'{self.get_name()} is helping all plants grow...')
        for plant in self._plants:
            plant.grow(grow)

    def get_growth(self) -> int:
        total_growth = 0
        for plant in self._plants:
            total_growth += plant.get_grow()
        return total_growth

    def get_types(self) -> dict[str, int]:
        types: dict[str, int] = {}
        for plant in self._plants:
            if (not types.get(plant.get_type())):
                types[plant.get_type()] = 1
            else:
                types[plant.get_type()] += 1
        return types

    def height_validation(self) -> str:
        for plant in self.get_plants():
            if (not plant.height_validation()):
                return ('False')
        return ('True')

    def get_score(self) -> int:
        score = 0
        for plant in self.get_plants():
            score += plant.get_height()
            if (hasattr(plant, 'get_blooming') and plant.get_blooming()):
                score += 5
            if (hasattr(plant, 'get_prize')):
                score += plant.get_prize() * 3
        return score

    def print_stats(self) -> None:
        print(f'Plants added: {len(self._plants)}, '
              f'Total growth: {self.get_growth()}cm')
        print(f'Plants types: {Utility.format_dict_int(self.get_types())}')

    def print_plants(self) -> None:
        print(f'Plant{'s' if len(self.get_plants()) else ''} in garden:')
        for plant in self.get_plants():
            print(f'- {plant.get_plant()}')

    def print_report(self) -> None:
        print(f'=== {self.get_name()} Garden Report ===')
        self.print_plants()
        print('')
        self.print_stats()
        print('')
        print(f'Height validation test: {self.height_validation()}')


class GardenManager:
    def __init__(self):
        self._network: dict[str, Garden] = {}

    def create_garden_network(self, name) -> Garden:
        id = Utility.name_to_id(name)
        if (self._network.get(id)):
            return Utility.print_error("Name already taken!")
        self._network[id] = Garden(name)
        return self._network[id]

    def get_garden(self, name) -> Garden:
        id = Utility.name_to_id(name)
        if (not self._network.get(id)):
            return Utility.print_error("Unknown garden!")
        return self._network[id]

    def del_garden(self, name) -> None:
        id = Utility.name_to_id(name)
        if (not self._network.get(id)):
            return Utility.print_error("Unknown garden!")
        del self._network[id]

    def get_scores(self) -> str:
        scores = ''
        index = 0
        for k, v in self._network.items():
            if (index != 0):
                scores += ', '
            index += 1
            scores += f'{v.get_name()} {v.get_score()}'
        return scores

    def print_stats(self) -> None:
        print(f'Gardens Score - {self.get_scores()}')
        print(f'Total gardens managed: {len(self._network)}')


def ft_garden_analytics():
    print('=== Garden Management System Demo ===\n')
    garden_manager = GardenManager()
    garden_manager.create_garden_network('aLicE')
    bob_garden = garden_manager.create_garden_network('bOb')
    bob_garden.add(Plant('Poppies', 10))
    print('')
    alice_garden = garden_manager.get_garden('AliCe')
    alice_garden.add(Plant('oaK tRee', 100))
    alice_garden.add(FloweringPlant('rosE', 25, 'red'))
    alice_garden.add(PrizeFlower('sunFlower', 50, 'yellow', 10))
    print('')
    alice_garden.grow()
    print('')
    alice_garden.print_report()
    garden_manager.print_stats()


if __name__ == '__main__':
    ft_garden_analytics()

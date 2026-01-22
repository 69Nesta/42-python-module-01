#! python3

class Utility:
    '''Utility class for common helper methods.'''
    @staticmethod
    def name_to_id(name: str) -> str:
        '''Convert a name to a standardized ID format.'''
        return name.lower().replace(' ', '_')

    @staticmethod
    def print_error(str: str) -> None:
        '''Print an error message and return None.'''
        print("Error: " + str)

    @staticmethod
    def format_dict_int(values: dict[str, int]) -> str:
        '''Format a dictionary of string keys and integer values into a
        readable string.'''
        formatted = ''
        index = 0
        for k, v in values.items():
            if index != 0:
                formatted += ', '
            index += 1
            formatted += f'{v} {k}'
        return formatted


class Plant:
    '''Base class for plants in the garden.'''
    def __init__(self, name: str, height: int) -> None:
        '''Initialize a Plant with a name and height.'''
        self._type = 'regular'
        self.set_name(name)
        self.set_height(height)
        self._grow = 0

    def set_name(self, name: str) -> None:
        '''Set the name of the plant, capitalizing each word.'''
        if (name):
            self._name = name.title()

    def get_name(self) -> str:
        '''Get the name of the plant.'''
        return self._name

    def set_height(self, height: int) -> None:
        '''Set the initial height of the plant.'''
        if (height >= 0):
            self._height = height
        else:
            Utility.print_error('Height can\'t be negaive !')

    def get_height(self) -> int:
        '''Get the current height of the plant, including growth.'''
        return self._height + self.get_grow()

    def height_validation(self) -> bool:
        '''Validate if the current height matches initial height plus
        growth.'''
        return self.get_grow() + self._height == self.get_height()

    def get_plant(self) -> str:
        '''Get a string representation of the plant.'''
        return f'{self._name}: {self.get_height()}cm'

    def grow(self, grow=1) -> None:
        '''Increase the growth of the plant by a specified amount.'''
        self._grow += grow
        print(f'{self._name} grew {grow}cm')

    def get_grow(self) -> int:
        '''Get the total growth of the plant.'''
        return self._grow

    def get_type(self) -> str:
        '''Get the type of the plant.'''
        return self._type


class FloweringPlant(Plant):
    '''Class representing a flowering plant.'''
    def __init__(self, name: str, height: int, color: str) -> None:
        '''Initialize a FloweringPlant with a name, height,
        and flower color.'''
        super().__init__(name, height)
        self._type = 'flowering'
        self._blooming = True
        self.set_color(color)

    def set_color(self, color: str) -> None:
        '''Set the color of the flowers.'''
        if (color):
            self.color = color.lower()

    def toggle_blooming(self):
        '''Toggle the blooming state of the plant.'''
        self._blooming = not self._blooming

    def get_blooming(self) -> bool:
        '''Get the blooming state of the plant.'''
        return self._blooming

    def get_plant(self):
        '''Get a string representation of the flowering plant.'''
        blooming = ' (blooming)' if self._blooming else ''
        return super().get_plant() + f', {self.color} flowers{blooming}'


class PrizeFlower(FloweringPlant):
    '''Class representing a prize flower with additional prize points.'''
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        '''Initialize a PrizeFlower with a name, height, color,
        and prize points.'''
        super().__init__(name, height, color)
        self._type = 'prize flowers'
        self.set_prize(prize)

    def set_prize(self, prize) -> None:
        '''Set the prize points for the prize flower.'''
        self._prize = prize

    def get_prize(self) -> int:
        '''Get the prize points of the prize flower.'''
        return self._prize

    def get_plant(self):
        '''Get a string representation of the prize flower.'''
        return super().get_plant() + f', Prize Points: {self._prize}'


class Garden:
    '''Class representing a garden containing various plants.'''
    def __init__(self, name: str) -> None:
        '''Initialize a Garden with a name and an empty list of plants.'''
        self.set_name(name)
        self._plants: list[Plant | FloweringPlant | PrizeFlower] = []

    def set_name(self, name: str) -> None:
        '''Set the name of the garden, capitalizing each word.'''
        if (name and not name.isspace()):
            self._name = name.title()

    def get_name(self) -> str:
        '''Get the name of the garden.'''
        return self._name

    def get_plants(self):
        '''Get the list of plants in the garden.'''
        return self._plants

    def add(self, plant: Plant | FloweringPlant | PrizeFlower) -> None:
        '''Add a plant to the garden.'''
        print(f'Added {plant.get_name()} to {self.get_name()}\'s garden')
        self._plants.append(plant)

    def grow(self, grow=1) -> None:
        '''Help all plants in the garden grow by a specified amount.'''
        print(f'{self.get_name()} is helping all plants grow...')
        for plant in self._plants:
            plant.grow(grow)

    def get_growth(self) -> int:
        '''Get the total growth of all plants in the garden.'''
        total_growth = 0
        for plant in self._plants:
            total_growth += plant.get_grow()
        return total_growth

    def get_types(self) -> dict[str, int]:
        '''Get a dictionary of plant types and their counts in the garden.'''
        types: dict[str, int] = {}
        for plant in self._plants:
            if (not types.get(plant.get_type())):
                types[plant.get_type()] = 1
            else:
                types[plant.get_type()] += 1
        return types

    def height_validation(self) -> str:
        '''Validate the height of all plants in the garden.'''
        for plant in self.get_plants():
            if (not plant.height_validation()):
                return ('False')
        return ('True')

    def get_score(self) -> int:
        '''Calculate the score of the garden based on plant attributes.'''
        score = 0
        for plant in self.get_plants():
            score += plant.get_height()
            if (hasattr(plant, 'get_blooming') and plant.get_blooming()):
                score += 5
            if (hasattr(plant, 'get_prize')):
                score += plant.get_prize() * 3
        return score

    def print_stats(self) -> None:
        '''Print statistics about the plants in the garden.'''
        print(f'Plants added: {len(self._plants)}, '
              f'Total growth: {self.get_growth()}cm')
        print(f'Plants types: {Utility.format_dict_int(self.get_types())}')

    def print_plants(self) -> None:
        '''Print the list of plants in the garden.'''
        print(f'Plant{"s" if len(self.get_plants()) else ""} in garden:')
        for plant in self.get_plants():
            print(f'- {plant.get_plant()}')

    def print_report(self) -> None:
        '''Print a comprehensive report of the garden.'''
        print(f'=== {self.get_name()} Garden Report ===')
        self.print_plants()
        print('')
        self.print_stats()
        print('')
        print(f'Height validation test: {self.height_validation()}')


class GardenManager:
    '''Class to manage multiple gardens.'''
    class GardenStats:
        @staticmethod
        def get_scores(gardens: dict[str, Garden]) -> str:
            '''Get a string representation of the scores of all gardens.'''
            scores = ''
            index = 0
            for k, v in gardens.items():
                if (index != 0):
                    scores += ', '
                index += 1
                scores += f'{v.get_name()} {v.get_score()}'
            return scores

        @staticmethod
        def get_total_score(gardens: dict[str, Garden]) -> int:
            '''Get the total score of all gardens in the network.'''
            total_score = 0
            for garden in gardens.values():
                total_score += garden.get_score()
            return total_score

        @staticmethod
        def print_stats(gardens: dict[str, Garden]) -> None:
            '''Print statistics about all gardens in the network.'''
            print(f'Gardens Score - {__class__.get_scores(gardens)}')
            print(f'Total gardens score: {__class__.get_total_score(gardens)}')
            print('Total plants managed: ' +
                  f'{sum(len(g.get_plants()) for g in gardens.values())}')
            print(f'Total gardens managed: {len(gardens)}')

    def __init__(self) -> None:
        '''Initialize a GardenManager with an empty network of gardens.'''
        self._network: dict[str, Garden] = {}

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        '''Create a new garden network manager.'''
        print('Creating garden network...\n')
        return cls()

    def create_garden(self, name) -> Garden | None:
        '''Create a new garden in the network.'''
        id = Utility.name_to_id(name)
        if (self._network.get(id)):
            return Utility.print_error("Name already taken!")
        self._network[id] = Garden(name)
        return self._network[id]

    def get_garden(self, name) -> Garden | None:
        '''Retrieve a garden from the network by name.'''
        id = Utility.name_to_id(name)
        if (not self._network.get(id)):
            return Utility.print_error("Unknown garden!")
        return self._network[id]

    def get_gardens(self) -> dict[str, Garden]:
        '''Retrieve all gardens in the network.'''
        return self._network

    def del_garden(self, name) -> None:
        '''Delete a garden from the network by name.'''
        id = Utility.name_to_id(name)
        if (not self._network.get(id)):
            return Utility.print_error("Unknown garden!")
        del self._network[id]


def ft_garden_analytics(): 
    '''Demo function for the Garden Management System.'''
    print('=== Garden Management System Demo ===\n')
    garden_manager = GardenManager.create_garden_network()
    garden_manager.create_garden('aLicE')
    bob_garden = garden_manager.create_garden('bOb')
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
    garden_manager.GardenStats.print_stats(garden_manager.get_gardens())


if __name__ == '__main__':
    ft_garden_analytics()

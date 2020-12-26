import random


class World:
    def __init__(self, size=20):
        self.size = size
        # GENETIC PARAMETERS
        self.population_size = 20
        self.minimal_resources = 45

        self.create_grid()
        self.create_tiles()

        # self.add_generation()
        # self.select_fittest()
        #

    @property
    def score(self):
        import types

        score = types.SimpleNamespace()
        score.population_count = len(self.population)
        score.total_resources = sum(x.area_resources for x in self.population)
        if self.population:
            score.max_resources = max(tile.area_resources for tile in self.population)
        else:
            score.max_resources = 0

        score.possible_max_resources = max(tile.area_resources for tile in self.tiles)
        return score

    @property
    def tiles(self):
        tiles = [item for sublist in self.grid for item in sublist]
        return tiles

    @property
    def population(self):
        return [tile for tile in self.tiles if tile.human]

    def create_grid(self):
        self.grid = [[None for i in range(self.size)] for j in range(self.size)]

    def create_tiles(self):
        from .tiles import tiles

        self.grid = [
            [random.choice(tiles)(i + 1, j + 1, self) for i in range(self.size)]
            for j in range(self.size)
        ]

    @property
    def html(self):
        html = "<table>"
        for row in range(self.size):
            html += "<tr>"
            for column in range(self.size):
                html += self.grid[row][column].html

            html += "</tr>"

        html += "</table>"
        return html

    def random_tile(self):
        return self.grid[random.randint(0, self.size - 1)][
            random.randint(0, self.size - 1)
        ]

    def add_generation(self, first=False):

        if first:
            remaining_population = self.population_size
            while remaining_population > 0:
                tile = self.random_tile()
                if tile.settleable:
                    tile.add_human()
                    remaining_population -= 1

        else:
            populations = [tile for tile in self.tiles if tile.human]
            remaining_population = self.population_size - len(populations)
            while remaining_population > 0:
                pop = random.choice(populations)
                tile = random.choice(pop.surrounding_tiles)
                if tile.settleable:
                    tile.add_human()
                    remaining_population -= 1

    def select_fittest(self):

        # kill those with not enought resources
        # populations = [tile for tile in self.tiles if tile.human]
        losers = [
            pop
            for pop in self.population
            if pop.area_resources < self.minimal_resources
        ]
        for tile in losers:
            tile.kill_human()

        # kill random part of population
        # populations = [tile for tile in self.tiles if tile.human]
        # random.shuffle(populations)
        losers = [pop for pop in random.sample(self.population, len(self.population)) if random.randint(1, 100) < 50]
        for tile in losers:
            tile.kill_human()

        # populations = [pop for pop in populations if pop.area_resources >= self.minimal_resources]
        #
        #

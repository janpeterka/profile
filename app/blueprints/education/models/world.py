import random

# from app import db

# from app.helpers.base_mixin import BaseMixin

# from .tiles import Tile


class World():
    # __tablename__ = "education_worlds"

    # id = db.Column(db.BigInteger, primary_key=True)
    # size = db.Column(db.BigInteger)
    # population_size = db.Column(db.String(255))
    # minimal_resources = db.Column(db.String(255))

    # tiles = db.relationship(
    #     "User", primaryjoin="World.id == Tile.world_id", backref="world",
    # )

    def __init__(self, size=20):
        self.size = size
        # GENETIC PARAMETERS
        self.population_size = 20
        self.minimal_resources = 30

        self.create_grid()
        self.create_tiles()

    def create_grid(self):
        self.grid = [[None for i in range(self.size)] for j in range(self.size)]

    def create_tiles(self):
        from .tiles import tiles

        self.grid = [
            [random.choice(tiles)(i + 1, j + 1, self) for i in range(self.size)]
            for j in range(self.size)
        ]

    @property
    def tiles(self):
        return [item for sublist in self.grid for item in sublist]

    @property
    def populated_tiles(self):
        return [tile for tile in self.tiles if tile.human]

    @property
    def random_tile(self):
        return self.grid[random.randint(0, self.size - 1)][
            random.randint(0, self.size - 1)
        ]

    def add_generation(self, first=False):
        """ Adds new populations """
        if first:
            remaining_population = self.population_size
            while remaining_population > 0:
                tile = self.random_tile
                if tile.settleable:
                    tile.add_human()
                    remaining_population -= 1

        else:
            populations = [
                tile for tile in self.tiles if tile.human and tile.has_settleable
            ]
            for population in random.sample(populations, len(populations)):
                if population.has_settleable:
                    # if random.random() > 0.1:
                    population.settle()

            # # remaining_population = self.population_size - len(populations)
            # while populations:
            #     pop = random.choice(populations)
            #     if not pop.surrounding_settleable_tiles:
            #         populations = [
            #             tile
            #             for tile in self.tiles
            #             if tile.human and tile.has_settleable
            #         ]
            #         continue
            #     tile = random.choice(pop.surrounding_settleable_tiles)
            #     if tile.settleable:
            #         tile.add_human()
            #         remaining_population -= 1

    def select_fittest(self):

        # kill those with not enought resources
        # populations = [tile for tile in self.tiles if tile.human]
        losers = [
            pop
            for pop in self.populated_tiles
            if pop.area_resources < self.minimal_resources
        ]
        for tile in losers:
            tile.kill_human()

        # kill random part of population
        # populations = [tile for tile in self.tiles if tile.human]
        # random.shuffle(populations)
        losers = [
            pop
            for pop in random.sample(self.populated_tiles, len(self.populated_tiles))
            if random.randint(1, 100) < 30
        ]
        for tile in losers:
            tile.kill_human()

        # populations = [pop for pop in populations if pop.area_resources >= self.minimal_resources]
        #
        #

    def mutate(self):
        # move around
        populated_tiles = [
            tile for tile in self.tiles if tile.human and tile.has_settleable
        ]

        for tile in populated_tiles:
            if tile.has_settleable and random.random() > 0.5:
                random.choice(tile.surrounding_settleable_tiles).add_human()
                tile.kill_human()

    @property
    def score(self):
        import types

        score = types.SimpleNamespace()
        score.population_count = len(self.populated_tiles)
        score.total_resources = sum(x.area_resources for x in self.populated_tiles)
        if self.populated_tiles:
            score.max_resources = max(
                tile.area_resources for tile in self.populated_tiles
            )
        else:
            score.max_resources = 0

        score.possible_max_resources = max(tile.area_resources for tile in self.tiles)
        return score

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

import random

from app import db

from app.helpers.base_mixin import BaseMixin


class Tile(db.Model, BaseMixin):
    __tablename__ = "education_tiles"

    id = db.Column(db.BigInteger, primary_key=True)
    x = db.Column(db.BigInteger)
    y = db.Column(db.BigInteger)
    world_id = db.Column(db.ForeignKey("education_worlds.id"), nullable=False)
    resources = db.Column(db.BigInteger)

    human = db.Column(db.Boolean)
    habitable = db.Column(db.Boolean)

    tile_type = db.Column(db.String(255))
    __mapper_args__ = {"polymorphic_on": tile_type, "polymorphic_identity": "tile"}

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.human = False
        self.habitable = True
        self.resources = 0
        self.cell_size = 2

    def kill_human(self):
        self.human = False

    def add_human(self):
        self.human = True

    @property
    def is_habitable(self):
        return self.habitable

    @property
    def settleable(self):
        if self.human:
            return False

        return self.is_habitable

    @property
    def has_settleable(self):
        return len(self.surrounding_settleable_tiles) > 0

    def settle(self):
        random.choice(self.surrounding_settleable_tiles).add_human()

    @property
    def area_resources(self):
        return self.resources + sum(
            tile.resources for tile in self.surrounding_tiles if tile.human is False
        )

    # @property
    # def resources(self):
    #     return math.ceil(
    #         self.resources
    #         / (len([tile for tile in self.surrounding_tiles if tile.human]) + 1)
    #     )

    @property
    def surrounding_settleable_tiles(self):
        return [tile for tile in self.surrounding_tiles if tile.settleable]

    @property
    def surrounding_tiles(self):
        surrounding_tiles = []

        grid = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, +1],
            [+1, -1],
            [+1, 0],
            [+1, +1],
        ]

        for positions in grid:
            if (
                self.x + positions[0] > 0
                and self.x + positions[0] <= self.world.size
                and self.x + positions[1] > 0
                and self.y + positions[1] <= self.world.size
            ):
                surrounding_tiles.append(
                    self.world.grid[self.y + positions[1] - 1][
                        self.x + positions[0] - 1
                    ]
                )

        return surrounding_tiles

    # HTML

    @property
    def human_class(self):
        if self.human:
            return "human"
        else:
            return ""

    @property
    def area_resources_html(self):
        if self.habitable:
            return f"{self.area_resources}"
        else:
            return ""

    @property
    def html(self):
        return f"<td class='tile {self.type} {self.human_class}' style='width: {self.cell_size}rem; height: {self.cell_size}rem;'></td>"


class WaterTile(Tile):
    __mapper_args__ = {"polymorphic_identity": "water"}

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "water"
        self.resources = random.randint(2, 7)
        self.habitable = False


class LandTile(Tile):
    __mapper_args__ = {"polymorphic_identity": "land"}

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "land"
        self.resources = random.randint(3, 10)


class RockTile(Tile):
    __mapper_args__ = {"polymorphic_identity": "rock"}

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.resources = random.randint(1, 4)


class ForrestTile(Tile):
    __mapper_args__ = {"polymorphic_identity": "forrest"}

    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "forrest"
        self.resources = random.randint(3, 8)


tiles = [WaterTile, LandTile, RockTile, ForrestTile]

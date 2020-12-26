import random


class Tile:
    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.human = False
        self.resources = 0
        self.cell_size = 2

    def kill_human(self):
        self.human = False

    def add_human(self):
        self.human = True

    @property
    def habitable(self):
        if self.type == "water":
            return False

        return True

    @property
    def settleable(self):
        if self.human:
            return False

        return self.habitable

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
        # return self._area_resources_html

    @property
    def html(self):
        return f"<td class='tile {self.type} {self.human_class}' style='width: {self.cell_size}rem; height: {self.cell_size}rem;'>{self.area_resources_html}</td>"

    @property
    def area_resources(self):
        return self.resources + sum(tile.resources for tile in self.surrounding_tiles)

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


class WaterTile(Tile):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "water"
        self.resources = random.randint(2, 7)


class LandTile(Tile):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "land"
        self.resources = random.randint(3, 10)


class RockTile(Tile):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "rock"
        self.resources = random.randint(1, 4)


class ForrestTile(Tile):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.type = "forrest"
        self.resources = random.randint(3, 8)


tiles = [WaterTile, LandTile, RockTile, ForrestTile]

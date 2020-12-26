class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def html(self):
        return (
            f"<td class='tile {self.type}' style='width: 2rem; height: 2rem;'></td>"
        )


class WaterTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "water"


class LandTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "land"


class RockTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "rock"


class ForrestTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = "forrest"


tiles = [WaterTile, LandTile, RockTile, ForrestTile]

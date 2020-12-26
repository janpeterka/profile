import random


class World:
    def __init__(self, size=20):
        self.size = size
        self.create_grid()
        self.fill_grid()

    def create_grid(self):
        self.grid = [[None for i in range(self.size)] for j in range(self.size)]

    def fill_grid(self):
        from .tiles import tiles

        self.grid = [
            [random.choice(tiles)(i, j) for i in range(self.size)] for j in range(self.size)
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
        print(html)
        return html

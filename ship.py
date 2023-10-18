import json


class Ship:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def is_sunk(self, grid):
        for i in range(self.size):
            if grid[self.y][self.x + i] != "X":
                return False
        return True

    def display(self, grid):
        for i in range(self.size):
            grid[self.y][self.x + i] = "*"

    def get_coord_all(self):
        coord = []
        for i in range(self.size):
            coord.append((self.x + i, self.y))
        return coord


class ShipEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

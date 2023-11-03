from json import JSONEncoder


class Ship:
    def __init__(self, x, y, size, orientation):
        self.x = x
        self.y = y
        self.size = size
        self.orientation = orientation

    def is_sunk(self, grid):
        for i in range(self.size):
            if grid[self.y][self.x + i] != "X":
                return False
        return True

    def display(self, grid):
        if self.orientation == "v":
            for i in range(self.size):
                grid[self.y + i][self.x] = "*"
        else:
            for i in range(self.size):
                grid[self.y][self.x + i] = "*"

    def hide(self, grid):
        if self.orientation == "v":
            for i in range(self.size):
                grid[self.y + i][self.x] = " "
        else:
            for i in range(self.size):
                grid[self.y][self.x + i] = " "

    def get_coord_all(self):
        coord = []
        if self.orientation == "v":
            for i in range(self.size):
                coord.append((self.x, self.y + i))
        else:
            for i in range(self.size):
                coord.append((self.x + i, self.y))
        return coord


class ShipEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

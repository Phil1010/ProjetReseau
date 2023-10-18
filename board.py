import ship

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(10)] for _ in range(10)]
        self.ship_little = []

    def is_ship_sunk(self, ship):
        # Vérifie si un bateau est coulé
        pass

    def display(self):
        # Affiche le plateau de jeu en ligne de commande
        print("  A B C D E F G H I J")
        for y in range(10):
            for x in range(10):
                for ship in self.ship_little:
                    if ship.x == x and ship.y == y:
                        for i in range(ship.size):
                            self.grid[y][x+i] = '*'
                    else:
                        self.grid[x][y] = ' '
            row = ' '.join(self.grid[y])                 
            print(f"{y} {row}")
                
from coordinate import Coordinate
import ship


class Board:
    def __init__(self, name: str):
        # Crée un plateau de 10x10
        self.grid = [["~" for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hit_shots = []
        self.missed_shots = []
        self.name = name

    def drawHeader(self) -> str:
        res = """
 ___       _        _ _ _                          _     
| _ ) __ _| |_ __ _(_) | |___   _ _  __ ___ ____ _| |___ 
| _ \/ _` |  _/ _` | | | / -_) | ' \/ _` \ V / _` | / -_)
|___/\__,_|\__\__,_|_|_|_\___| |_||_\__,_|\_/\__,_|_\___|
\n"""

        res += "# - - - - - - - - - - #" + 10 * " " + "# - - - - - - - - - - #\n"
        res += "#    votre plateau    #" + 10 * " " + "#    plateau ennemi   #\n"
        res += "# - - - - - - - - - - #" + 10 * " " + "# - - - - - - - - - - #\n\n"

        res += "# 0 1 2 3 4 5 6 7 8 9 #" + 10 * " " + "# 0 1 2 3 4 5 6 7 8 9 #\n"
        return res

    def drawLineWithoutShip(self, n: int) -> str:
        if n == 0:
            self.drawHeader()
        return f"{n} ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"

    def drawLineWithShips(self, n: int) -> str:
        if n == 0:
            self.drawHeader()
        return f'{n} {" ".join(self.grid[n]).replace("X", "~")} |'

    def drawLineWithShots(self, n: int) -> str:
        if n == 0:
            self.drawHeader()
        return f'{n} {" ".join(self.grid[n]).replace("*", "~")} |'

    def drawLineWithShipsAndShots(self, n: int) -> str:
        if n == 0:
            self.drawHeader()
        return f'{n} {" ".join(self.grid[n])} |'

    def drawFullBoard(self):
        res = "# 0 1 2 3 4 5 6 7 8 9 #\n"
        for i in range(10):
            res += self.drawLineWithShipsAndShots(i) + "\n"
        res += "# - - - - - - - - - - #\n"
        return res

    def addShip(self, ship: ship.Ship):
        # test si le bateau rentre dans le plateau et si il n'y a pas de bateau déjà présent
        if ship.orientation == "v":
            if ship.y + ship.size > 10:
                raise Exception("Le bateau ne rentre pas dans le plateau")
            for i in range(ship.size):
                if self.grid[ship.y + i][ship.x] != "~":
                    print("wtf", self.grid[ship.y + i][ship.x])
                    raise Exception("Il y a déjà un bateau à cet endroit")
                self.grid[ship.y + i][ship.x] = "*"
        else:
            if ship.x + ship.size > 10:
                raise Exception("Le bateau ne rentre pas dans le plateau")
            for i in range(ship.size):
                if self.grid[ship.y][ship.x + i] != "~":
                    raise Exception("Il y a déjà un bateau à cet endroit")
                self.grid[ship.y][ship.x + i] = "*"
        # Ajoute un bateau au plateau
        self.ships.append(ship)

    def shot(self, coordinate: Coordinate):
        x = coordinate.x
        y = coordinate.y
        ships_location = []
        for ship in self.ships:
            ships_location.extend(
                ship.get_coord_all()
            )  # Utilisez extend pour ajouter les coordonnées de chaque bateau à la liste

        # Vérifiez si (x, y) est dans les coordonnées des bateaux
        if (x, y) in ships_location:
            self.hit_shots.append((x, y))
            self.grid[y][x] = "X"

        else:
            self.missed_shots.append((x, y))
            self.grid[y][x] = "-"

        print(x, y)
        print(self.drawFullBoard())
        return self.grid

    def is_win(self) -> bool:
        # Vérifiez si tous les bateaux sont coulés
        if self.drawFullBoard().count("*") == 0:
            return True

        return False

    def get_board(self):
        return self.grid

    def get_empty_coord(self):
        empty_coord = []
        for i in range(10):
            for j in range(10):
                if self.grid[i][j] == " ":
                    empty_coord.append((i, j))
        return empty_coord

    def get_hit_shots(self):
        return self.hit_shots

    def get_missed_shots(self):
        return self.missed_shots

    def isShipPositionValid(self, ship: ship.Ship) -> bool:
        if ship.x < 0 and ship.x > 9  and ship.y < 0 and ship.y > 9:
            return False

        if ship.orientation == "h":
            if ship.x + ship.size > 9:
                return False
            
        elif ship.orientation == "v":
            if ship.y + ship.size > 9:
                return False

        return True

    def isShipPlacable(self, ship: ship.Ship) -> bool:
        if not self.isShipPositionValid(ship):
            return False

        if ship.orientation == "v":
            for y in range(0, ship.size):
                if self.grid[ship.y + y][ship.x] != "~":
                    return False
        elif ship.orientation == "h":
            for x in range(0, ship.size):
                if self.grid[ship.y][ship.x + x] != "~":
                    return False
        else:  # l'orientation est pas bonne
            return False

        return True


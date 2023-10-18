import ship
import player


class Board:
    def __init__(self):
        # Crée un plateau de 10x10
        self.grid = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hit_shots = []
        self.missed_shots = []

    def add_ship(self, ship):
        # test si le bateau rentre dans le plateau et si il n'y a pas de bateau déjà présent
        if ship.orientation == "vertical":
            if ship.y + ship.size > 10:
                raise Exception("Le bateau ne rentre pas dans le plateau")
            for i in range(ship.size):
                if self.grid[ship.y + i][ship.x] != " ":
                    raise Exception("Il y a déjà un bateau à cet endroit")
                self.grid[ship.y + i][ship.x] = "*"
        else:
            if ship.x + ship.size > 10:
                raise Exception("Le bateau ne rentre pas dans le plateau")
            for i in range(ship.size):
                if self.grid[ship.y][ship.x + i] != " ":
                    raise Exception("Il y a déjà un bateau à cet endroit")
                self.grid[ship.y][ship.x + i] = "*"
        # Ajoute un bateau au plateau
        self.ships.append(ship)

    # affiche juste le plateau, sans batteaux
    def display_init(self):
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(10):
            print(i, end=" ")
            for j in range(10):
                print(self.grid[i][j], end=" ")
            print()

    # display pour afficher le plateau de départ, sans tirs
    def display_ships(self):
        # Affiche le plateau de jeu en ligne de commande
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(10):
            print(i, end=" ")
            for j in range(10):
                for ship in self.ships:
                    if ship.x == j and ship.y == i:
                        ship.display(self.grid)
                print(self.grid[i][j], end=" ")
            print()

    def display_board(self):
        # Crée une copie du plateau actuel pour afficher les tirs réussis et ratés
        display_grid = [row[:] for row in self.grid]

        # Marquer les tirs réussis avec "X"
        for x, y in self.hit_shots:
            display_grid[y][x] = "X"

        # Marquer les tirs ratés avec "-"
        for x, y in self.missed_shots:
            display_grid[y][x] = "-"

        # Affiche le plateau de jeu en ligne de commande
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(10):
            print(i, end=" ")
            for j in range(10):
                for ship in self.ships:
                    if ship.x == j and ship.y == i:
                        ship.display(self.grid)
                print(display_grid[i][j], end=" ")
            print()

    def shot(self, x, y):
        ships_location = []
        for ship in self.ships:
            ships_location.extend(
                ship.get_coord_all()
            )  # Utilisez extend pour ajouter les coordonnées de chaque bateau à la liste

        # Vérifiez si (x, y) est dans les coordonnées des bateaux
        if (x, y) in ships_location:
            self.hit_shots.append((x, y))
        else:
            self.missed_shots.append((x, y))

    def get_board(self):
        return self.grid

    def get_hit_shots(self):
        return self.hit_shots

    def get_missed_shots(self):
        return self.missed_shots

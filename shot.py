from board import Board
from coordinate import Coordinate


class Shot():
    def __init__(self, x, y: int):
        self.coordinate = Coordinate(x, y)

    def isPositionValid(self, board: Board) -> bool:
        # TODO: ajouter des variable width et height à board et les utiliser ici comme ca peu importe la taille de la grille !!
        if self.coordinate.x >= 0 and self.coordinate.x < 10 and self.coordinate.y >= 0 and self.coordinate.y < 10:
            return True

        return False
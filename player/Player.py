from abc import (
    ABC,
    abstractmethod,
)
from typing import List

from board import Board
from ship import Ship


class Player(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def play(self, playerBoard: Board, ennemyBoard: Board) -> Board:
        pass

    @abstractmethod
    def getShip(self, size: int) -> Ship:
        pass

    @abstractmethod
    def win(self) -> None:
        pass

    @abstractmethod
    def lose(self) -> None:
        pass

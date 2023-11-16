from abc import (
    ABC,
    abstractmethod,
)
from typing import List

from board import Board
from coordinate import Coordinate
from ship import Ship


class Player(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_username(self) -> str:
        pass

    @abstractmethod
    def get_shot(self) -> Coordinate:
        pass

    @abstractmethod
    def get_ship(self, size: int) -> Ship:
        pass

    @abstractmethod
    def set_win(self) -> None:
        pass

    @abstractmethod
    def set_lose(self) -> None:
        pass

    @abstractmethod
    def get_gamemode(self) -> str:
        pass

    @abstractmethod
    def set_grid(self, playerBoard, ennemyBoard: Board) -> None:
        pass

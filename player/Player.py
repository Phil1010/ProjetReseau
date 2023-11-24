from abc import (
    ABC,
    abstractmethod,
)

from board import Board
from ship import Ship
from shot import Shot
from message import Message


class Player(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_username(self) -> str:
        pass

    @abstractmethod
    def get_shot(self, board: Board, message: Message) -> Shot:
        pass

    @abstractmethod
    def get_ship(self, board: Board, size: int) -> Ship:
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
    def set_grid(self, playerBoard, ennemyBoard: Board, playerA, playerB) -> None:
        pass

    @abstractmethod
    def notify(self, chronometer: int):
        pass

    @abstractmethod
    def timeout(self):
        pass

    @abstractmethod
    def set_exit(self) -> None:
        pass

    @abstractmethod
    def set_time(self, duration: int) -> None:
        pass

    @abstractmethod
    def sendMessage(self, message: str) -> None:
        pass

    @abstractmethod
    def get_action(self) -> Message:
        pass

    @abstractmethod
    def get_message(self, message: Message) -> str:
        pass

from enum import Enum


class Move(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def __str__(self):
        return f'{self.name}'

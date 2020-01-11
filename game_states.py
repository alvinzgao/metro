"""
Enum representing all possible game states in Ride the Bus
"""
from enum import Enum, auto


class GameState(Enum):
    r1_red_or_black = auto()
    r1_higher_or_lower = auto()
    r1_inside_or_outside = auto()
    r1_guess_the_suit = auto()
    r2 = auto()
    r3_red_or_black = auto()
    r3_higher_or_lower = auto()
    r3_inside_or_outside = auto()
    r3_guess_the_suit = auto()
    finished = auto()

    def advance(self):
        """
        Advance the game state
        """
        assert self != GameState.finished, f'Game is already finished'
        return GameState(self.value + 1)

    @property
    def round(self) -> int:
        return int(self.name[1])

"""
Enum representing all possible game states in Ride the Bus
"""
from enum import Enum, auto
from typing import Callable, Optional

from metro import player_choices


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

    @property
    def player_choice(self) -> Optional[Callable]:
        if 'red_or_black' in self.name:
            return player_choices.red_or_black
        elif 'higher_or_lower' in self.name:
            return player_choices.higher_or_lower
        elif 'inside_or_outside' in self.name:
            return player_choices.inside_or_outside
        elif 'guess_the_suit' in self.name:
            return player_choices.guess_the_suit
        return None

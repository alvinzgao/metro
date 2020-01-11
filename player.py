"""
Representation of a player in Ride the Bus
"""
from typing import Any, Callable, Dict, List

from metro.deck import Deck, Card
from metro.game_states import GameState
from metro.player_strategies import DEFAULT_STRATEGIES


class Player(object):

    def __init__(self, name: Any = None):
        self.name: Any = name
        self.hand: List[Card] = []
        self.drinks: int = 0
        self.assigned_drinks: int = 0
        self.strategies: Dict[GameState, Callable] = DEFAULT_STRATEGIES

    def set_strategies(self, strategies: Dict[GameState, Callable]) -> None:
        self.strategies.update(strategies)

    def draw(self, deck: Deck) -> Card:
        card = deck.draw()
        self.hand.append(card)
        return card

    def drink(self) -> None:
        self.drinks += 1

    def assign_drink(self) -> None:
        self.assigned_drinks += 1

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        formatted_player_name = str(self.name) + ', ' if self.name else ''
        return f'{class_name}({formatted_player_name}{self.drinks} drinks)'

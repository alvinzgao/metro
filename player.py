"""
Representation of a player in Ride the Bus
"""
from collections import Counter
from enum import Enum
from typing import Any, Callable, Dict, List, Type, Set

from metro.deck import Deck, Card
from metro.game_states import GameState
from metro.player_strategies import (choose_color_with_card_counting,
                                     choose_hi_or_lo_with_card_counting,
                                     choose_in_or_out_with_card_counting,
                                     choose_suit_with_card_counting,
                                     play_all_matches)


DEFAULT_STRATEGIES: Dict[GameState, Callable] = {
    GameState.r1_red_or_black: choose_color_with_card_counting,
    GameState.r1_higher_or_lower: choose_hi_or_lo_with_card_counting,
    GameState.r1_inside_or_outside: choose_in_or_out_with_card_counting,
    GameState.r1_guess_the_suit: choose_suit_with_card_counting,
    GameState.r2: play_all_matches,
    GameState.r3_red_or_black: choose_color_with_card_counting,
    GameState.r3_higher_or_lower: choose_hi_or_lo_with_card_counting,
    GameState.r3_inside_or_outside: choose_in_or_out_with_card_counting,
    GameState.r3_guess_the_suit: choose_suit_with_card_counting,
}


class Player(object):

    def __init__(self, name: Any = None):
        self.name: Any = name
        self.hand: List[Card] = []
        self.drinks: Counter[GameState] = Counter()
        self.assigned_drinks: Counter[GameState] = Counter()
        self.strategies: Dict[GameState, Callable] = DEFAULT_STRATEGIES

    def set_strategies(self, strategies: Dict[GameState, Callable]) -> None:
        self.strategies.update(strategies)

    def discard_hand(self):
        self.hand = []

    def guess(self, game_state: GameState, deck: Deck) -> Type[Enum]:
        assert game_state.round in {1, 3}, 'Can only guess during round 1 or 3'

        guess = self.strategies[game_state](hand=self.hand, deck=deck)
        self.hand.append(deck.draw())
        return guess

    def match(self, flipped_card: Card, deck: Deck) -> Set[Card]:
        matched_cards = self.strategies[GameState.r2](
            flipped_card=flipped_card, hand=self.hand, deck=deck)
        self.hand = [card for card in self.hand if card not in matched_cards]
        return matched_cards

    def drink(self, game_state: GameState, num_drinks: int = 1) -> None:
        self.drinks[game_state] += num_drinks

    def assign_drink(self, game_state: GameState, num_drinks: int = 1) -> None:
        self.assigned_drinks[game_state] += num_drinks

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        formatted_player_name = (
            str(self.name) + ', ' if self.name is not None else '')
        return f'{class_name}({formatted_player_name}{len(self.drinks)} drinks)'

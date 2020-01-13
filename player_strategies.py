"""
Functions representing possible player strategies in Ride the Bus
"""
from enum import Enum
import random
from typing import Dict, Callable, Type, List

from metro.deck import Color, Suit, Card, Deck
from metro.game_states import GameState
from metro.player_choices import HiLoChoices, InOutChoices


def choose_randomly(choices: Type[Enum]) -> Callable:
    """
    Returns a function representing a random choice from an enum
    """
    def _strategy(previous_cards: List[Card], deck: Deck) -> Type[Enum]:
        del previous_cards
        del deck
        return random.choice(list(choices))

    return _strategy


def play_all_matches(flipped_card: Card, hand: List[Card]) -> List[Card]:
    """
    Play all cards with the same value as the flipped card
    """
    return [card for card in hand if card.value == flipped_card.value]


DEFAULT_STRATEGIES: Dict[GameState, Callable] = {
    GameState.r1_red_or_black: choose_randomly(Color),
    GameState.r1_higher_or_lower: choose_randomly(HiLoChoices),
    GameState.r1_inside_or_outside: choose_randomly(InOutChoices),
    GameState.r1_guess_the_suit: choose_randomly(Suit),
    GameState.r2: play_all_matches,
    GameState.r3_red_or_black: choose_randomly(Color),
    GameState.r3_higher_or_lower: choose_randomly(HiLoChoices),
    GameState.r3_inside_or_outside: choose_randomly(InOutChoices),
    GameState.r3_guess_the_suit: choose_randomly(Suit),
}

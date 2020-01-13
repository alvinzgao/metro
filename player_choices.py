"""
Functions representing player choices in Ride the Bus
"""
from enum import Enum, auto
from typing import List

from metro.deck import Card, Color, Suit


class HiLoChoices(Enum):
    """
    Enum containing all possible higher-or-lower choices
    """
    higher = auto()
    lower = auto()


class InOutChoices(Enum):
    """
    Enum containing all possible inside-or-outside choices
    """
    inside = auto()
    outside = auto()


def red_or_black(next_card: Card, choice: Color, **kwargs) -> bool:
    """
    Player guesses whether the next card will be red or black
    """
    del kwargs
    return next_card.color == choice


def higher_or_lower(next_card: Card,
                    previous_cards: List[Card],
                    choice: HiLoChoices) -> bool:
    """
    Player guesses whether the next card will be higher or lower than the
    previous card drawn by that player
    """
    assert len(previous_cards) >= 1, (
        'Must have one previous card to guess higher or lower')

    previous_value = previous_cards[-1].value
    if next_card.value == previous_value:
        return False

    return not ((next_card.value > previous_value)
                ^ (choice == HiLoChoices.higher))


def inside_or_outside(next_card: Card,
                      previous_cards: List[Card],
                      choice: InOutChoices) -> bool:
    """
    Player guesses whether the next card will be inside or outside the range
    defined by the two previous cards drawn by that player (exclusive)
    """
    assert len(previous_cards) >= 2, (
        'Must have two previous cards to guess inside or outside')

    previous_values = sorted(card.value for card in previous_cards[-2:])
    if next_card.value in previous_values:
        return False

    is_inside = previous_values[0] < next_card.value < previous_values[1]
    return not (is_inside ^ (choice == InOutChoices.inside))


def guess_the_suit(next_card: Card, choice: Suit, **kwargs) -> bool:
    """
    Player guesses the suit of the next card
    """
    del kwargs
    return next_card.suit == choice

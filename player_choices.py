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


def red_or_black(next_card: Card, choice: Color) -> bool:
    """
    Player guesses whether the next card will be red or black
    """
    return next_card.color == choice


def higher_or_lower(next_card: Card,
                    previous_card: Card,
                    choice: HiLoChoices) -> bool:
    """
    Player guesses whether the next card will be higher or lower than the
    previous card drawn by that player
    """
    if next_card.value == previous_card.value:
        return False
    return not ((next_card.value > previous_card.value)
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

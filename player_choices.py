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


def red_or_black(hand: List[Card], choice: Color) -> bool:
    """
    Player guesses whether the next card will be red or black
    """
    assert len(hand) >= 1, (
        'Must have one card in hand to evaluate red or black')
    return hand[-1].color == choice


def higher_or_lower(hand: List[Card], choice: HiLoChoices) -> bool:
    """
    Player guesses whether the next card will be higher or lower than the
    previous card drawn by that player
    """
    assert len(hand) >= 2, (
        'Must have two cards in hand to evaluate higher or lower')
    return False if hand[-1].value == hand[-2].value else (
        not (hand[-1].value > hand[-2].value) ^ (choice == HiLoChoices.higher))


def inside_or_outside(hand: List[Card], choice: InOutChoices) -> bool:
    """
    Player guesses whether the next card will be inside or outside the range
    defined by the two previous cards drawn by that player (exclusive)
    """
    assert len(hand) >= 3, (
        'Must have three cards in hand to evaluate inside or outside')

    previous_values = sorted(card.value for card in hand[-3:-1])
    is_inside = previous_values[0] < hand[-1].value < previous_values[1]
    return False if hand[-1].value in previous_values else (
        not is_inside ^ (choice == InOutChoices.inside))


def guess_the_suit(hand: List[Card], choice: Suit) -> bool:
    """
    Player guesses the suit of the next card
    """
    assert len(hand) >= 1, (
        'Must have one card in hand to evaluate suit')
    return hand[-1].suit == choice

"""
Functions representing possible player strategies in Ride the Bus
"""
from enum import Enum
import random
from typing import Callable, Type, List

from metro.deck import Color, Suit, Card, Deck
from metro.player_choices import HiLoChoices, InOutChoices


def choose_randomly(choices: Type[Enum]) -> Callable:
    """
    Returns a function representing a random choice from an enum
    """
    def _strategy(**kwargs) -> Type[Enum]:
        del kwargs
        return random.choice(list(choices))

    return _strategy


def choose_color_with_card_counting(deck: Deck, **kwargs) -> Color:
    """
    Choose the color that appears most often in the deck
    """
    del kwargs
    counts = deck.count('color')
    return max(counts, key=counts.get)


def choose_hi_or_lo_with_card_counting(hand: List[Card], deck: Deck
                                       ) -> HiLoChoices:
    """
    Choose whether there are more cards in the deck that are higher or lower
    than the previous card
    """
    assert len(hand) >= 1, (
        'Must have one card in hand to guess higher or lower')

    previous_value = hand[-1].value
    counts = deck.count('value')
    higher_count = sum(count for value, count in counts.items()
                       if value > previous_value)
    lower_count = sum(count for value, count in counts.items()
                      if value < previous_value)
    return HiLoChoices.higher if higher_count > lower_count else (
        HiLoChoices.lower)


def choose_in_or_out_with_card_counting(hand: List[Card], deck: Deck
                                        ) -> HiLoChoices:
    """
    Choose whether there are more cards in the deck that are higher or lower
    than the previous card
    """
    assert len(hand) >= 2, (
        'Must have two cards in hand to guess inside or outside')

    previous_values = sorted(card.value for card in hand[-2:])
    counts = deck.count('value')
    inside_count = sum(count for value, count in counts.items()
                       if previous_values[0] < value < previous_values[1])
    outside_count = sum(count for value, count in counts.items()
                        if (value < previous_values[0]
                            or value > previous_values[1]))
    return InOutChoices.inside if inside_count > outside_count else (
        InOutChoices.outside)


def choose_suit_with_card_counting(deck: Deck, **kwargs) -> Suit:
    """
    Choose the suit that appears most often in the deck
    """
    del kwargs
    counts = deck.count('suit')
    return max(counts, key=counts.get)


def play_all_matches(flipped_card: Card, hand: List[Card]) -> List[Card]:
    """
    Play all cards with the same value as the flipped card
    """
    return [card for card in hand if card.value == flipped_card.value]

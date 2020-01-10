"""
A lightweight implementation of a deck of playing cards
"""
from collections import Counter
from enum import Enum, auto
import random
from typing import Dict, List, NamedTuple


NAMED_VALUES = {
    1: 'Ace',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}


class Suit(Enum):
    """
    Enum containing all possible card suits
    """
    clubs = auto()
    diamonds = auto()
    hearts = auto()
    spades = auto()


SUIT_TO_COLOR: Dict[Suit, str] = {
    Suit.clubs: 'b',
    Suit.diamonds: 'r',
    Suit.hearts: 'r',
    Suit.spades: 'b',
}
assert len(SUIT_TO_COLOR) == len(Suit)


class Card(NamedTuple):
    """
    Class representing a playing card
    """
    suit: Suit
    value: int

    @property
    def color(self) -> str:
        return SUIT_TO_COLOR[self.suit]

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        value_name = NAMED_VALUES.get(self.value, self.value)
        suit_name = self.suit.name.capitalize()
        return f'{class_name}({value_name} of {suit_name})'


class Deck(object):
    """
    Class representing a deck of playing cards
    """

    def __init__(self, num_cards=52):
        assert num_cards <= 52, 'Deck cannot have > 52 cards'

        self.cards: List[Card] = []

        self.reset_cards()
        if num_cards < 52:
            self.cards = self.cards[:num_cards]

    def reset_cards(self) -> None:
        """
        Shuffle all cards back into the deck
        """
        cards = [Card(suit=suit, value=value)
                 for suit in Suit for value in range(1, 14)]
        random.shuffle(cards)
        self.cards = cards

    def draw(self) -> Card:
        """
        Draw a random card
        """
        return self.cards.pop()

    def count(self, attr: str) -> Counter:
        """
        Count cards in the deck by card attribute
        """
        assert hasattr(Card, attr), f'Card has no {attr} attribute'
        return Counter(getattr(card, attr) for card in self.cards)

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({len(self)} cards)'

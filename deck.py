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
    
    
class Color(Enum):
    """
    Enum containing all possible card colors
    """
    red = auto()
    black = auto()


SUIT_TO_COLOR: Dict[Suit, Color] = {
    Suit.clubs: Color.black,
    Suit.diamonds: Color.red,
    Suit.hearts: Color.red,
    Suit.spades: Color.black,
}
assert len(SUIT_TO_COLOR) == len(Suit)


class Card(NamedTuple):
    """
    Class representing a playing card
    """
    value: int
    suit: Suit

    @property
    def color(self) -> Color:
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

    def __init__(self, num_cards: int = 52, reset_when_empty: bool = True):
        assert num_cards <= 52, 'Deck cannot have > 52 cards'

        self.cards: List[Card] = []
        self.reset_when_empty: bool = reset_when_empty

        self.reset_cards()
        if num_cards < 52:
            self.cards = self.cards[:num_cards]

    def reset_cards(self) -> None:
        """
        Shuffle all cards back into the deck
        """
        cards = [Card(value=value, suit=suit)
                 for value in range(1, 14) for suit in Suit]
        random.shuffle(cards)
        self.cards = cards

    def draw(self) -> Card:
        """
        Draw a random card
        """
        assert self.cards, 'Deck is empty'
        next_card = self.cards.pop()
        if not self.cards and self.reset_when_empty:
            self.reset_cards()
        return next_card

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

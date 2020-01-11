"""
Simulator for Ride the Bus
"""
from typing import List

from metro.deck import Deck
from metro.game_states import GameState
from metro.player import Player


class Game(object):

    def __init__(self, players: List[Player]):
        self.players = players
        self.deck = Deck()
        self.game_state: GameState = GameState(1)

    def play(self):
        """
        Play an entire game to completion
        """
        pass

    def play_turn(self):
        """
        Play a single turn and advance the game state
        """
        assert self.game_state != GameState.finished, (
            f'Game is already finished')

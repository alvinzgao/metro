"""
Simulator for Ride the Bus
"""
from typing import List

from metro.deck import Deck
from metro.game_states import GameState
from metro.player import Player


class Game(object):

    def __init__(self, players: List[Player]):
        self.players: List[Player] = players
        self.game_state: GameState = GameState(1)
        self.deck: Deck = Deck()
        self.bus_rider: Player = None

    def advance_game_state(self) -> None:
        """
        Advance the game state
        """
        self.game_state = self.game_state.advance()

    def play(self) -> None:
        """
        Play an entire game to completion
        """
        while self.game_state != GameState.finished:
            print(self.game_state)
            self.play_turn()

    def play_turn(self) -> None:
        """
        Play a single turn and advance the game state
        """
        assert self.game_state != GameState.finished, (
            f'Game is already finished')

        if self.game_state.round == 1:
            self._play_round_one_turn()
        elif self.game_state.round == 2:
            self._play_round_two()
        elif self.game_state.round == 3:
            self._play_round_three_turn()

    def _play_round_one_turn(self) -> None:
        """
        Play a single turn in round one and advance the game state
        """
        for player in self.players:
            choice = player.choose(self.game_state, self.deck)
            next_card = player.draw(self.deck)
            if self.game_state.player_choice(next_card=next_card,
                                             previous_cards=player.hand,
                                             choice=choice):
                player.assign_drink()
            else:
                player.drink()
        self.advance_game_state()

    def _play_round_two(self) -> None:
        """
        Play round two and advance the game state
        """
        # TODO: implement
        self.bus_rider = self.players[0]
        self.advance_game_state()

    def _play_round_three_turn(self) -> None:
        """
        Play a single turn in round three and advance the game state
        """
        assert self.bus_rider, 'Bus rider not chosen in round two'

        choice = self.bus_rider.choose(self.game_state, self.deck)
        next_card = self.bus_rider.draw(self.deck)
        if self.game_state.player_choice(next_card=next_card,
                                         previous_cards=self.bus_rider.hand,
                                         choice=choice):
            self.advance_game_state()
        else:
            self.bus_rider.drink()
            self.game_state = GameState.r3_red_or_black

"""
Simulator for Ride the Bus
"""
from typing import List

from metro.deck import Deck
from metro.game_states import GameState
from metro.player import Player


class Game(object):

    def __init__(self, players: List[Player], num_pyramid_rows: int = 4):
        assert 4 * len(players) + sum(range(num_pyramid_rows + 1)) <= 52, (
            f'Not enough cards for {len(players)} players and '
            f'{num_pyramid_rows} pyramid rows')

        self.players: List[Player] = players
        self.num_pyramid_rows = num_pyramid_rows
        self.game_state: GameState = GameState(1)
        self.deck: Deck = Deck()
        self.bus_rider: Player = None

    @classmethod
    def with_default_players(cls, num_players: int):
        return cls(players=[Player(index) for index in range(num_players)])

    def advance_game_state(self) -> None:
        """
        Advance the game state
        """
        self.game_state = self.game_state.advance()

    def play(self,
             stop_state: GameState = GameState.finished,
             wait_for_input: bool = False,
             verbose: bool = False) -> None:
        """
        Play an entire game to completion
        """
        while self.game_state != stop_state:
            self.play_turn(verbose=verbose)
            if wait_for_input:
                input()
        if verbose:
            print('Game finished. Player results:\n'
                  + '\n'.join([str(player) for player in self.players]))

    def play_turn(self, verbose: bool = False) -> None:
        """
        Play a single turn and advance the game state
        """
        assert self.game_state != GameState.finished, (
            f'Game is already finished')

        if verbose:
            print(f'Starting turn: {self.game_state.name}')

        if self.game_state.round == 1:
            self._play_round_one_turn(verbose=verbose)
        elif self.game_state.round == 2:
            self._play_round_two(verbose=verbose)
        elif self.game_state.round == 3:
            self._play_round_three_turn(verbose=verbose)

    def _play_round_one_turn(self, verbose: bool = False) -> None:
        """
        Play a single turn in round one and advance the game state
        """
        for player in self.players:
            choice = player.guess(self.game_state, self.deck)
            correct = self.game_state.player_choice(hand=player.hand,
                                                    choice=choice)
            if verbose:
                descriptor = '' if correct else 'NOT '
                print(f'{player} chose {choice.name} and drew '
                      f'{player.hand[-1]}, so they were {descriptor}correct')
            if correct:
                player.assign_drink()
            else:
                player.drink()
        self.advance_game_state()

    def _play_round_two(self, verbose: bool = False) -> None:
        """
        Play round two and advance the game state
        """
        # TODO: implement
        self.bus_rider = self.players[0]
        self.advance_game_state()

    def _play_round_three_turn(self, verbose: bool = False) -> None:
        """
        Play a single turn in round three and advance the game state
        """
        assert self.bus_rider, 'Bus rider not chosen in round two'
        player = self.bus_rider

        choice = player.guess(self.game_state, self.deck)
        correct = self.game_state.player_choice(hand=player.hand,
                                                choice=choice)
        if verbose:
            descriptor = '' if correct else 'NOT '
            print(f'{player} chose {choice.name} and drew '
                  f'{player.hand[-1]}, so they were {descriptor}correct')
        if correct:
            self.advance_game_state()
        else:
            player.drink()
            self.game_state = GameState.r3_red_or_black

"""
Utility functions for facilitating simulation
"""
from collections import Counter
from typing import List

from metro.game import Game
from metro.game_states import GameState
from metro.player import Player


def summarize_player_stats(players: List[Player],
                           num_games: int = 1) -> None:
    """
    Print formatted player stats
    """
    player_games = len(players) * num_games

    drinks = sum([p.drinks for p in players], Counter())
    assigned = sum([p.assigned_drinks for p in players], Counter())
    combined = drinks + assigned

    drinks_total = sum(drinks.values())
    assigned_total = sum(assigned.values())
    combined_total = drinks_total + assigned_total
    
    print(f'Total drinks in {num_games} game(s) = {combined_total} '
          f'= {drinks_total} (dealt) + {assigned_total} (assigned)')
    print(f'Average drinks per player per game '
          f'= {combined_total / player_games:.2f} '
          f'= {drinks_total / player_games:.2f} (dealt) '
          f'+ {assigned_total / player_games:.2f} (assigned)')
    print()

    print('Average drinks per round per player per game: ')
    for round_num in [1, 2, 3]:
        avg_drinks = sum(drinks[gs] for gs in drinks
                         if gs.round == round_num) / player_games
        avg_assigned = sum(assigned[gs] for gs in assigned
                           if gs.round == round_num) / player_games
        avg_combined = avg_drinks + avg_assigned
        print(f'\tRound {round_num} : {avg_combined:.2f} '
              f'= {avg_drinks:.2f} (dealt) + {avg_assigned:.2f} (assigned)')
    print()

    print('Average drinks per turn per player per game: ')
    for game_state in GameState:
        if game_state == GameState.finished:
            break
        avg_drinks = drinks[game_state] / player_games
        avg_assigned = assigned[game_state] / player_games
        avg_combined = avg_drinks + avg_assigned
        print(f'\t{game_state.name:<20} : {avg_combined:.2f} '
              f'= {avg_drinks:.2f} (dealt) + {avg_assigned:.2f} (assigned)')


def play_and_summarize(game: Game, num_games: int) -> None:
    """
    Play a number of games and print formatted player stats
    """
    assert game.game_state == GameState(1), f'Game state is not {GameState(1)}'

    for _ in range(num_games):
        game.play()
        game.reset()

    summarize_player_stats(players=game.players, num_games=num_games)

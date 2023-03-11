from game import Game
from player import Player
from move import Move

import time
import os
import sys


def user_play(game):
    print(game)

    try:
        while True:
            user_in = input()

            if user_in == "w":
                game.move_robot(move=Move.UP)
            elif user_in == "a":
                game.move_robot(move=Move.LEFT)
            elif user_in == "s":
                game.move_robot(move=Move.DOWN)
            elif user_in == "d":
                game.move_robot(move=Move.RIGHT)

            print(game)

    except EOFError:
        print(game)


def player_play(game):
    player = Player()

    print("Start learning")
    player.learn(episodes=game.board_dim*2000, board_dim=game.board_dim)
    print("Stop learning")

    on_move_played(game, None)
    player.play_game(game=game, on_move_played=on_move_played)


def on_move_played(game, move):
    cls()
    print(move)
    print(game)
    time.sleep(2)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main(argv):
    board_dim = 6

    if len(argv) > 1:
        board_dim = int(argv[1])

    game = Game(board_dim=board_dim)

    player_play(game)
    # user_play(game)


if __name__ == "__main__":
    main(sys.argv)

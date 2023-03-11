from game import Game
from player import Player
from move import Move

import time
import os


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

    print(game)
    print()
    player.play_game(game=game, on_move_played=on_move_played)


def on_move_played(game, move):
    cls()
    print(move)
    print(game)
    time.sleep(2)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    game = Game(board_dim=6)

    player_play(game)
    # user_play(game)


if __name__ == "__main__":
    main()

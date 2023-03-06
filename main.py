from game import Game
from player import Player
from move import Move


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
    print(game)

    player = Player(Game())

    print("Start learning")
    player.learn(episodes=10)
    print("Learning finished")

    player.game = game

    try:
        flag_stop = False

        while not flag_stop:
            input()
            print(player.play_one_move())

            print(game)

    except EOFError:
        print(game)


def main():
    game = Game()

    player_play(game)
    # user_play(game)


if __name__ == "__main__":
    main()

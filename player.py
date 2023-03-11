from move import Move
import random
from game import Game

rand = random.Random(24)


class Player:
    state_action = {}
    game = None

    def play_game(self, game, on_move_played=lambda game, move: None):
        self.game = game

        flag_stop = False

        while not flag_stop:
            move, flag_stop = self.play_one_move(alpha=0)
            on_move_played(self.game, move)

    def learn(self, episodes=1000, board_dim=3):
        for count in range(episodes):
            self.game = Game(board_dim=board_dim)

            try:
                self.state_action[self.game.state.__str__()]
            except KeyError:
                self.state_action[self.game.state.__str__()] = {
                    Move.UP: 0,
                    Move.RIGHT: 0,
                    Move.DOWN: 0,
                    Move.LEFT: 0
                }

            flag_stop = False

            while not flag_stop:
                _, flag_stop = self.play_one_move()

    def play_one_move(self, alpha=0.5):
        greedy_move = self.__get_greedy_moves__()

        old_state = self.game.state.__str__()
        eat_diamond = self.game.move_robot(move=greedy_move)

        try:
            self.state_action[self.game.state.__str__()]

        except KeyError:
            self.state_action[self.game.state.__str__()] = {
                Move.UP: 0,
                Move.RIGHT: 0,
                Move.DOWN: 0,
                Move.LEFT: 0
            }

        if not eat_diamond:
            q_n = self.state_action[old_state][greedy_move]
            max_q_n_1 = max([qn[1] for qn in self.state_action[self.game.state.__str__()].items()])
            self.state_action[old_state][greedy_move] = q_n + alpha * (-1 + max_q_n_1 - q_n)

        return greedy_move, eat_diamond

    def __get_greedy_moves__(self, epsilon=0.9):
        actions = None
        try:
            actions = self.state_action[self.game.state.__str__()]
        except KeyError:
            print()

        sorted_actions = sorted(actions.items(), key=lambda x: -x[1])

        if rand.choices([0, 1], weights=[1-epsilon, epsilon]) == 1:
            sorted_actions.insert(0, rand.choice(sorted_actions)[0])

        return sorted_actions[0][0]

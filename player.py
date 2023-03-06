from move import Move
import random


class Player:
    state_action = {}

    def __init__(self, game):
        self.game = game

        self.state_action[self.game.state.__str__()] = {
            Move.UP: 0,
            Move.RIGHT: 0,
            Move.DOWN: 0,
            Move.LEFT: 0
        }

    def play_one_move(self):
        greedy_moves = self.__get_greedy_moves__()

        action = greedy_moves[random.randrange(0, len(greedy_moves), 1)]
        eat_diamond = self.game.move_robot(move=action)

        return action, eat_diamond

    def learn(self, episodes=1000):
        for count in range(episodes):
            print("Start episode", count)
            self.__learn_episode__()
            print("End episode", count)

    def __learn_episode__(self):
        moves = []
        flag_stop = False

        while not flag_stop:
            old_state = self.game.state.__str__()
            action, flag_stop = self.play_one_move()

            if self.game.state.__str__() not in self.state_action.keys():
                self.state_action[self.game.state.__str__()] = {
                    Move.UP: 0,
                    Move.RIGHT: 0,
                    Move.DOWN: 0,
                    Move.LEFT: 0
                }

            moves.append((old_state, action))

        self.__reward_moves__(moves)

    def __reward_moves__(self, actions):
        num_moves = len(actions)

        for (state, move) in actions:
            self.state_action[state][move] -= num_moves

    def __get_greedy_moves__(self):
        actions = self.state_action[self.game.state.__str__()]

        result = []
        result_value = 0

        for action in actions:
            if actions[action] > result_value:
                result = [action]
                result_value = actions[action]

            elif actions[action] == result_value:
                result.append(action)

        return result

import random
from move import Move
from game_state import GameState


class Game:
    robot_pos = ()

    def __init__(self):
        self.state = GameState(3)

        self.robot_pos = (random.randrange(0, 3, 1), random.randrange(0, 3, 1))
        self.state.state[self.robot_pos[0]][self.robot_pos[1]] = GameState.ROBOT

        diamond_pos = (random.randrange(0, 3, 1), random.randrange(0, 3, 1))
        while diamond_pos[0] == self.robot_pos[0] and diamond_pos[1] == self.robot_pos[1]:
            diamond_pos = (random.randrange(0, 3, 1), random.randrange(0, 3, 1))

        self.state.state[diamond_pos[0]][diamond_pos[1]] = GameState.DIAMOND

    def move_robot(self, up=0, right=0, down=0, left=0, move=-1):
        self.state.state[self.robot_pos[0]][self.robot_pos[1]] = GameState.EMPTY

        if move == Move.UP:
            up = 1
            right = 0
            down = 0
            left = 0
        elif move == Move.RIGHT:
            up = 0
            right = 1
            down = 0
            left = 0
        elif move == Move.DOWN:
            up = 0
            right = 0
            down = 1
            left = 0
        elif move == Move.LEFT:
            up = 0
            right = 0
            down = 0
            left = 1

        if up == 1 and self.robot_pos[0] != 0:
            self.robot_pos = (self.robot_pos[0] - 1, self.robot_pos[1])

        if right == 1 and self.robot_pos[1] != len(self.state.state[0]) - 1:
            self.robot_pos = (self.robot_pos[0], self.robot_pos[1] + 1)

        if down == 1 and self.robot_pos[0] != len(self.state.state) - 1:
            self.robot_pos = (self.robot_pos[0] + 1, self.robot_pos[1])

        if left == 1 and self.robot_pos[1] != 0:
            self.robot_pos = (self.robot_pos[0], self.robot_pos[1] - 1)

        eat_diamond = self.state.state[self.robot_pos[0]][self.robot_pos[1]] == GameState.DIAMOND

        self.state.state[self.robot_pos[0]][self.robot_pos[1]] = GameState.ROBOT

        return eat_diamond

    def __str__(self):
        return self.state.__str__()

    def __eq__(self, other):
        return self.state == other

    def __hash__(self):
        return hash(repr(self))

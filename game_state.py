class GameState:
    EMPTY = 0
    ROBOT = 1
    DIAMOND = 2

    state = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    def __init__(self, dim):
        self.state = []

        for x in range(dim):
            row = []
            for y in range(dim):
                row.append(self.EMPTY)

            self.state.append(row)

    def __str__(self):
        result = ""

        for x in self.state:
            if len(result) != 0:
                result = result + "\n"

            result_line = ""
            for y in x:
                if len(result_line) != 0:
                    result_line = result_line + " "

                if y == self.DIAMOND:
                    result_line = result_line + "*"
                elif y == self.ROBOT:
                    result_line = result_line + "#"
                else:
                    result_line = result_line + str(y)

            result = result + result_line

        return result

    def __eq__(self, other):
        result = type(self) == type(other)
        result = result and len(self.state) == len(other.state)

        for x in range(len(self.state)):
            result = result and len(self.state[x]) == len(other.state[x])

            if result:
                for y in range(len(self.state[x])):
                    result = result and self.state[x][y] == other.state[x][y]

        return result

    def __hash__(self):
        return hash(repr(self))

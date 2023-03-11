# Introduction

In this repo is implemented a simple game and it's player. This game is composed by a ___car___ represented with the symbol __#__ and a ___coin___ represented with the symbol __*__. In the board the car has to reach the coin to win the game.

---

# Board

The board is generated automatically from the game engine, implemented in the file $game.py$, with the following aspect:
$$
\begin{matrix}
0 & 0 & 0 & 0 \\
0 & \# & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & *
\end{matrix}
$$
The dimension of the board is a parameter of the $game.py$_'s_ _class_.

---

# Game

To win the game the player has to move the _car_ in order to reach the _coin_. The _car_ can move only in four directions: ___up___, ___right___, ___down___, ___left___. This possible moves are implemented in the file $move.py$.

---

# Player

In the file $player.py$ is implemented a _"AI"_ player using __Reinforcement Learning__ in particular implements _q-learning_ _algorithm_.

---

# Code

## Launch

In order to execute the game and the player use the following command:

```shell
$ python main.py [board dimension]
```
# This challenge is based on the classic video game "Snake".
#
# Assume the game screen is an n * n square, and the snake starts the game with length 1
# (i.e. just the head) positioned on the top left corner.
import math


def snakefill(n):
    return math.floor(math.log2(n ** 2))

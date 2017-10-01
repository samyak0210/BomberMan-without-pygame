from __future__ import print_function
from termcolor import colored as cl


class Board():
    a = 0

    def __init__(self):
        self.a = 0

    def makeBoard(self, score, s):
        for i in range(1, 3):
            for j in range(1, 69):
                s[i - 1][j - 1] = 1

        for i in range(1, 39):
            k = i + 2
            for j in range(4):
                s[k - 1][j] = 1
            for j in range(1, 61):
                l = j + 4
                if i % 4 == 3 or i % 4 == 0:
                    if j % 8 in [0, 5, 6, 7]:
                        s[k - 1][l - 1] = 1

            for j in range(4):
                s[k - 1][j + 64] = 1

        for i in range(2):
            for j in range(1, 69):
                s[i + 40][j - 1] = 1

    def printBoard(self, s, b, score, x, y, count, bx, by, life, level):
        print("Your Score is ", score)
        print("No of lives left ", life)
        print("You are on level ", level)
        print("Press q to quit")
        for i in range(42):
            for j in range(68):
                if s[i][j] == 2:
                    print(cl("^", "yellow"), end="")
                elif b[i][j] == 2:
                    print(cl("E", "red"), end="")
                elif b[i][j] == 1:
                    print(cl("B", "white"), end="")
                elif s[i][j] == 0 and b[i][j] == 0:
                    print(" ", end="")
                elif s[i][j] == 1 and b[i][j] == 0:
                    print(cl("#", "cyan"), end="")

                elif s[i][j] == 3 and b[i][j] == 0:
                    if j == by:
                        print(cl("[", "yellow"), end="")
                    elif j == by + 1 or j == by + 2:
                        print(cl(count, "yellow"), end="")
                    elif j == by + 3:
                        print(cl("]", "yellow"), end="")

                elif s[i][j] == 4 and b[i][j] == 0:
                    print(cl("/", "green"), end="")

            print(" ")

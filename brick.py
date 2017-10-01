from __future__ import print_function
import random


class Brick():
    a = 0

    def __init__(self):
        self.a = 0

    def create_bricks(self, x, y, s):
        for i in range(2):
            for j in range(4):
                s[x + i][y + j] = 4

    def make_bricks(self, wall, s, num):
        a = random.sample(range(0, len(wall)), num)
        for i in a:
            self.create_bricks(wall[i][0], wall[i][1], s)

    def remove_bricks(self, s, bx, by, wall):
        if s[bx][by - 1] == 4:
            wall.remove([bx, by - 4])
        if s[bx - 1][by] == 4:
            wall.remove([bx - 2, by])
        if s[bx][by + 4] == 4:
            wall.remove([bx, by + 4])
        if s[bx + 2][by] == 4:
            wall.remove([bx + 2, by])

    def make_wall(self, wall):
        for i in range(4, 40, 2):
            if i % 4 == 0 or i % 4 == 1:
                for j in range(4, 61, 8):
                    wall.append([i, j])
            if i % 4 == 2 or i % 4 == 3:
                for j in range(4, 61, 4):
                    wall.append([i, j])

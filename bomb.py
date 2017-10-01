from __future__ import print_function
from brick import Brick


class Bomb(Brick):

    def __init__(self, bx, by):
        self.bx = bx
        self.by = by

    def change(self, x, y):
        self.bx = x
        self.by = y

    def explode(self, s, b, wall, enemy_pos):
        self.remove_bricks(s, self.bx, self.by, wall)
        self.remove(b)
        bx = self.bx
        by = self.by
        for i in range(bx, bx + 2):
            for j in range(by - 1, by - 5, -1):
                if s[i][j] in [0, 4]:
                    s[i][j] = 2
                b[i][j] = 0
            for j in range(by + 4, by + 8):
                if s[i][j] in [0, 4]:
                    s[i][j] = 2
                b[i][j] = 0

        for i in range(bx - 1, bx - 3, -1):
            for j in range(by, by + 4):
                if s[i][j] in [0, 4]:
                    s[i][j] = 2
                b[i][j] = 0

        for i in range(bx + 2, bx + 4):
            for j in range(by, by + 4):
                if s[i][j] in [0, 4]:
                    s[i][j] = 2
                b[i][j] = 0
        if [bx, by] in enemy_pos:
            enemy_pos.remove([bx, by])
        if [bx, by - 4] in enemy_pos:
            enemy_pos.remove([bx, by - 4])
        if [bx, by + 4] in enemy_pos:
            enemy_pos.remove([bx, by + 4])
        if [bx - 2, by] in enemy_pos:
            enemy_pos.remove([bx - 2, by])
        if [bx + 2, by] in enemy_pos:
            enemy_pos.remove([bx + 2, by])

    def place(self, s):
        x = self.bx
        y = self.by
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                s[i][j] = 3

    def remove(self, s):
        for i in range(self.bx, self.bx + 2):
            for j in range(self.by, self.by + 4):
                s[i][j] = 0

    def rem_expo(self, s):
        x = self.bx
        y = self.by
        for i in range(x, x + 2):
            for j in range(y - 1, y - 5, -1):
                if s[i][j] == 2:
                    s[i][j] = 0
            for j in range(y + 4, y + 8):
                if s[i][j] == 2:
                    s[i][j] = 0

        for i in range(x - 1, x - 3, -1):
            for j in range(y, y + 4):
                if s[i][j] == 2:
                    s[i][j] = 0
        for i in range(x + 2, x + 4):
            for j in range(y, y + 4):
                if s[i][j] == 2:
                    s[i][j] = 0

from __future__ import print_function
from person import *


class BomberMan(Person):

    def make(self, i, j, b):
        for k in range(i, i + 2):
            for l in range(j, j + 4):
                b[k][l] = 1

    def check(self, enemy_pos, x, y, b, life):
        for i in range(len(enemy_pos)):
            tmpx = enemy_pos[i][0]
            tmpy = enemy_pos[i][1]
            if (tmpx == x and tmpy == y):
                for i in range(x, x + 2):
                    for j in range(y, y + 4):
                        b[i][j] = 2
                x = 2
                y = 4
                self.make(2, 4, b)
                life -= 1
        return [x, y, life]

from __future__ import print_function
from person import Person


class BomberMan(Person):
    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.life = life

    def check(self, enemy_pos, b):
        for i in range(len(enemy_pos)):
            tmpx = enemy_pos[i][0]
            tmpy = enemy_pos[i][1]
            if (tmpx == self.x and tmpy == self.y):
                for i in range(self.x, self.x + 2):
                    for j in range(self.y, self.y + 4):
                        b[i][j] = 2
                self.x = 2
                self.y = 4
                self.make(self.x, self.y, b)
                self.life -= 1

from __future__ import print_function
from person import Person
import random


class Enemy(Person):
    a = 0

    def __init__(self):
        self.a = 0

    def create_enemy(self, x, y, s):
        for i in range(2):
            for j in range(4):
                s[x + i][y + j] = 2

    def gen_enemy(self, s, enemy, num, b):
        for i in range(4, 40, 2):
            if i % 4 == 0 or i % 4 == 1:
                for j in range(4, 61, 8):
                    if s[i][j] == 0 and (s[i - 1][j] == 0 or s[i + 2][j] == 0):
                        enemy.append([i, j])
            if i % 4 == 2 or i % 4 == 3:
                for j in range(4, 61, 4):
                    if s[i][j] == 0 and (s[i][j - 1] == 0 or s[i][j + 4] == 0):
                        enemy.append([i, j])

        a = random.sample(range(0, len(enemy)), num)
        en = []
        for i in a:
            self.create_enemy(enemy[i][0], enemy[i][1], b)
            en.append([enemy[i][0], enemy[i][1]])
        return en

    def move(self, enemy_pos, s, b):
        for i, l in enumerate(enemy_pos):
            tmpx = l[0]
            tmpy = enemy_pos[i][1]
            if self.check_left(tmpx, tmpy, s) == 0 or b[tmpx][tmpy - 1] == 2:
                if (self.check_right(tmpx, tmpy, s) == 0 or b[tmpx][tmpy + 4] == 2) and (b[tmpx - 1][tmpy] == 2 or self.check_up(tmpx, tmpy, s) == 0) and ((self.check_down(tmpx, tmpy, s) == 0) or b[tmpx + 2][tmpy] == 2):
                    continue
            while tmpx == enemy_pos[i][0] and tmpy == enemy_pos[i][1]:
                cx = enemy_pos[i][0]
                cy = enemy_pos[i][1]
                x = random.randint(0, 3)
                if x == 0 and b[cx][cy + 4] != 2:
                    enemy_pos[i][1] = self.moveright(
                        enemy_pos[i][0], enemy_pos[i][1], b, s, 2)
                if x == 1 and b[cx][cy - 1] != 2:
                    enemy_pos[i][1] = self.moveleft(
                        enemy_pos[i][0], enemy_pos[i][1], b, s, 2)
                if x == 2 and b[cx + 2][cy] != 5:
                    enemy_pos[i][0] = self.movedown(
                        enemy_pos[i][0], enemy_pos[i][1], b, s, 2)
                if x == 3 and b[cx - 1][cy] != 5:
                    enemy_pos[i][0] = self.moveup(
                        enemy_pos[i][0], enemy_pos[i][1], b, s, 2)

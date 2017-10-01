from __future__ import print_function


class Person():
    a = 0

    def __init__(self):
        self.a = 0

    def check_right(self, i, j, s):
        for k in range(4):
            if s[i][j + 4 + k] in [1, 4] or s[i + 1][j + 4 + k] in [1, 4]:
                return 0
        return 1

    def check_left(self, i, j, s):
        for k in range(1, 5):
            if s[i][j - k] in [1, 4] or s[i + 1][j - k] in [1, 4]:
                return 0
        return 1

    def check_up(self, i, j, s):
        for k in range(1, 3):
            for l in range(4):
                if s[i - k][j + l] in [1, 4]:
                    return 0
        return 1

    def check_down(self, i, j, s):
        for k in range(1, 3):
            for l in range(4):
                if s[i + k + 1][j + l] in [1, 4]:
                    return 0
        return 1

    def moveup(self, x, y, per, s, n):
        if self.check_up(x, y, s) == 0:
            return x
        for k in range(4):
            per[x - 2][y + k] = n
            per[x - 1][y + k] = n
            per[x][y + k] = 0
            per[x + 1][y + k] = 0
        x = x - 2
        return x

    def movedown(self, x, y, per, s, n):
        if self.check_down(x, y, s) == 0:
            return x
        for k in range(4):
            per[x + 3][y + k] = n
            per[x + 2][y + k] = n
            per[x][y + k] = 0
            per[x + 1][y + k] = 0
        x = x + 2
        return x

    def moveleft(self, x, y, per, s, n):
        if self.check_left(x, y, s) == 0:
            return y
        for k in range(2):
            for l in range(y - 4, y):
                per[x + k][l] = n
                per[x + k][l + 4] = 0
        y = y - 4
        return y

    def moveright(self, x, y, per, s, n):
        if self.check_right(x, y, s) == 0:
            return y
        for k in range(2):
            for l in range(y + 4, y + 8):
                per[x + k][l] = n
                per[x + k][l - 4] = 0
        y = y + 4
        return y

    def remove(self, x, y, b):
        for i in range(x, x + 2):
            for j in range(y, y + 4):
                b[i][j] = 0

    def make(self, i, j, b):
        for k in range(i, i + 2):
            for l in range(j, j + 4):
                b[k][l] = 1

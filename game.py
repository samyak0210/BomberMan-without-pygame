from __future__ import print_function
from board import *
from bomberman import *
from person import *
import sys
import copy
import signal
import os
from time import time
from alarmexception import *
from getchunix import *
from bomb import *
from random import randint
from brick import *
from enemy import *
getch = GetchUnix()


s = [[0 for i in range(68)] for j in range(42)]
b = copy.deepcopy(s)
arr = []
x = 2
y = 4
num_bricks = 10
num_enemy = 3
bx = 0
by = 0
flag = 0
count = 0
fl = 0
life = 3
score = 0

# brick functions
wall = []
brick = Brick()
brick.make_wall(wall)
brick.make_bricks(wall, s, num_bricks)
length = len(wall)

# bomberman
bomber = BomberMan()
bomber.make(x, y, b)

# board
board = Board()
board.makeBoard(0, s)

# bomb
bomb = Bomb()

# enemy
enemy = []
zombie = Enemy()
enemy_pos = copy.deepcopy(zombie.gen_enemy(s, enemy, num_enemy, b))
en_length = len(enemy_pos)
level = 1


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


ini_time = time.time()
# start
while True:
    curr_time = time.time()
    q = copy.deepcopy(bomber.check(enemy_pos, x, y, b, life))
    x = q[0]
    y = q[1]
    life = q[2]

    if (curr_time - ini_time >= 1):
        arr = copy.deepcopy(zombie.move(enemy_pos, s, b, x, y))
        x = arr[0]
        y = arr[1]

        if count == 0:
            if flag == 1:
                bomb.explode(bx, by, s, b, wall, enemy_pos)
                bomb.remove(bx, by, s)
                fl = 1
            flag = 0
            count = 2

        if flag == 1:
            count -= 1
        ini_time = curr_time

    if life == 0:
        bomber.remove(x, y, b)
        for i in enemy_pos:
            zombie.remove(i[0], i[1], b)

        bomb.remove(bx, by, s)

    if level == 4:
        os.system("tput reset")
        print ("Your Score is: ",score)
        print("You Win")
        sys.exit(0)
    board.printBoard(s, b, score, x, y, count, bx, by, life, level)

    if life == 0:
        os.system("tput reset")
        print("Your Score is: ", score)
        print("You Lose")
        sys.exit(0)
    if fl == 1:
        bomb.rem_expo(bx, by, s)
        score = (length - len(wall)) * 20 + (en_length - len(enemy_pos)) * 100
        if b[x][y] == 0 or b[x][y] == 2:
            bomber.make(2, 4, b)
            x = 2
            y = 4
            life -= 1
        fl = 0

    inp = input_to()

    if inp == 'w':
        x = bomber.moveup(x, y, b, s, 1)

    elif inp == 's':
        x = bomber.movedown(x, y, b, s, 1)

    elif inp == 'a':
        y = bomber.moveleft(x, y, b, s, 1)

    elif inp == 'd':
        y = bomber.moveright(x, y, b, s, 1)

    elif inp == 'q':
        os.system("tput reset")
        print("Your Score is: ", score)
        print("Thank You")
        sys.exit(0)

    elif inp == 'b':
        if flag == 0:
            bomb.place(x, y, s)
            bx = x
            by = y
            flag = 1
            count = 2

    print(" ")
    if len(enemy_pos) == 0:
        level += 1
        num_bricks += 5
        num_enemy += 4
        s = [[0 for i in range(68)] for j in range(42)]
        b = copy.deepcopy(s)
        arr = []
        x = 2
        y = 4
        bx = 0
        by = 0
        flag = 0
        count = 2
        fl = 0
        # brick functions
        wall = []
        brick = Brick()
        brick.make_wall(wall)
        brick.make_bricks(wall, s, num_bricks)
        length = len(wall)
        # bomberman
        bomber = BomberMan()
        bomber.make(x, y, b)
        # board
        board = Board()
        board.makeBoard(0, s)
        # bomb
        bomb = Bomb()
        # enemy
        enemy = []
        zombie = Enemy()
        enemy_pos = copy.deepcopy(zombie.gen_enemy(s, enemy, num_enemy, b))
        en_length = len(enemy_pos)
        ini_time = time.time()

    os.system("clear")

from __future__ import print_function
from board import Board
from bomberman import BomberMan
from person import Person
import sys
import copy
import signal
import os
import time
from alarmexception import AlarmException
from getchunix import GetchUnix
from bomb import Bomb
from random import randint
from brick import Brick
from enemy import Enemy
getch = GetchUnix()


s = [[0 for i in range(68)] for j in range(42)]
b = copy.deepcopy(s)
arr = []
num_bricks = 10
num_enemy = 3
flag = 0
count = 0
fl = 0
score = 0

# brick functions
wall = []
brick = Brick()
brick.make_wall(wall)
brick.make_bricks(wall, s, num_bricks)
length = len(wall)

# bomberman
bomber = BomberMan(2, 4, 3)
bomber.make(bomber.x, bomber.y, b)

# board
board = Board()
board.makeBoard(0, s)

# bomb
bomb = Bomb(0, 0)

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
    bomber.check(enemy_pos, b)

    if (curr_time - ini_time >= 1):
        zombie.move(enemy_pos, s, b)

        if count == 0:
            if flag == 1:
                bomb.explode(s, b, wall, enemy_pos)
                bomb.remove(s)
                fl = 1
            flag = 0
            count = 2

        if flag == 1:
            count -= 1
        ini_time = curr_time

    if bomber.life == 0:
        bomber.remove(bomber.x, bomber.y, b)
        for i in enemy_pos:
            zombie.remove(i[0], i[1], b)

        bomb.remove(s)

    if level == 4:
        os.system("tput reset")
        print("Your Score is: ", score)
        print("You Win")
        sys.exit(0)
    board.printBoard(
        s,
        b,
        score,
        bomber.x,
        bomber.y,
        count,
        bomb.bx,
        bomb.by,
        bomber.life,
        level)

    if bomber.life == 0:
        os.system("tput reset")
        print("Your Score is: ", score)
        print("You Lose")
        sys.exit(0)
    if fl == 1:
        bomb.rem_expo(s)
        score = (length - len(wall)) * 20 + (en_length - len(enemy_pos)) * 100
        if b[bomber.x][bomber.y] == 0 or b[bomber.x][bomber.y] == 2:
            bomber.make(b)
            bomber.x = 2
            bomber.y = 4
            bomber.life -= 1
        fl = 0

    inp = input_to()

    if inp == 'w':
        bomber.x = bomber.moveup(bomber.x, bomber.y, b, s, 1)

    elif inp == 's':
        bomber.x = bomber.movedown(bomber.x, bomber.y, b, s, 1)

    elif inp == 'a':
        bomber.y = bomber.moveleft(bomber.x, bomber.y, b, s, 1)

    elif inp == 'd':
        bomber.y = bomber.moveright(bomber.x, bomber.y, b, s, 1)

    elif inp == 'q':
        os.system("tput reset")
        print("Your Score is: ", score)
        print("Thank You")
        sys.exit(0)

    elif inp == 'b':
        if flag == 0:
            bomb.change(bomber.x, bomber.y)
            bomb.place(s)
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
        bomber = BomberMan(2, 4, bomber.life)
        bomber.make(b)
        # board
        board = Board()
        board.makeBoard(0, s)
        # bomb
        bomb = Bomb(0, 0)
        # enemy
        enemy = []
        zombie = Enemy()
        enemy_pos = copy.deepcopy(zombie.gen_enemy(s, enemy, num_enemy, b))
        en_length = len(enemy_pos)
        ini_time = time.time()

    os.system("clear")

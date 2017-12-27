import pygame
from time import time
from random import choice
from collections import deque

def getdrt():
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and olddrt[1] != 1:
        return (0,-1)
    elif keys[pygame.K_DOWN] and olddrt[1] != -1:
        return (0,1)
    elif keys[pygame.K_LEFT] and olddrt[0] != 1:
        return (-1,0)
    elif keys[pygame.K_RIGHT] and olddrt[0] != -1:
        return (1,0)
    else:
        return drt

def show():
    global score
    show_out = ''
    for row in layout:
        for i in row:
            show_out += shape[i]
        show_out += '\n'
    show_out += ' Score: ' + str(score)
    print('\n'*40) #more beautiful
    print(show_out)

def move(drt):
    global snake_x,snake_y
    snake_x += drt[0]
    snake_y += drt[1]
    thing = layout[snake_y][snake_x]
    layout[snake_y][snake_x] = 2
    snake.append((snake_x,snake_y))
    if thing == 0:
        go()
    elif thing == 1 or thing == 2:
        die(thing)
    elif thing == 3:
        eat()

def die(thing):
    if thing == 1:
        print('You moved into the wall!')
    elif thing == 2:
        print('You ate yourself!')
    quit()

def eat():
    global score,move_speed,food
    score += 1
    move_speed *= 0.94
    i = j = 0   #food
    while layout[j][i]:
        i = choice(range(1,width-1))
        j = choice(range(1,height-1))
    layout[j][i] = 3    #food


def go():
    i = snake.popleft()
    layout[i[1]][i[0]] = 0


#settings and initializations
width = 18
height = 20
shape = ['   ',' X ',' * ',' $ ']   #0=nothing 1=wall 2=snake 3=food
layout = [[0 for i in range(width)] for i in range(height)] #wall
for i in [0,width-1]:
    for j in range(0,height):
        layout[j][i] = 1
for i in [0,height-1]:
    for j in range(0,width):
        layout[i][j] = 1
snake_x = snake_y = 10
olddrt = drt = (1,0) #initial moving direction
snake = deque([(snake_x,snake_y)])
layout[snake_y][snake_x] = 2  #snake
layout[choice(range(1,height-1))][choice(range(1,width-1))] = 3    #food
move_speed = 0.7  #snake moves * time per second
score = 0

pygame.init()
loop = True
move_time = time()
while loop:
    drt = getdrt()
    if time() - move_time > move_speed:
        move(drt)
        show()
        olddrt = drt
        move_time = time()

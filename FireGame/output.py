from map import map

"""def shoot():
    index = None
    for num, i in enumerate(map[0]):
        if i == 1:
            index = num

    for i in range(1, len(map)):
        map[i][index] = '*'
        map[i-1][index] = 0
        try:
            if map[i+1][index] != 0:
                print(i+1)
                map[i+1][index] = 0
                map[i][index] = 0
                break
        except:
            pass

shoot()
for i in map:
    print(i)"""

import random
import time
import os

def enemy():
    for num, i in enumerate(map):
        if num == 4:
            map[random.randint(3,4)][random.randint(0,4)] = '#'

def enemy_animation():
    r = random.randint(0,4)
    lenght = len(map)
    for num, i in enumerate(map):
        time.sleep(1)
        if num >= 1:
            for x in range(lenght):
                lenght -= 1
                map[lenght][r] = '#'
                try:
                    map[lenght+1][r] = 0
                except:
                    pass

enemy_animation()


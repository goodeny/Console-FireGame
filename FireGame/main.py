from map import map
import time
import os
import keyboard
import threading
import random

pos = 0
e_pos = 4
shooting = False

def show_map():
    for i in map:
        print(i)

def game_start():
    map[0][0] = 1

def move_right():
    global pos
    try:
        if pos < 4:
            pos += 1
            map[0][pos-1] = 0
            map[0][0+pos] = 1
        print(pos)
    except:
        pass
            
def move_left():
    global pos #2
    try:
        if pos >= 1:
            pos -= 1
            map[0][pos+1] = 0
            map[0][0+pos] = 1
        print(pos)
    except:
        pass

index = 0
for num, i in enumerate(map[0]):
    if i == 1:
        index = num

def shoot():
    index = 0
    for num, i in enumerate(map[0]):
        if i == 1:
            index = num
    for i in range(1, len(map)):
        map[i][index] = "*"
        try:
            if i != 1:
                map[i-1][index] = 0
                if map[i+1][index] != 0:
                    print(i+1)
                    map[i+1][index] = 0
                    map[i][index] = 0
                    break
        except:
            pass
        os.system('cls')
        time.sleep(0.1)
        show_map()
        
def clear_map():
    for num, i in enumerate(map[4]):
        if i == '*':
            map[4][num] = 0

def enemy_animation():
    r = random.randint(0,4)
    lenght = len(map)
    for num, i in enumerate(map):
        if num >= 1:
            for x in range(lenght):
                lenght -= 1
                map[lenght][r] = 2
                try:
                    map[lenght+1][r] = 0
                    #os.system('cls')
                    #show_map()
                    time.sleep(0.5)
                except:
                    pass

game_start()

def game_update():
    global shooting 

    if keyboard.is_pressed('d'):
        move_right()
    if keyboard.is_pressed('a'):
        move_left()
    if keyboard.is_pressed('space'):
        shooting = True
    
    if shooting:
        threading.Thread(target=shoot()).start()
        shooting = False

    time.sleep(0.1)
    os.system('cls')
    show_map()
    clear_map()

while True:
    threading.Thread(target=enemy_animation).start()
    game_update()
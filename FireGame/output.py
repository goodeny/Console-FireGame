from map import map

def shoot():
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
    print(i)

     
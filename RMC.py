from random import randint  # For rooms

def fillRect(grid: list, x: int, y: int, w: int, h: int, fill: str = "*") -> list:
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[j][i] = fill
    return grid

def rect(grid: list, x: int, y: int, w: int, h: int, stroke: str = "#") -> list:
    for i in range(x, x + w):
        grid[i][y] = stroke
    for i in range(x, x + w):
        grid[i][y + h - 1] = stroke
    for i in range(y, y + h):
        grid[x][i] = stroke
    for i in range(y, y + h):
        grid[x + w - 1][i] = stroke

    return grid

def line(grid: list, x: int, y: int, tx: int, ty: int, stroke: str = "*") -> list:
    #print("line: ", end="")  # Debug
    #print([x, y, tx, ty])
    if max(tx - x, x - tx) >= max(ty - y, y - ty):  # If distance between tx and x >= distance between ty and y
        for i in range(min(x, int((x+tx)/2)), max(x, int((x+tx)/2))+1):
            grid[y][i] = stroke
        for i in range(min(y, ty), max(y, ty+1)):
            grid[i][int((x+tx)/2)] = stroke
        for i in range(min(int((x+tx)/2), tx+1), max(int((x+tx)/2), tx+1)):
            grid[ty][i] = stroke
    else:
        for i in range(min(y, int((y+ty)/2)), max(y, int((y+ty)/2)+1)):
            grid[i][x] = stroke
        for i in range(min(x+1, tx+1), max(x+1, tx+1)):
            grid[int((y+ty)/2)][i] = stroke
        for i in range(min(int((y+ty)/2), ty), max(int((y+ty)/2)+1, ty+1)):
            grid[i][tx] = stroke
    return grid

def createMap(x: int, y: int, wall: str = "#", air: str = "*") -> dict:
    grid: list = []
    for ci in range(y):  # Fill grid
        grid.append([])
        for cj in range(x):
            grid[ci].append(wall)
    num_of_rooms = 0
    brx = 0
    bry = 0
    bw = 0
    bh = 0
    while True:
        if randint(0, 100) < num_of_rooms*2000/x/y and num_of_rooms > 1:  # Then, create room
            break
        rx = randint(0, x-1)
        ry = randint(0, y-1)
        w = randint(1, min(x-rx, 5))
        h = randint(1, min(y-ry, 5))
        grid = fillRect(grid, rx, ry, w, h, air)
        if num_of_rooms > 0:
            grid = line(grid, int((rx*2+w)/2), int((ry*2+h)/2), int((brx*2+bw)/2), int((bry*2+bh)/2), air)
        #print("gen: "+str(num_of_rooms))  # Debug
        #for i in range(len(grid)):
        #    for j in range(len(grid[i])):
        #        print(grid[j][i], end="")
        #    print()
        #print([rx, ry, w, h]) # Debug
        #print([brx, bry, bw, bh])
        #print()

        brx = rx
        bry = ry
        bw = w
        bh = h
        num_of_rooms += 1
    return {'grid': grid, 'num_of_rooms': num_of_rooms}


if __name__ == "__main__":
    a = createMap(20, 20, "S", "~")
    grid = a['grid']
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[j][i], end="")
        print()
    print("num of rooms: " + str(a['num_of_rooms']))
    exit(0)

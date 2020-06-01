from random import randint  # For rooms

# =====================
#  Name: RMG (rouge map creator)
#  Author: KseandI
#  Version: 0.0.1
#  Made: with love and for Liqerty Team
# =====================

def fillRect(grid: list, x: int, y: int, w: int, h: int, fill: str = "~") -> list:
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[i][j] = fill
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


def createMap(x: int, y: int, wall: str = "#", air: str = "*") -> dict:
    grid: list = []
    for ci in range(y):  # Fill grid
        grid.append([])
        for cj in range(x):
            grid[ci].append(wall)
    num_of_rooms = 0
    while True:
        if randint(0, 100) < num_of_rooms*2000/x/y and num_of_rooms > 1:  # Then, create room
            break
        rx = randint(0, x-1)
        ry = randint(0, y-1)
        w = randint(1, x-rx)
        h = randint(1, y-ry)
        grid = fillRect(grid, rx, ry, w, h, air)
        num_of_rooms += 1
    return {'gird': grid, 'num_of_rooms': num_of_rooms}


if __name__ == "__main__":
    a = createMap(20, 20, "S", "~")
    gird = a['gird']
    for i in range(len(gird)):
        for j in range(len(gird[i])):
            print(gird[j][i], end="")
        print()
    print("num of rooms: " + str(a['num_of_rooms']))
    exit(0)

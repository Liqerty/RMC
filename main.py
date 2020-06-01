# =====================
#  Name: RMG (rouge map creator)
#  Author: KseandI
#  Version: 0.0.1
#  Made: with love and for Liqerty Team
# =====================

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


def createMap(x: int, y: int, wall: str = "#", air: str = "*") -> list:
    grid: list = []
    for ci in range(y):  # Fill grid
        grid.append([])
        for cj in range(x):
            grid[ci].append(air)
    grid = rect(grid, 2, 2, 5, 5, wall)
    return grid


if __name__ == "__main__":
    a = createMap(20, 20, "S", "~")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[j][i], end="")
        print()
    exit(0)

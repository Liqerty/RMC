
# =====================
#  Name: RMG (rouge map creator)
#  Author: KseandI
#  Version: 0.0.1
#  Made: with love and for Liqerty Team
# =====================

def createMap(x: int, y: int) -> list:
    grid: list = []
    for ci in range(y):
        grid.append([])
        for cj in range(x):
            grid[ci].append("*")
    return grid


if __name__ == "__main__":
    a = createMap(20, 20)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end="")
        print()
    exit(0)

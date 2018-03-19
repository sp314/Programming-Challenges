def ShebaAmoeba():
    dimensions = list(map(int, input().split()))
    y = dimensions[0]
    x = dimensions[1]
    loops = 0

    dish = [list(input()) for rows in range(y)]

    for row in range(y):
        for col in range(x):
            if dish[row][col] == "#":
                posX = col
                posY = row
                while True:
                    AmoebaDelete(posY, posX, dish)
                    point = findNeighborPoint(posX, posY, y, x, dish)
                    if point != None:
                        posX = point[1]
                        posY = point[0]
                    else:
                        loops += 1
                        break

    return loops


def findNeighborPoint(cx, cy, m, n, dish):
    for x in range(cx -1, cx + 2):
        if 0 <= x < n:
            for y in range(cy - 1, cy + 2):
                if 0 <= y < m:
                    if dish[y][x] == "#":
                        pointtup = (y,x)
                        return pointtup
                    else:
                        continue

    return None

def AmoebaDelete(y, x, dish):
    dish[y][x] = "."

print(ShebaAmoeba())
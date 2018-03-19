def createTileMap(quad_key):
    dimen = 2 ** len(quad_key)
    tile_map = [0,dimen,0,dimen]
    return tile_map

def Quad0(tile_map):
    x_dist = tile_map[1] - tile_map[0]
    y_dist = tile_map[3] - tile_map[2]

    tile_map[1] -= x_dist/2
    tile_map[3] -= y_dist/2
    return tile_map


def Quad1(tile_map):
    x_dist = tile_map[1] - tile_map[0]
    y_dist = tile_map[3] - tile_map[2]

    tile_map[0] += x_dist/2
    tile_map[3] -= y_dist/2
    return tile_map


def Quad2(tile_map):
    x_dist = tile_map[1] - tile_map[0]
    y_dist = tile_map[3] - tile_map[2]

    tile_map[1] -= x_dist/2
    tile_map[2] += y_dist/2
    return tile_map


def Quad3(tile_map):
    x_dist = tile_map[1] - tile_map[0]
    y_dist = tile_map[3] - tile_map[2]

    tile_map[0] += x_dist/2
    tile_map[2] += y_dist/2
    return tile_map

def findTile(quad_key):
    tile_map = createTileMap(quad_key)



    for entry in quad_key:
        if int(entry) == 0:
            Quad0(tile_map)
        elif int(entry) == 1:
            Quad1(tile_map)
        elif int(entry) == 2:
            Quad2(tile_map)
        elif int(entry) == 3:
            Quad3(tile_map)

    return tile_map

quad_key = input()
tile_map = findTile(quad_key)
print(len(quad_key), int(tile_map[0]), int(tile_map[2]))

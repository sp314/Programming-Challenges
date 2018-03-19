def FindKnightPos(dimensions):
    chessBoard = [list(input()) for row in range(dimensions)]
    knights = sum(row.count('k') for row in chessBoard)
    coord = []

    if knights != 9:
        coord = [[0, 0], [2, 1]]
    else:
        for row in range(len(chessBoard)):
            for columnEntry in range(len(chessBoard[row])):
                if (chessBoard[row][columnEntry] == "k"):
                    coord.append([columnEntry, row])
    return coord



def IsValidConfig(coordinateArray):
    isValid = ""
    for coordset in range(len(coordinateArray)):
        x = int(coordinateArray[coordset][0])
        y = int(coordinateArray[coordset][1])

        if [x + 2, y + 1] in coordinateArray:
            isValid = "invalid"
        elif [x + 2, y - 1] in coordinateArray:
            isValid = "invalid"

        elif [x - 2, y + 1] in coordinateArray:
            isValid = "invalid"
        elif [x - 2, y - 1] in coordinateArray:
            isValid = "invalid"

        elif [x + 1, y + 2] in coordinateArray:
            isValid = "invalid"
        elif [x + 1, y - 2] in coordinateArray:
            isValid = "invalid"

        elif [x - 1, y + 2] in coordinateArray:
            isValid = "invalid"
        elif [x - 1, y - 2] in coordinateArray:
            isValid = "invalid"
        else:
            isValid = "valid"

    print(isValid)

IsValidConfig(FindKnightPos(5))

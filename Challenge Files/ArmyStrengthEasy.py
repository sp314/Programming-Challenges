def WarWinner():
    testCases = int(input())
    for case in range(testCases):
        blankLine = input()
        armySizes = list(map(int, input().split()))
        godzillaArmy = list(map(int, input().split()))
        mechaArmy = list(map(int, input().split()))

        if(max(godzillaArmy) < max(mechaArmy)):
            print("MechaGodzilla")
        else:
            print("Godzilla")

WarWinner()
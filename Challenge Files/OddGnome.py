def OddGnome():
    gnomeInput = input()
    gnomeList = gnomeInput.split()
    gnomeList = [int(i) for i in gnomeList]
    for i in range(1,len(gnomeList) -1):
        if gnomeList[i] != gnomeList[i +1] -1:
            kingGnomePos = i
    return kingGnomePos

def RunOddGnomeCase():
    GnomeCases = int(input())
    for case in range(GnomeCases):
        print(OddGnome())

RunOddGnomeCase()
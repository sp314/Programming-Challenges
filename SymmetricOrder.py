n = 1
names = 1
while 1:
    names = int(input())
    if names == 0:
        break
    nameList = [input() for entry in range(names)]
    OddList = nameList[::2]
    EvenList = nameList[1::2]
    finalNameList = OddList + EvenList[::-1]
    print("SET", str(n))
    print("\n".join(finalNameList))
    n += 1
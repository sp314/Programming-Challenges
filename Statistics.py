Xcount = 0
while True:
    X = input()
    Xcount += 1
    if X != '':
        Xlist = list(map(int, X.split()[1:]))
        print("Case " + str(Xcount) + ":", str(min(Xlist)), str(max(Xlist)), str((max(Xlist)) - min(Xlist)))
    else:
        
        break

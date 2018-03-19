def Helpaphd():
    tc = int(input())
    for case in range(tc):
        problem = input()
        if problem != "P=NP":
            print(int(problem[0]) + int(problem[2]))
        else:
            print("skipped")

Helpaphd()
while(True):
    events = int(input())

    if(events == 0):
        break

    times = [(input().replace(':',' ').split()) for event in range(events)]
    times.sort(key= lambda tup: tup[2])
    AMtimes = [times[i] for i in range(len(times)) if times[i][2] == 'a.m.']
    PMtimes = [times[i] for i in range(len(times)) if times[i][2] == 'p.m.']

    for time in AMtimes:
        if(int(time[0]) == 12):
            time[0] = '0'

    AMtimes.sort(key=lambda tup: (int(tup[0]), int(tup[1])))
    for time in AMtimes:
        if(int(time[0]) == 0):
            time[0] = '12'

    for time in PMtimes:
        if(int(time[0]) == 12):
            time[0] = '0'

    PMtimes.sort(key=lambda tup: (int(tup[0]), int(tup[1])))
    for time in PMtimes:
        if(int(time[0]) == 0):
            time[0] = '12'

    AMtimes.extend(PMtimes)
    for timeEvent in AMtimes:
        print(timeEvent[0] + ":" + timeEvent[1] + " " + timeEvent[2])
    print("")


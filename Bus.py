cases = int(input())
for case in range(cases):
    stops = int(input())
    passengers = 0
    for stop in range(stops):
        passengers = passengers*2 + 1
    print(passengers)

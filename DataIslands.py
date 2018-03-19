def sub_lists(lst):
    subs = []
    for start in range(len(lst) - 2):
        end = start + 3
        while(end <= len(lst)):
            subs.append(lst[start:end])
            end += 1
    return subs

cases = int(input())
for case in range(cases):
    islands = 0
    data_stream = list(map(int, input().split()))
    data_subs = sub_lists(data_stream)

    for possible_island in range(len(data_subs)):
        minimum = max(data_subs[possible_island][0], data_subs[possible_island][-1])
        is_island = True

        for i in data_subs[possible_island][1:-1]:
            if i <= minimum:
                is_island = False
                break
        if(is_island):
            islands += 1
    print(case + 1, islands)






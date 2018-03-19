edges = int(input())
raw_edge_info = [list(map(int, input().split())) for edge in range(edges - 1)]
ant_water = list(map(int, input().split()))
print(raw_edge_info)
print(ant_water)


tree = []
for data in range(len(raw_edge_info)):
    start = raw_edge_info[data][0] - 1
    end = raw_edge_info[data][1]
    fraction = raw_edge_info[data][2]
    powers = raw_edge_info[data][3]


    try:
        tree[start].append({end: (fraction, powers)})
    except IndexError:
        tree.insert(start, [{end: (fraction, powers)}])

print(tree)
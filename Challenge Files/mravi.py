# Input
# The first line of input contains the integer N (1≤N≤1000).
#
# Each of the following N−1 lines contain four integers Ai, Bi, Xi, Ti (1≤Ai,Bi≤N, 1≤Xi≤100, 0≤Ti≤1) where Ai and Bi are the ends of a pipe (the labels of nodes connected by the pipe), Xi is the flow of the liquid through the pipe, and Ti denotes whether the pipe has a superpower. If Ti is 1, that pipe has a superpower, otherwise it does not.
#
# The following line contains N integers Ki describing the amount of liquid needed for the ants in the i-th node. If the i-th node is not a leaf, Ki will be −1, otherwise it will be an integer from the interval [1,10].
#
# Output
# The first and only line of output must contain the required number from the task. Please note: The allowed absolute error from the correct (precise) solution is 0.001.
#

edges = int(input())
raw_edge_info = [list(map(int, input().split())) for edge in range(edges - 1)]
ant_water = list(map(int, input().split()))
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
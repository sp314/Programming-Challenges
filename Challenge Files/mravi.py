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

lines = int(input())
edge_info = [list(map(int, input().split())) for edge in range(lines - 1)]
ant_water = list(map(int, input().split()))
parent_node = 0 #default parent node
nodes = [edge[1] for edge in edge_info]
nodes = max(nodes)

#Creates non-directional adjacency list
adjacency_list = [[] for node in range(nodes)]
for edge in edge_info:
    first = edge[0]
    second = edge[1]

    first_second = {edge[1]:(edge[2], edge[3])}
    second_first = {edge[0]: (edge[2], edge[3])}

    adjacency_list[first - 1].append(first_second)
    adjacency_list[second - 1].append(second_first)


# sets parent node based on which node has a 100 weight in its edges and is not a leaf
# (according to last line in input)
for node in range(len(adjacency_list)):
    node_weight_total = 0
    for edge in range(len(adjacency_list[node])):
        edge_weight = list(adjacency_list[node][edge].values())[0][0]
        node_weight_total += edge_weight
    if node_weight_total == 100 and ant_water[node] == -1:
        parent_node = node  + 1


#Creates directed adjacency list with edges coming from CHILD
child_list = [node for node in range(nodes)]
for edge in edge_info:
    second = edge[1]

    second_first = {edge[0]: (edge[2], edge[3])}

    child_list[second - 1] =  second_first


#List of tuples representing each leaf and the amount of water they need
leaves = [((index + 1), ant_water[index]) for index in range(len(ant_water)) if ant_water[index] != -1]

#List of each leaf's list of multipliers racked up by travelling UP from the particular leaf to the parent node
multiplier_list = [[] for leaf in leaves]
for leaf in range(len(leaves)):
    current_leaf = leaves[leaf][0]

    while(current_leaf != parent_node):
        super = list(child_list[current_leaf - 1].values())[0][1]
        if super == 1:
            multiplier_list[leaf].append("square")

        multiplier = list(child_list[current_leaf - 1].values())[0][0]/100
        multiplier_list[leaf].append(multiplier)
        current_leaf = list(child_list[current_leaf - 1].keys())[0]

liter_list = []
#creates a list of the solved for minimum liters needed for each leaf
for leaf in range(len(multiplier_list)):
    liters = leaves[leaf][1]
    for operation in multiplier_list[leaf]:
        if operation == "square":
            liters = liters ** (1/2)
        else:
            liters /= operation
    liter_list.append(liters)
#prints out the largest number of within liter_list to the 3rd decimal place
print(format(max(liter_list), ".3f"))
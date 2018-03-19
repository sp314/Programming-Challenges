our_input = []
while(len(our_input) < 8):
    input_line = list(map(int, input().split()))
    our_input.extend(input_line)


box_heights = our_input[:6]
box_heights.sort(reverse=True)

tower1 = our_input[6]
tower2 = our_input[7]

sum_permute_tower1 = [[i, j, k, (i + j + k)] for i in box_heights for j in box_heights for k in box_heights if (i + j + k == tower1) and (i != j) and (i != k) and (j != k)][0][:3]

for num in range(len(sum_permute_tower1)):
    box_heights.remove(sum_permute_tower1[num])

sum_permute_tower1.extend(box_heights)
print(*sum_permute_tower1, sep=" ")
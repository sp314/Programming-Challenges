stone_list = list(input())
num_stones = len(stone_list)
white_stones = 0
for stones in range(num_stones):
    if stone_list[stones] == 'W':
        white_stones += 1

if white_stones == num_stones/2:
    print(1)
else:
    print(0)

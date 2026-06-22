matrix = []
for x in range(5):
    arr = list(map(int, input().split()))
    matrix.append(arr)

position_one = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            position_one.append(i+1)
            position_one.append(j+1)

# a_line = 0
# b_column = 0
# if position_one[1] > 3:
#     b_column = position_one[1] - 3
# elif position_one[1] < 3:
#     b_column = 3 - position_one[1]
# if position_one[0] > 3:
#     a_line = position_one[0] - 3
# elif position_one[0] < 3:
#     a_line = 3 - position_one[0]

# print(a_line+b_column)

## Cara yg lebih cepat
if position_one[0] == 3 and position_one[1] == 3:
    print(0)
else:
    print(abs(position_one[0] - 3) + abs(position_one[1] - 3))
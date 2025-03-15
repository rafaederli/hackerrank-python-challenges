# List Comprehensions
x = 1
y = 1
z = 2
n = 3

range_x = range(x + 1)
range_y = range(y + 1)
range_z = range(z + 1)

coor = [[i, j, k] for i in range_x for j in range_y for k in range_z if (i + j + k) != n]

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if (i + j + k) != n:
#                 coor.append([i, j, k])

print(coor)
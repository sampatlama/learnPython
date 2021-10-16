'''
[1,2,3],
[4,5,6],   <== 3*3 matrix
[7,8,9]

[[1, 2, 3, 4],
 [5, 6, 7, 8],    <== 4*4 matrix
[9, 10, 11, 12],
[13, 14, 15, 16]
]

'''
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]
          ]
ram = matrix[0][3]
matrix[0][3] = 6
print(matrix[2][3])
print(ram)
for row in matrix:
    for item in row:
        print(item)
# accessing the lists of matrix elements
# or 2d lists

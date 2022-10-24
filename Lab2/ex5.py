def newMatrix(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            matrix[i][j] = 0
    return matrix

mtr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

for line in mtr:
    print ('  '.join(map(str, line)))
    
mtr = newMatrix(mtr)
print('\n')

for line in mtr:
    print ('  '.join(map(str, line)))
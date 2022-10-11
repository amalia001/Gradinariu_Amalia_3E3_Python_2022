# Given a square matrix of characters write a script that prints the string obtained by going
# through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7


def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row - 1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir = 0

    while (top <= bottom and left <= right):
        if dir == 0:
            for i in range(left, right + 1):  # moving left->right
                print(arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top += 1
            dir = 1

        elif dir == 1:
            for i in range(top, bottom + 1):  # moving top->bottom
                print(arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -= 1
            dir = 2

        elif dir == 2:
            for i in range(right, left - 1, -1):  # moving right->left
                print(arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -= 1
            dir = 3

        elif dir == 3:
            for i in range(bottom, top - 1, -1):  # moving bottom->top
                print(arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left += 1
            dir = 0


array = [["f", "i", "r", "s"],
          ["n", "_", "l", "t"],
          ["o", "b", "a", "_"],
          ["h", "t", "y", "p"]]

spiralMatrixPrint(4, 4, array)
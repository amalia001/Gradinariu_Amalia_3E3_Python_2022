def places(matrix):
    listOfTuples = []
    for i in range(0, len(matrix[0])):  # parsing the columns
        maxValue = 0
        for j in range(0, len(matrix)):  # parsing the rows
            if matrix[j][i] > maxValue:
                maxValue = matrix[j][i]
            elif matrix[j][i] <= maxValue:  # shorter or same height
                listOfTuples.append((j, i))
    return listOfTuples


matrix = [[1, 2, 3, 2, 1, 1],

          [2, 4, 4, 3, 7, 2],

          [5, 5, 2, 5, 6, 4],

          [6, 6, 7, 6, 7, 5]]

print(places(matrix))
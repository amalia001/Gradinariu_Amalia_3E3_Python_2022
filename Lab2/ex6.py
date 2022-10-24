#  1. Write a function to return a list of the first n numbers in the Fibonacci string.
import json
from collections import Counter
#from typing import re


def ex1(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return ex1(num - 2) + ex1(num - 1)


n = 7
thelist=[]
for i in range(0, n):
    thelist.append(ex1(i))
print(thelist)


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def ex2(number_list):
    new_list = []
    for nr in number_list:
        if (isPrime(nr)):
            new_list.append(nr)
    print(new_list)


l = [1, 2, 3, 4, 5, 6, 7, 8]
ex2(l)


# 3. Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def ex3(a, b):
    print('A U B = ', a.union(b))
    print("Intersection:", a.intersection(b))
    print("a-b: ", a.difference(b))
    print("b-a: ", b.difference(a))


x = {4, 5, 6, 7, 8}
y = {5, 6, 8, 9, 0}
ex3(x, y)


# 4. Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer). The function will return the song
# composed by going though the musical notes beginning with the start position and following the
# moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return
# 	["mi", "fa", "do", "sol", "re"]

def compose(list_musical_notes, list_moves, start_position):
    composition = list()
    composition.append(list_musical_notes[start_position])
    current_position = start_position
    for move in list_moves:
        current_position = current_position + move
        if current_position in range(0, len(list_musical_notes)):
            composition.append(list_musical_notes[current_position])
        while current_position > len(list_musical_notes):
            current_position = current_position - len(list_musical_notes)
            if current_position > len(list_musical_notes):
                continue
            composition.append(list_musical_notes[current_position])
        while current_position < 0:
            current_position = len(list_musical_notes) - current_position
            if current_position < 0:
                continue
            composition.append(list_musical_notes[current_position])

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by
# replacing all the elements under the main diagonal with 0 (zero).

def ex5(matrix, m, n):
    for i in range(0, n):
        for j in range(0, m):
            if i > j:
                matrix[i][j] = 0
    return matrix


rows = 3
cols = 3
mat = [[0 for x in range(cols)] for y in range(rows)]
mat[0][0], mat[0][1], mat[0][2] = 1, 2, 3
mat[1][0], mat[1][1], mat[1][2] = 4, 5, 6
mat[2][0], mat[2][1], mat[2][2] = 7, 8, 9

print(ex5(mat, rows, cols))


# 6.  Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ]
# 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

def appearances(x, *large_list):
    finalList = set()
    allElementsArray = []
    for list in large_list:
        for element in list:
            allElementsArray.append(element)
    for element in allElementsArray:
        if allElementsArray.count(element) == x:
            finalList.add(element)
    return finalList

list1 = [1, 2, 3, 4, 1, 2, 3, 4]
list2 = [6, 7, 8]
list3 = [7, 78, 9]
list4 = [10, 11, 12, 1]
print(appearances(2, list1, list2, list3, list4))


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple
# with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the
# list and the second element will be the greatest palindrome number.

def isPalindrome(num):
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return True
    else:
        return False


def ex7(number_list):
    max = number_list[0]
    palindromes = 0
    for x in number_list:
        if (isPalindrome(int(x))):
            palindromes += 1
            if int(x) > max:
                max = int(x)
    my_tuple = (palindromes, max)
    return my_tuple


lista = [11211, 65, 99499, 0, 434, 215]
print(ex7(lista))


# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a
# boolean flag set to True. For each string, generate a list containing the characters that have the
# ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that
# have the ASCII code not divisible by x.

# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" .
# Note: The function must return list of lists.

def ex8(string_list, x=1, flag=True):
    new_list = []
    for word in string_list:
        char_list = []
        if flag == True:
            for letter in word:
                if ord(letter) % x == 0:
                    char_list.append(letter)
        else:
            for letter in word:
                if ord(letter) % x != 0:
                    char_list.append(letter)
        new_list.append(char_list)
    print(new_list)


lista = ["test", "hello", "lab002"]
ex8(lista, 2, False)


# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators
# in a stadium and will return a list of tuples (line, column) each one representing a seat of a
# spectator which can't see the game. A spectator can't see the game if there is at least one
# taller spectator standing in front of him. All the seats are occupied. All the seats are at the
# same level. Row and column indexing starts from 0, beginning with the closest row from the field.
#
# 	Example:
# # FIELD
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]]
# Will return : [(2, 2), (3, 4), (2, 4)]

import numpy

def check_spectators_heights(seats):
    transpose = numpy.transpose(seats)

    result_ = list()
    for i in range(len(transpose)):
        maximum_height = transpose[i][0]

        for j in range(len(transpose[i])):
            if transpose[i][j] < maximum_height:
                result_.append((j, i))

            elif transpose[i][j] > maximum_height:
                maximum_height = transpose[i][j] + 1
    return result_


rows = 3
cols = 2
mat = [[0 for _ in range(cols)] for _ in range(rows)]
mat[0][0], mat[0][1] = 1, 2
mat[1][0], mat[1][1] = 4, 3
mat[2][0], mat[2][1] = 1, 2
print(mat)

print(check_spectators_heights(mat))


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the
# position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ")
# ,(2, 6, "b"), (3,7, "c")].


def ex10(matrix_):
    transpose = numpy.transpose(matrix_)
    print(transpose)
    result_ = [tuple(list__) for list__ in transpose]
    return result_

ceva=[[1,2,3], [5,6,7], ["a", "b", "c"]]
print(ex10(ceva))


# 11. Write a function that will order a list of string tuples based on the 3rd character of the
# 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sort_rule(tuple_):
    return tuple_[1][2]

def ex11(input_):
    input_.sort(key=sort_rule)
    return input_

ceva=[('abc', 'bcd'), ('abc', 'zza')]
print(ex11(ceva))

# 12. Write a function that will receive a list of words  as parameter and will return a list of lists
# of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
# Ex.:  group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'],
# ['carte', 'parte'], ['arme']]

def ex12(words):
    d = {}
    for word in words:
        if word[-2:] in d:
            d[word[-2:]].append(word)
        else:
            d[word[-2:]] = [word]

    print(d)
    return [list_[1] for list_ in d.items()]

print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))
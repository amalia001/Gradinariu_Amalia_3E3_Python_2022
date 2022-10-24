def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def reunion(lst1, lst2):
    return list(set(lst1) | set(lst2))

def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def reversedDifference(lst1, lst2):
    return list(set(lst2) - set(lst1))
 
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [7, 8, 9, 10, 11, 12, 13, 14, 15]
print(intersection(lst1, lst2))
print(reunion(lst1, lst2))
print(difference(lst1, lst2))
print(reversedDifference(lst1, lst2))

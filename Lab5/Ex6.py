#  Write a function that receives a list with integers as parameter that contains an equal number
#  of even and odd numbers that are in no specific order. The function should return a list of pairs
#  (tuples of 2 elements) of numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi
#  is the i-th odd number

def function6(lst):
    odds=[]
    evens=[]
    pairs=[]
    for el in lst:
        if el % 2 == 0:
            evens.append(el)
        else:
            odds.append(el)
    for (x, y) in zip(evens, odds):
        pairs.append((x,y))
    return pairs

l=[1,3,5,2,8,7,4,10,9,2]
print(function6(l))

#Write a function with one parameter which represents a list. The function will return a new list
# containing all the numbers found in the given list.

def function5(lst):

    new_lst = []
    for el in lst:
        if type(el) in [int, float, complex]:
            new_lst.append(el)
    return new_lst

print(function5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
# 2. Create a function and an anonymous function that receive a variable number of arguments.
# Both will return the sum of the values of the keyword arguments.
# Example:  For the call my_function(1, 2, c=3, d=4) the returned value will be 7.


def mysum(*args, **kwargs):
    s = 0
    for k, v in kwargs.items():
        s += v
    return s


# print(mysum(1, 2, c=3, d=4))


anom_function = lambda *args, **kwargs: sum([val for val in kwargs.values()])
print(anom_function(1, 2, c=3, d=4))

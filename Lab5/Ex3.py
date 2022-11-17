# Using functions, anonymous functions, list comprehensions and filter, implement three methods to
# generate a list with all the vowels in a given string.
# Ex: For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].

def ex3(string):
    def returnVowels(string):
        return [ch for ch in string if ch.lower() in "aeiou"]
    first_list = returnVowels(string)

    anon_function = lambda string: [ch for ch in string if ch.lower() in "aeiou"]
    second_list = anon_function(string)

    f_filter = lambda string: list(filter(lambda x: x.lower() in "aeiou", string))
    third_list = f_filter(string)

    return first_list, second_list, third_list

text="Programming in Python is fun"
print(ex3(text))

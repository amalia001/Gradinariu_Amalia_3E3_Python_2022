#Write a function that extract a number from a text
# (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.


import re
def extract(s):
    temp = re.findall(r'\d+', s)
    res = list(map(int, temp))
    print(str(res[0]))


extract("An apple is 123 66 USD")
extract("abc123abc")
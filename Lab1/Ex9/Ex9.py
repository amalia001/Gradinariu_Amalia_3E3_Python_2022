#Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato", then the most common character is "a"
# (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered
# "A" and "a" represent the same character.

def most_common_letter(text):
    letters=dict()
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    max_key = max(letters, key=letters.get)
    return max_key

print(most_common_letter("an apple is not a tomato"))

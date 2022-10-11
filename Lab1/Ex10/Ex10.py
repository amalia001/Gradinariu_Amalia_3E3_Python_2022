#Write a function that counts how many words exists in a text. A text is considered to be form out
# of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def how_many_words(text):
    text=text.split(' ')
    print("Textul are {} cuvinte".format(len(text)))

how_many_words("I have Python exam")
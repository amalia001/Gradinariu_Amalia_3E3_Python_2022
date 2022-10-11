#Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def countOnes(n):
    binary=bin(n)[2:]
    print(binary)
    print(binary.count("1"))

countOnes(24)

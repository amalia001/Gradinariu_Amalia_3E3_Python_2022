# Write a script that receives two strings and prints the number of occurrences of the first string
# in the second.

def occNumber(s1, s2):
    count = 0
    sub_len = len(s1)
    for i in range(len(s2)):
        if s2[i:i + sub_len] == s1:
            count += 1
    return count


print(occNumber("aa", "aamaaliaa") )
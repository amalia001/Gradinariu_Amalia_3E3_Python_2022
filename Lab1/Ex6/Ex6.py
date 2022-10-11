#Write a function that validates if a number is a palindrome.

def isPalindrome(s):
    return s == s[::-1]

cuvant="eraotiparapitoare"
pe_dos=isPalindrome(cuvant)
if(pe_dos):
    print("Este palindrom")
else:
    print("Nu este palindrom")


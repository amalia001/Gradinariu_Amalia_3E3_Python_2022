def isNumberPalindrome(number: int):
    ok = True
    copyNumber = number
    numberOfZeros = 0
    while copyNumber != 0:
        copyNumber //= 10
        numberOfZeros += 1

    while number != 0 and ok == True:
        leftNumber = number//(10 ** (numberOfZeros-1))
        rightNumber = number % 10
        if leftNumber == rightNumber:
            number -= leftNumber * (10 ** (numberOfZeros-1))
            number //= 10
            numberOfZeros -= 2
        else:
            ok = False
    return ok


def myPalindromeFunction(list):
    counter = 0
    maxNumber = -1
    for element in list:
        if isNumberPalindrome(element):
            counter += 1
            if element > maxNumber:
                maxNumber = element
    return counter, maxNumber
    
    
list = [121, 112, 38, 484, 100, 997, 12321]
print(myPalindromeFunction(list))
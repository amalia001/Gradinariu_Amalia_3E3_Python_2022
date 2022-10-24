def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def checkForPrimes(numbersList):
    numbers = []
    for number in numbersList:
        if is_prime(number):
            numbers.append(number)
    return numbers

myNumbersList = [ 5, 10, 20, 11, 8, 7]
print(checkForPrimes(myNumbersList))
# Ex 1. a) Write a module named utils.py that contains one function called process_item. The function will have one
# parameter, x, and will return the least prime number greater than x. When run, the module will request an input from the user,
# convert it to a number and it will display the output of the process_item function.





def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def process_item(x):
    ok = 0
    while ok == 0:
        x = x + 1
        if is_prime(x):
            ok = 1
    return x

if __name__ == "__main__":
    print("hei")
    number = input("Please enter a number: ")
    number = int(number)
    print("the smallest prime number greater than ", number, "is: ")
    print(process_item(number))


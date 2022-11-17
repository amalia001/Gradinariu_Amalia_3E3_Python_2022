# 1. b) Write a module named app.py. When this module is run, it will run in an infinite loop, waiting for inputs from
# the user. The program will convert the input to a number and process it using the function process_item implented in utils.py.
# You will have to import this function in your module. The program stops when the user enters the message "q".

import utils as ut

while (1):
    user_input = input("Enter input: ")
    if user_input == "q":
        break
    else:
        number = int(user_input)
        processed_item = ut.process_item(number)
        print("Processed item : ")
        print(processed_item)

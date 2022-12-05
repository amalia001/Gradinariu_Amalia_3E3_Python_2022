import datetime
import calendar
import csv
import math
import pandas as pd

currentInventory = list(csv.reader(open("./InventarCurent.csv")))
salesHistory = list(csv.reader(open("./IstoricVanzari.csv")))
products_list = ["Concelear", "Foundation", "Blush", "MakeUp Palette", "Primer", "Powder",
                 "Setting Spray", "Eyeliner", "Bronzer", "Brow Kit", "Highlighter", "Glitter",
                 "Lipstick", "Lipgloss", "Eyelashes"]


def days_in_inventory(year=datetime.datetime.now().year):
    return 365 + calendar.isleap(year) - 31


def howManySoldPerDay():
    total_number_of_days = days_in_inventory()
    salesDict = dict()
    product_index = 0
    for row in range(1, 16):
        productStock = 0
        for column in range(1, 12):
            productStock += int(salesHistory[row][column])
        salesDict[products_list[product_index]] = math.ceil(productStock / total_number_of_days)
        product_index += 1
    # pprint(salesDict)
    return salesDict


def necessaryStock(period_of_time_in_days):
    sales_per_day = howManySoldPerDay()
    products_needed_in_total = dict()
    products_to_order = dict()
    product_index = 1
    for product in sales_per_day.keys():
        x = int(period_of_time_in_days)
        total = sales_per_day[product] * x
        # products_needed_in_total[product] = total
        products_to_order[product] = total - int(currentInventory[product_index][1])
        product_index += 1
        # print(products_needed_in_total[product])
        # products_needed_in_total[product] = sales_per_day[product] * period_of_time_in_days
        # print("Number of ", product, "needed: ", int(products_needed_in_total[product]) - int(currentInventory[product_index][1]))
        # products_to_order[product] = (int(products_needed_in_total[product])/days_in_inventory()) - int(currentInventory[product_index][1])
        # products_to_order[product] = int(products_needed_in_total[product]) - int (currentInventory[product_index][1])

    return products_to_order
    # return ""


# print(necessaryStock(14))

def updateStock(days_nr):
    update_dict = necessaryStock(days_nr)
    inventar_header = ['Product', 'Stock']
    with open('InventarUpdatat3.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(inventar_header)
        for i in range(1, 15):
            product_to_be_updated = currentInventory[i][0]
            new_value = int(currentInventory[i][1]) + int(update_dict[product_to_be_updated])
            product_data = [currentInventory[i][0], new_value]
            writer.writerow(product_data)

    # df = pd.read_csv('employees.csv', index_col='Id')
    # df.loc[row_label, column name] = new_value
    # df.to_csv('employees.csv')

    # with open('InventarCurent.csv', 'w') as file2:
    #     writer2 = csv.writer(file2)
    #     writer2.writerow(inventar_header)
    #     for i in range(1, 15):
    #         product_to_be_updated = updatedInventory[i][0]
    #         new_value = int(currentInventory[i][1]) + int(update_dict[product_to_be_updated])
    #         product_data = [updatedInventory[i][0], new_value]
    #         writer2.writerow(product_data)

    return ""

    # update_dict = necessaryStock(days_nr)
    # for i in range(1, 15):
    #     product_to_be_updated = currentInventory[i][0]
    #     currentInventory[i][1] += update_dict[product_to_be_updated]
    # return ""


def main():
    print("Choose a number to give a command: ")
    print("1 - See current inventory")
    print("2 - See sales history")
    print("3 - See how many of each product were sold per day")
    print("4 - See how many more products you need to refill the stock")
    print("5 - Quit")
    print("\n")
    ok = True
    inventar_updatat = False
    while (ok):
        user_input = input("Your command:")
        if int(user_input) not in [1, 2, 3, 4, 5]:
            print("Please enter a number from 1 to 5")
        elif int(user_input) == 1:
            print("Current inventory: ")
            # if inventar_updatat == False:
            #     inventar_dataset = pd.read_csv("./InventarCurent.csv")
            #     print(inventar_dataset)
            # else:
            #     inventar_dataset = pd.read_csv("./InventarUpdatat2.csv")
            #     print(inventar_dataset)
            inventar_curent_dataset = pd.read_csv("./InventarCurent.csv")
            print(inventar_curent_dataset)
        elif int(user_input) == 2:
            print("Sales history: ")
            istoric_dataset = pd.read_csv("./IstoricVanzari.csv")
            print(istoric_dataset)
        elif int(user_input) == 3:
            print("This is how many of each product were sold per day: ")
            print(howManySoldPerDay())
        elif int(user_input) == 4:
            condition_days = True
            while condition_days:
                days_number = input(
                    "You want to see if you need to refill the stock? Great! Please enter the number of days\n")
                if days_number.isnumeric() and int(days_number) > 0:
                    condition_days = False
                    print("For", days_number, "days you will need: ")
                    print(necessaryStock(days_number))
                    condition_update_stock = True
                    while condition_update_stock:
                        answer = input("Would you like to update the stock? (Yes/No)\n")
                        if answer == "Yes" or answer == "yes":
                            updateStock(days_number)
                            inventar_updatat_dataset = pd.read_csv("./InventarUpdatat3.csv")
                            # inventar_updatat = True
                            print("Stock has been updated! ")
                            print("New inventory:")
                            print(inventar_updatat_dataset)
                            condition_update_stock = False
                            ok = False
                        elif answer == "No" or answer == "no":
                            print("All right, but you're running out of products soon!")
                            condition_update_stock = False
                        else:
                            print("Please enter Yes/No\n")
                else:
                    print("Please enter a (strictly positive) number")
        elif int(user_input) == 5:
            ok = False
    print("Thank you")
    return ""


if __name__ == "__main__":
    main()

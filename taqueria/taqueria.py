# Program allows user to place order and user use the command CTR + D to exit when done
def main():
    menu = {  # Dict containing items and their corresponding price
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0  # A  variable that computes prices of items
    while True:
        try:
            item = input("Item: ").title()  # Gets user input and formats the first char if needed
            # Checks if item is in dict
            if item in menu:
                total += menu[item]  # Updates total with the price of selected item
                print(f'Total: ${total:.2f}')  # Prints total cost
            else:  # Reprompts user if item is not in dict
                continue
        except EOFError:  # Handles EOFError
            print()
            break  # Exits program if EOFError encountered


main()
# Program makes a grocery list from user input
def main():
    grocery_list = {}  # Empty dict to store items and the number of times they are inputted
    while True:
        try:
            item = input().upper()  # Prompts user for input
            # Checks if item has been previously entered into the dict
            if item in grocery_list:
                grocery_list[item] += 1  # Updates the count by 1

            else:
                grocery_list[item] = 1  # Adds item to the dict and gives it a count of 1.

        except EOFError:  # Handles EOFError
            for item in sorted(grocery_list):  # Loop to scan through the sorted dict
                print(grocery_list[item], item)  # Prints count and items respectively
            break  # Exit program


main()
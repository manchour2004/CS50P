# Program bids farewell to the names entered by user
def main():
    name_list = []  # An empty list that will store names along with ', '

    while True:
        try:
            name = input("Name: ")  # Prompts user for name
            name_list.append(name)  # Appends name to name_list from earlier
            name_list.append(", ")  # Appends ", ' to the list

        except EOFError:  # Handles EOFError
            name_list.pop(len(name_list) - 1)  # Removes the ', ' at the end of the list
            print()  # Prints a new line for output

            # Checks if two names are entered
            if len(name_list) == 3:
                name_list[(len(name_list) - 2)] = ' and '  # Replaces the comma before the last name with ' and '

            # Checks if more than two names are entered
            elif len(name_list) > 3:
                name_list[(len(name_list) - 2)] = ', and '  # Replaces the comma before the last name with ', and '

            print("Adieu, adieu, to", end=' ')  # Prints "Adieu, adieu, to"

            # Loops that prints each name and ends on the same line
            for i in range(len(name_list)):
                print(f"{name_list[i]}", end='')

            print()  # Prints new line after output

            exit()  # Exits the program


main()
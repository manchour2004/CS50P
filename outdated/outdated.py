def main():

    months = [  # List conatining months
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
    ]

    month = 0  # A variable that stores the index of the month
    while True:
        try:
            # Gets user input, removes quotes and spaces on either side of the string
            date = input("Date: ").replace('"', '').strip()

            if date.count(" ") > 0:  # Checks if user input is seperated by a space
                date = date.title().split(" ")  # Splits user input into a list

                if date[1].count(',') > 0:  # Checks if the day is followed by a comma
                    date[1] = date[1].replace(',', '')

                else:
                    continue  # Reprompts user for input if condition is false

                # Checks if the first-indexed string in the list date is a month in the list. Also checks if the day is within the range of 1 and 31
                if date[0] in months and 1 <= int(date[1]) <= 31:
                    # Assigns the 1 added to value of the index of the string in the list months to month
                    month = months.index(date[0]) + 1
                    break  # Breaks out of loop

            elif date.count("/") > 0:  # Checks if user_input is seperated by a forward slash
                date = date.split("/")  # Splits each string on either side of the forward slash in a list

                # Checks if the first-indexed string in the list date is within the range of 1 and 1. Also checks if day is in the range of 1 and 31
                if 1 <= int(date[0]) <= 12 and 1 <= int(date[1]) <= 31:
                    month = int(date[0])  # Assign the int value of first_indexed string to month
                    break  # Breaks out of loop

        except ValueError:  # Handles value error
            continue  # Reprompts user

    print(f'{date[2]}-{month:02d}-{int(date[1]):02d}')  # Prints the formatted date


main()
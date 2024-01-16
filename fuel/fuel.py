# Program gets a quotient expression and returns a fraction
def main():
    fraction = get_fraction("Fraction: ")  # Prompts user for the expresion and returns a float
    print(f'{round(fraction * 100)}%')  # Converts float to fraction and prints it out


def get_fraction(prompt):
    while True:
        try:
            x = input(prompt).split('/')  # Splits chars on either side of / into a list
            if round((int(x[0]) / int(x[1])), 1) == 1:  # Checks if  the result of numerator over denominator to a decimal place is 1
                print("F")
                exit()
            elif (int(x[0]) == 0) or (int(x[1]) == 100):  # Checks if numerator is 0 and denominator is 100
                print("E")
                exit()
            elif (int(x[0]) < int(x[1])):  # Checks if numerator is less than denominator, else it keeps prompting user
                return int(x[0]) / int(x[1])  # Returns the result of the division
        except (ValueError, ZeroDivisionError):  # Handles errors
            pass


main()
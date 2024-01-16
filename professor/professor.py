# This is a program that generates random addition problems based on user input for difficulty level
import random  # Imports the library module


def main():

    print(f'Score: {generate_integer(get_level())}')  # Prints final score


def get_level():
    """Function attempts to get level from user"""

    accepted_levels = [1, 2, 3]  # List containing valid levels user should enter

    while True:
        try:
            level = int(input("Level: "))  # Prompts user for level
            # Checks if level the user entered is in the list of accepted levels
            if level in accepted_levels:
                return level  # breaks out of the loop and passes the value of level out of the function
            else:
                continue  # Keeps reprompting user till valid input

        except ValueError:  # Handles non-numeric value the user enters
            continue


def generate_integer(level):
    """Function generates Maths problem depending on the level the user entered earlier"""

    correct_answers = 0  # A variable that keeps track of the number of correct answers the user has

    # Loops generates 10 different Maths problem
    for i in range(10):
        # Checks if level user entered is 1
        if level == 1:
            # Generates numbers from 0 - 9(inclusive)
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        # Checks if level user entered is 2
        elif level == 2:
            # Generates numbers from 10 - 99(inclusive)
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        # Checks if level user entered is 3
        else:
            # Generates numbers from 100 - 999(inclusive)
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        sum = x + y  # Computes the sum of each randomly generated numbers x and y
        incorrect_guesses = 0  # A variable that keeps track of incorrect answers the user typed in and is initialized for each loop

        # Loop will iterate 3 times if user keeps inputting the wrong answer
        while incorrect_guesses < 3:
            try:
                user_sum = int(input(f'{x} + {y} = '))  # Asks user for answer to the Maths problem
                # Checks if user answer is the correct sum
                if sum == user_sum:
                    correct_answers += 1  # Increases the number of correct answers user has entered by 1
                    cont = input(f'Enter yes to continue: ')
                    if cont == "yes":
                        break  # Breaks out of the while loop and continues the for loop
                    else:
                        exit(f"Score: {correct_answers}")


                # Checks if user answer is incorrect
                else:
                    print("EEE")  # Outputs EEE
                    incorrect_guesses += 1  # Updates the number of incorrect_guesses by 1
                    continue  # Reprompts user for input

            except ValueError:
                print("EEE")  # Outputs EEE
                incorrect_guesses += 1  # Updates the number of incorrect_guesses by 1
                continue  # Reprompts user for input

        # Checks if number of incorrect guesses exceeds the limit 3
        else:
            print(f'{x} + {y} = {sum}')  # Outputs the expression and the correct sum
            cont = input(f'Enter yes to continue: ')
            if cont == 'yes':
                continue  # Continues the for loop
            else:
                exit(f"Score: {correct_answers}")

    return correct_answers  # Passes the value of correct_answers out of the function at the end of the for loop


if __name__ == "__main__":
    main()
# Program asks user to randomly generated number bbased on the difficulty the user inputed
import random  # Imports random module


def main():
    while True:
        try:
            level = int(input("Level: "))  # Prompts user for level

            # Keeps reprompting user if level is less than 1
            while level < 1:
                level = int(input("Level: "))

            random_number = random.randint(1, level)  # Generates a random number from1 to user level(inclusive)

            guessed_number = int(input("Guess: "))  # Ask user the random number generated

            # Keeps reprompting user if guessed number is less than 1
            while guessed_number < 1:
                guessed_number = int(input("Guess: "))

            # Checks if guessed number is less than random number generated and keeps reprompting if true
            if guessed_number < random_number:
                print("Too small!")
                continue

            # Checks if guessed number is greater than random number generated and keeps reprompting if true
            elif guessed_number > random_number:
                print("Too large!")
                continue

            # Checks if guessed number is exactly random number generated and exits effectively
            else:
                print("Just right!")
                exit()

        # Handles non-numeric input and reprompts user
        except ValueError:
            continue


main()
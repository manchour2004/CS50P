# Program changes camelCase to snake_case
def main():
    name = input("Input Camelcase: ")
    print(snake_case(name))


def snake_case(n):
    snake_case_character = ''  # An empty string variable that allows me concatenate each characters from the preceeding loop

    for i in range(len(n)):
        # Condition to check if character is caps
        if n[i].isupper():
            snake_case_character += '_'  # Adds underscore character to strings of characters preceeding it
            snake_case_character += n[i].lower()  # Adds uncapitalized character after the underscore
        else:
            snake_case_character += n[i]  # Concatenate characters which aren't caps
    return snake_case_character


main()
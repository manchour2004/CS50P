# Program removes vowels from user input
def main():
    string = input("Input: ")  # Prompts user for input
    print(remove_vowels(string))  # Prints formatted input


def remove_vowels(n):
    new_string = ''  # An empty string variable that allows me concatenate characters from the loop
    vowels = ['a', 'e', 'i', 'o', 'u']  # List of lower case vowels
    caps_vowels = ['A', 'E', 'I', 'O', 'U']  # List of upper case vowels

    for i in range(len(n)):
        # Checks if character is in the list of upper or lower case vowels
        if n[i] in vowels or n[i] in caps_vowels:
            new_string += ''  # Replaces the character with an empty string
        # Leaves other characters unchanged
        else:
            new_string += n[i]
    return new_string  # Returns formatted string


main()
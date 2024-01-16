import sys  # Import sys for command-line arguments
import pyfiglet  # Imports the pyfiglet package

def main():
    fonts = ['alphabet', 'slant', 'rectangles', 'regular']  # A list of acceptable fonts for figlet

    # Checks if font wasn't specified in the command line
    if len(sys.argv) == 1:
        text = input("Input: ")  # Prompts user for Input
        figlet = pyfiglet.Figlet()  # Assigns a default font

    # Checks if font was specified in the command line
    elif len(sys.argv) == 3:
        # Checks if user used the valid use of font specifier
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            # Checks if user typed in a correct font style
            if sys.argv[2] in fonts:
                text = input("Input: ")  # Prompts user for Input
                figlet = pyfiglet.Figlet(sys.argv[2])  # Assigns specified font
    else:
        sys.exit("Invalid usage")  # Exits program if none of the conditions were met

    print(figlet.renderText(text))  # Prints the formatted text


main()
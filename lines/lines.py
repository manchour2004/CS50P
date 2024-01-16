import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command line arguments")
        elif ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
        else:
            lines = []
            with open(sys.argv[1], 'r') as file:
                let_see = file.readlines()
                for line in let_see:
                    lines.append(line.strip())
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count_lines(lines))


def count_lines(list):
    """ Function checks for number of lines in a file """
    count_lines = 0
    for items in list:
        if items.isspace():
            count_lines = count_lines
        elif items == "":
            count_lines = count_lines
        elif items[0] == "#" and items[1] == " ":
            count_lines = count_lines
        elif items[:3] == '"""':
            count_lines = count_lines
        elif items == 'if __name__ == "__main__":':
            count_lines = count_lines
        else:
            count_lines += 1
    return count_lines


if __name__ == "__main__":
    main()
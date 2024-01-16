import sys


from csv import DictReader


from tabulate import tabulate


def main():
     try:
        if len(sys.argv) < 2:
            sys.exit("Too few command line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command line arguments")
        elif ".csv" not in sys.argv[1]:
            sys.exit("Not a Python file")
        else:
            lines = []
            with open(sys.argv[1], 'r') as file:
                let_see = DictReader(file)
                for dict in let_see:
                    lines.append(dict)
     except FileNotFoundError:
        sys.exit("File does not exist")

     print(tabulate(lines,headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
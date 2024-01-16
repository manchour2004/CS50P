import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = "([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
    if re.search(fr"^(?:{valid}\.)(?:{valid}\.)(?:{valid}\.)(?:{valid})$",ip):
        return True
    return False


if __name__ == "__main__":
    main()
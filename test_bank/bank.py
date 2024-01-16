def main():
    string = input("Greeting: ")
    print(f'${value(string)}')


def value(greeting):
    greeting = greeting.lower().strip().split(',')

    if greeting[0][0] == "h" and greeting[0] != "hello":
        return 20
    elif greeting[0][0] == "w":
        return 100
    else:
        return 0

if __name__ == "__main__":
    main()
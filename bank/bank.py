def main():
    string = input("Greeting: ").lower()
    string_1 = string.split(',')

    if string[0] == "h" and string_1[0] != "hello":
        print("$20")
    elif string[0] == "w":
        print("$100")
    else:
        print("$0")


main()
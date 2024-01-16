def main():
    number = int(input("How many numbers: "))
    sum = 0

    for _ in range(number):
        x = int(input("input number: "))
        sum += x

    print(sum)


main()
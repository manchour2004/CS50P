def main():
    string = input("Expression: ")
    value = string.split(" ")
    value_1 = int(value[0])
    value_2 = int(value[2])
    result = 0

    match value[1]:
        case '+':
            result = value_1 + value_2
        case '-':
            result = value_1 - value_2
        case '*':
            result = value_1 * value_2
        case '/':
            result = value / value_2
    print(f'{result:.1f}')

main()

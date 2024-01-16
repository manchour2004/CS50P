def main():
    string = input()

    string = emoji(string)

    print(string)

def emoji(text):
    text = text.replace(':(', '🙁')

    text = text.replace(':)', '🙂')

    return text
main()
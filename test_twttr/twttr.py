def main():
    string = input("Input: ")
    print(shorten(string))


def shorten(n):
    new_string = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    caps_vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(n)):
        if n[i] in vowels or n[i] in caps_vowels:
            new_string += ''
        else:
            new_string += n[i]

    return new_string


if __name__ == "__main__":
    main()
def main():
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip(" ").lower()

    match string:
        case "42" | "forty-two" | "forty two" :
            print("Yes")
        case _ :
            print("No")
main()

def main():
    file = input("Input file type: ").lower().strip(" ").split(".")
    length = len(file) - 1

    if file[0] == "plain" and file[length] == "txt":
        print("text/plain")
    elif file[0] != "plain" and file[length] == "txt":
        print("application/txt")
    elif file[length] == "jpg":
        print("image/jpeg")
    elif file[length] == "jpeg":
        print("image/jpeg")
    elif file[length] == "gif":
        print("image/gif")
    elif file[length] == "png":
        print("image/png")
    elif file[length] == "pdf":
        print("application/pdf")
    elif file[length] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


main()
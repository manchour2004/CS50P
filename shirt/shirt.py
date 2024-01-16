import sys

from PIL import Image, ImageOps


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            if not (".jpg" in sys.argv[2] or ".png" in sys.argv[2]):
                sys.exit("Invalid output")
            elif (sys.argv[1][len(sys.argv[1]) - 4:]) != (sys.argv[2][len(sys.argv[2]) - 4:]):
                sys.exit("Input and output have different extensions")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    with Image.open(sys.argv[1]) as im:
        new_image = ImageOps.fit(im, (600,600))
        new_image.paste(shirt, box=(0,0), mask=shirt)
        new_image.save(sys.argv[2])

if __name__ == "__main__":
    main()
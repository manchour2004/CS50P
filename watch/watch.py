import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "<iframe" in s:
        if matches := re.search(r'(https?://)c?(youtube)(?:.com)(/)(?:embed/)?(\w+)',s):
            url = "".join(matches.groups())
            if "https" in url:
                return url.replace("youtube","youtu.be")
            else:
                return url.replace("youtube","youtu.be").replace("http","https")
    return None


if __name__ == "__main__":
    main()
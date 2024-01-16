from twttr import shorten


def test_vowels():
    assert shorten("hey") == "hy"
    assert shorten("Integrated") == "ntgrtd"


def test_punctuation():
    assert shorten("hi, i am joe") == "h,  m j"
    assert shorten("a,b,c,d,e,f") == ",b,c,d,,f"

def test_numbers():
    assert shorten("zeR0") == "zR0"


if __name__ == "__main__":
    main()

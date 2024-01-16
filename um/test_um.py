from um import count

def test1():
    assert count("yummy") == 0


def test2():
    assert count("Um, I don't belive you, um") == 2
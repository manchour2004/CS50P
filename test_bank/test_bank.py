from bank import value

def test_h():
    assert value("Hey") == 20


def test_hello():
    assert value("Hello") == 0


def test_specialcase():
    assert value("What's up") == 100

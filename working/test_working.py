from working import convert

import pytest
def test1():
    pytest.deprecated_call() d
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test3():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test4():
    with pytest.raises(ValueError):
        convert("10 AM - 7 PM")

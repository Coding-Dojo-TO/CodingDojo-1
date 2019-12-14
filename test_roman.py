from .roman import roman_to_integer

def test_roman_number_I():
    number = "I"
    assert 1 == roman_to_integer(number)

def test_roman_II():
    number = "II"
    assert 2 == roman_to_integer(number)

def test_roman_III():
    number = "III"
    assert 3 == roman_to_integer(number)

def test_roman_IV():
    number = "IV"
    assert 4 == roman_to_integer(number)

def test_roman_V():
    number = "V"
    assert 5 == roman_to_integer(number)

def test_roman_VI():
    number = "VI"
    assert 6 == roman_to_integer(number)

def test_roman_VII():
    number = "VII"
    assert 7 == roman_to_integer(number)

def test_roman_VIII():
    number = "VIII"
    assert 8 == roman_to_integer(number)
def test_roman_IX():
    number = "IX"
    assert 9 == roman_to_integer(number)

def test_roman_X():
    number = "X"
    assert 10 == roman_to_integer(number)

def test_roman_L():
    number = "L"
    assert 50 == roman_to_integer(number)

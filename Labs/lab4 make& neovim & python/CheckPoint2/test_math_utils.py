from math_utils import subtract, divide
def test_subtract():
    assert subtract(9, 2) == 7
    assert subtract(-3, -3) == 0
def test_divide():
    assert divide(18, 3) == 6
    assert divide(10, 0) is None

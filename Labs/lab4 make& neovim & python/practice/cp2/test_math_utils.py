from math_utils import subtract, divide
def test_subtract():
    assert subtract(18, 6) == 12
    assert subtract(99, 0) == 99

def test_divide():
    assert divide(18,6) == 3
    assert divide(99,0) is None

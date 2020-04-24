from calculator import add, subtract, multiply


def test_add():
    out = add(3, 4)
    expected_out = 7
    assert out == expected_out


def test_subtract():
    out = subtract(9, 1)
    expected_out = 8
    assert out == expected_out


def test_multiply():
    out = multiply(4, 5)
    expected_out = 20
    assert out == expected_out
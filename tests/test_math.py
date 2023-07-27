import pytest

MULTIPLICATION_CASES = (
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
)


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        # Removed `num` var because unused
        1/0

        # Moved assert inside `with` block, because I'm not sure `e` is
        # guaranteed to be available outside of it
        assert "division by zero" in str(e.value)


@pytest.mark.parametrize("a, b, product", MULTIPLICATION_CASES)
def test_multiplication(a, b, product):
    assert a*b == product

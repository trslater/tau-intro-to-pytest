import pytest

from stuff.accum import Accumulator


def test_accumulator_init():
    a = Accumulator()

    assert a.count == 0


# Changed name from `_add_one` to `_add_default`, since this could be changed
def test_accumulator_add_default():
    a = Accumulator()
    a.add()

    assert a.count == 1


def test_accumulator_add_int():
    a = Accumulator()
    a.add(3)

    assert a.count == 3


def test_accumulator_add_multiple():
    a = Accumulator()
    a.add(3)
    a.add(4)

    assert a.count == 7


def test_accumulator_set_count():
    a = Accumulator()

    with pytest.raises(AttributeError):
        a.count = 10

import pytest


def test_frombytes():
    assert int.from_bytes(b'\x00\x7f', byteorder='big') == 127


def test_bitlendth():
    x = 204
    assert bin(x) == '0b11001100'
    assert x.bit_length() == 8


def test_classint():
    class Person:
        age = 23

        def __int__(self):
            return self.age

    person = Person()
    assert int(person) == 23


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("9//2", 4),
    pytest.mark.xfail(("6*9", 42))])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

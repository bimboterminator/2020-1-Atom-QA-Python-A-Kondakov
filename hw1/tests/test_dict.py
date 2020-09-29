import pytest


def test_nokey():
    dict1 = {"name": "Mike", "salary": 8000}
    with pytest.raises(KeyError):
        assert dict1["age"]


def test_pop():
    student = {"name": "Emma", "class": 9}
    student['marks'] = 75
    assert student.popitem() == ('marks', 75)


def test_dictasllist():
    d = {'jack': 4098, 'guido': 4127, 'irv': 4127}
    assert isinstance(list(d),list)


@pytest.mark.parametrize("x", ['123456','abcdef'])
def test_fromkeys(x):
    sub_dict = dict.fromkeys(x, "Hello")
    assert len(sub_dict) == 6


class Testdict:
    d = dict()
    c = {0: 0, 7: 0, 1: 1, 8: 1}

    def test_compare(self):
        for x in enumerate(range(2)):
            self.d[x[0]] = x[1]
            self.d[x[1] + 7] = x[0]

        assert self.d == self.c

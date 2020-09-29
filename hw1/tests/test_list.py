import pytest


def test_objectref():
    a = [1, 2, 3, 4, 5]
    b = a
    b[2] = 10
    assert a[2] == 10
    assert b is a


def test_slicing():
    a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
    assert 'baz' in a[4::-2]


def test_nested():
    x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
    assert x[1][2][1][-1] == 'z'


def test_borders():
    a = [-1, 1, 3]
    with pytest.raises(IndexError):
        assert a[3]


class TestListElements:
    list1 = ['a', 'bar', 'baz']
    list2 = ['baz', 'foo', 'bar']

    def test_list_eq(self):
        assert not all([a == b for a, b in zip(self.list1,self.list2)])


@pytest.mark.parametrize('obj', [[1, 2, 3], [1, 5, 6]])
def test_copy(obj):
    a = obj.copy()
    assert a is not obj;

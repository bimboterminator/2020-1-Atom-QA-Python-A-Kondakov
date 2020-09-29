import pytest


def test_hashabletype():
    a = set()
    with pytest.raises(TypeError):
        assert a.add([1,2,3])

def test_setinit():
    sets = {3, 4, 5, 3, 3, 3}
    sets.update([1, 2, 3])
    assert sets == {1, 2, 3, 4, 5}

class Testsets:

    base = {4, 5, 6, 7, 8}
    other = {1, 2, 3, 4, 5}

    def test_symdif(self):
        assert self.base ^ self.other == {1, 2, 3, 6, 7, 8}

    def test_subset(self):
        with pytest.raises(AttributeError):
            assert self.other.ispropersubset(self.base) == False


@pytest.mark.parametrize("x,y", [({'a', 'b', 'c'},{1,2,3}), (set(),{0,1,4,8}), (set(),set())])
def test_setlogic(x,y):
    assert (x & y <= x) and (x & y <= y)

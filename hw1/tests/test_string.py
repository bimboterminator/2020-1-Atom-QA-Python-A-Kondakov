import pytest


def test_slicing():
    s = '12345' * 5
    assert s[::-5] == '55555'


def test_immutable():
    s = 'foobar'
    with pytest.raises(TypeError):
        s[3] = 'x'
    s = s.replace('b','x')
    assert s[3] == 'x'


def test_upperlower():
    s = 'abc1$d'
    s = s.upper()
    assert s.isupper()
    s = s.lower()
    assert s.islower()


class Teststring():
    str = 'abcdefcdyz'
    substr = 'ab'

    def test_partition(self):
        assert self.str.partition(self.substr) == ('', 'ab', 'cdefcdyz')

    def test_zfill(self):
        assert self.substr.zfill(5) == '000ab'

    def test_center(self):
        assert self.substr.center(10,"*") == "****ab****"

    @pytest.mark.parametrize('sample', ['floruda dolphins abc','creme brulabcee', 'string slicistring slicingabcng'])
    def test_instring(self,sample):
        assert self.substr in sample
        assert isinstance(sample.find(self.substr), int)

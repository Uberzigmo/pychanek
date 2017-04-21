def secti(a, b):
    return a + b


def nasob(a, b):
    raise Exception('Funkce jeste neni implementovana!')


def vydel(a, b):
    out = a / b
    return out

def test_secti():
    assert secti(1, 2) == 3




import pytest


def test_deleni_nulou():
    with pytest.raises(Exception):
        vydel(1,0)
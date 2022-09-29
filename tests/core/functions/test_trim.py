import pytest

from dataconverter.core.functions.Trim import Trim


@pytest.fixture
def trim():
    return Trim()


def test_trim(trim):
    assert trim.apply(" abc ") == ["abc"]
    assert trim.apply(True) == [""]
    assert trim.apply("str") == ["str"]
    assert trim.apply("\r\n str\r\n") == ["str"]
    assert trim.apply([]) == [""]
    assert trim.apply({}) == [""]

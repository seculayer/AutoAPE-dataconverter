import pytest
from hypothesis import given
from hypothesis import strategies as st

from dataconverter.core.functions.BasicNormal import BasicNormal


@pytest.fixture
def basic():
    return BasicNormal()


def test_basic_normal(basic):
    assert basic.apply("abc") == [(3 / 32767)]
    assert basic.apply("Hello World") == [""]
    assert basic.apply("asht14234") == [""]
    assert basic.apply(32767) == [1]


def test_basic_normal_with_wrong_type(basic):
    # type: ignore
    assert basic.apply(None) == [0]
    assert basic.apply("-+*@") == [""]

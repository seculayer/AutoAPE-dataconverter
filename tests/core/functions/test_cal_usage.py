import pytest
from hypothesis import given
from hypothesis import strategies as st

from dataconverter.core.functions.CalUsage import CalDevUsage


@pytest.fixture
def cal():
    return CalDevUsage()


def test_CalDevUsage(cal):
    assert cal.apply("24.5753") == [0.245753]
    assert cal.apply("") == [0]
    assert cal.apply("0") == [0]
    assert cal.apply(10) == [0.1]
    assert cal.apply(100.0) == [1]

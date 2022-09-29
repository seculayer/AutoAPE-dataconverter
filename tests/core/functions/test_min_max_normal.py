import pytest

from dataconverter.core.functions.MinMaxNormal import MinMaxNormal


@pytest.fixture
def minmax_normal_255():
    return MinMaxNormal(stat_dict={"min": 0, "max": 255})


def test_minmax_8bit(minmax_normal_255: MinMaxNormal):
    assert minmax_normal_255.apply(255) == [1.0]
    assert minmax_normal_255.apply(0) == [0.0]
    assert minmax_normal_255.apply(128) == [(128 / 255)]

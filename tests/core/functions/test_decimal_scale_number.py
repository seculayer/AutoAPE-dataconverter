import pytest

from dataconverter.core.functions.DecimalScaleNormal import DecimalScaleNormal


@pytest.fixture
def decimal_scale():
    return DecimalScaleNormal()


def test_decimal_scale_normal(decimal_scale):
    assert decimal_scale.apply(0) == [0]
    assert decimal_scale.apply(2543) == [0.02543]
    assert decimal_scale.apply(192) == [0.00192]
    assert decimal_scale.apply(-1) == [-1e-5]
    assert decimal_scale.apply("str") == [0]

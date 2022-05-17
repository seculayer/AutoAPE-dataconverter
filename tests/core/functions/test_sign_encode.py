import pytest

from dataconverter.core.functions.SignEncode import SignEncode


@pytest.fixture
def sign_encode():
    return SignEncode()


def test_sign_encode(sign_encode):
    assert sign_encode.apply(0) == [-1]
    assert sign_encode.apply(1) == [1]
    assert sign_encode.apply(10) == [None]
    assert sign_encode.apply("aht") == [None]

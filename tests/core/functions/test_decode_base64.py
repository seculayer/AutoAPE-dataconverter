import base64

import pytest
from hypothesis import given
from hypothesis import strategies as st

from dataconverter.core.functions.DecodeBase64 import DecodeBase64


@pytest.fixture(scope="module")
def base64_decoder():
    return DecodeBase64()


def test_decode_base64(base64_decoder):
    assert base64_decoder.apply("SGVsbG8gV29ybGQ=") == ["Hello World"]


@given(st.text())
def test_base64_with_ramdom_str(base64_decoder, text):
    assert base64_decoder.apply(base64.b64encode(text.encode())) == [text]


def test_decode_base64_wrong_input(base64_decoder):
    # type: ignore
    assert base64_decoder.apply(0) == [""]
    assert base64_decoder.apply([]) == [""]
    assert base64_decoder.apply({}) == [""]
    assert base64_decoder.apply(1.0) == [""]
    assert base64_decoder.apply(1 + 1j) == [""]

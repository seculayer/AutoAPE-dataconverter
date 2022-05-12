import binascii

import pytest
from hypothesis import given, strategies as st
from dataconverter.core.functions.HexToString import HexToString


@pytest.fixture(scope="module")
def hex2str():
    return HexToString(arg_list=["utf-8"])


def test_hex_to_string_hello(hex2str):
    assert hex2str.apply("68656c6c6f") == ["hello"]


@given(st.text())
def test_hex_to_utf8_string_with_ranmdom_str(hex2str, text):
    assert hex2str.apply(binascii.hexlify(text.encode())) == [text]

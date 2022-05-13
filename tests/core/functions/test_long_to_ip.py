import pytest

from dataconverter.core.functions.LongToIP import LongToIP


@pytest.fixture
def long2ip():
    return LongToIP()


def test_long_to_ip(long2ip: LongToIP):
    assert long2ip.apply(16909060) == ["1.2.3.4"]
    assert long2ip.apply(0x7F000001) == ["127.0.0.1"]
    assert long2ip.apply(0x0A0A0A00) == ["10.10.10.0"]


def test_long_to_ip_wrong_input(long2ip: LongToIP):
    # type: ignore
    assert long2ip.apply([]) == [""]
    assert long2ip.apply({}) == [""]
    assert long2ip.apply("string") == [""]

import pytest

from dataconverter.core.functions.UnixTimeStamp import UnixTimeStamp


@pytest.fixture
def unix_timestamp():
    return UnixTimeStamp()


def test_unix_timestamp(unix_timestamp):
    assert unix_timestamp.apply("0") == ["19700101000000"]
    assert unix_timestamp.apply(0) == ["19700101000000"]
    assert unix_timestamp.apply(0.0) == ["19700101000000"]

    assert unix_timestamp.apply("1636359465") == ["20211108081745"]
    assert unix_timestamp.apply(1636359465) == ["20211108081745"]
    assert unix_timestamp.apply(1636359465.0) == ["20211108081745"]

    assert unix_timestamp.apply("1351239803") == ["20121026082323"]
    assert unix_timestamp.apply(1351239803) == ["20121026082323"]
    assert unix_timestamp.apply(1351239803.0) == ["20121026082323"]


def test_unix_timestamp_unexpected_inputs(unix_timestamp):
    assert unix_timestamp.apply([]) == [""]
    assert unix_timestamp.apply([123]) == [""]
    assert unix_timestamp.apply({}) == [""]
    assert unix_timestamp.apply(set()) == [""]
    assert unix_timestamp.apply(-1) == [""]
    assert unix_timestamp.apply(-1.0) == [""]
    assert unix_timestamp.apply(0 + 0j) == [""]

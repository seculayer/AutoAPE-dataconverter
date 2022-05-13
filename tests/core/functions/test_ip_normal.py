from unittest.mock import DEFAULT

import pytest

from dataconverter.core.functions.IPNormal import IPNormal

DEFAULT = [0, 0, 0, 0]


@pytest.fixture
def ip_normal() -> IPNormal:
    return IPNormal()


def test_ipnormal(ip_normal):
    assert ip_normal.apply("127.0.0.1") == [(127 / 255), 0, 0, (1 / 255)]
    assert ip_normal.apply("::1") == DEFAULT
    assert ip_normal.apply("10.0.0.1") == [(10 / 255), 0, 0, (1 / 255)]


def test_ip_normal_with_wrong_type(ip_normal):
    # type: ignore
    assert ip_normal.apply(1123094) == DEFAULT
    assert ip_normal.apply(123.0) == DEFAULT

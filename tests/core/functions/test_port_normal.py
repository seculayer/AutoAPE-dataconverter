import pytest

from dataconverter.core.functions.PortNormal import PortNormal


@pytest.fixture
def port_normal():
    return PortNormal()


def test_port_normal(port_normal):
    assert port_normal.apply("ashtr") == [None]
    assert port_normal.apply("8080") == [8080 / 65535]
    assert port_normal.apply(0) == [0]

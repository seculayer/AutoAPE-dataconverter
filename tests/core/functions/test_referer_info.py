import pytest

from dataconverter.core.functions.RefererInfo import RefererInfo


@pytest.fixture
def referer_info():
    return RefererInfo()


def test_referer_info(referer_info):
    assert referer_info.apply("www.example.com:8080") == ["www.example.com_8080"]
    assert referer_info.apply("www.example.com/index.html") == [
        "www.example.com/index.html"
    ]
    assert referer_info.apply("www.example.com/index.html?referer=example.com") == [
        "www.example.com/index.html"
    ]


def test_referer_info_wrong(referer_info):
    assert referer_info.apply(None) == ["#PADDING#"]
    assert referer_info.apply(1) == ["#PADDING#"]
    assert referer_info.apply([]) == ["#PADDING#"]
    assert referer_info.apply({}) == ["#PADDING#"]
    assert referer_info.apply(()) == ["#PADDING#"]

import pytest

from dataconverter.core.functions.ExtractDomain import ExtractDomain


@pytest.fixture
def extract_domain():
    return ExtractDomain()


def test_extract_domain(extract_domain):
    assert extract_domain.apply("www.naver.com") == ["naver.com"]
    assert extract_domain.apply("http://www.seculayer.com/index.html?arg1=0") == [
        "seculayer.com"
    ]

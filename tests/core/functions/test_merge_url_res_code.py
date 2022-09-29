import pytest

from dataconverter.core.functions.MergeURLResCode import MergeURLResCode


@pytest.fixture
def merge_url_res_code_0():
    return MergeURLResCode(arg_list=[0])


@pytest.fixture
def merge_url_res_code_1():
    return MergeURLResCode(arg_list=[1])


def test_merge_url_res_code_type_1(merge_url_res_code_1):
    payload_list = [
        (["200", "/index.html"], ["200|/index.html"]),
        (["404", "/404.html"], ["404|/404.html"]),
        (["301", "example.com/index.html?q=none"], ["301|example.com/index.html"]),
    ]

    for payload, expected in payload_list:
        assert merge_url_res_code_1.apply(payload) == expected


def test_merge_url_res_code_type_0(merge_url_res_code_0):
    data_list = [
        (["200", "GET /index.html"], ["200|/index.html"]),
        (["404", "GET /404.html"], ["404|/404.html"]),
        (["301", "GET example.com/index.html?q=none"], ["301|example.com/index.html"]),
    ]

    for payload, expected in data_list:
        assert merge_url_res_code_0.apply(payload) == expected

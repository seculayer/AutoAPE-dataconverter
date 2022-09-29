import pytest

from dataconverter.core.functions.Tokenizer import Tokenizer


def test_tokenizer():
    token = Tokenizer(arg_list=[20])

    assert token.apply("GET /shop/ProdSearch.php?Ccode1=0&Ccode2=&Ccode3=") == [
        "get",
        "/",
        "shop",
        "/",
        "prodsearch",
        ".",
        "php",
        "?",
        "ccode1",
        "=",
        "0",
        "&",
        "ccode2",
        "=",
        "&",
        "ccode3",
        "=",
        "",
        "#PADDING#",
        "#PADDING#",
    ]

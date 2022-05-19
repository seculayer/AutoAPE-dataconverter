from dataconverter.core.functions.SplitSpecialChar import SplitSpecialChar


def test_split_special_char():
    token = SplitSpecialChar(arg_list=[10])

    assert token.apply("~_str_!# abc,text;한글;😀|_$") == [
        "_str_",
        "abc",
        "text",
        "한글",
        "😀",
        "_",
        "#PADDING#",
        "#PADDING#",
        "#PADDING#",
        "#PADDING#",
    ]


def test_split_special_char_url():
    token = SplitSpecialChar(arg_list=[20])

    assert token.apply(
        "GET\n/shop/ProdSearch.php?Ccode1=0&Ccode2=&Ccode3=&SearchType=All&word_blank=and&word=&width=5 HTTP/1.1#CRLF#Host: 1.1.1.1"
    ) == [
        "get",
        "shop",
        "prodsearch.php",
        "ccode1=0",
        "ccode2=",
        "ccode3=",
        "searchtype=all",
        "word_blank=and",
        "word=",
        "width=5",
        "http",
        "1.1",
        "crlf",
        "host:",
        "1.1.1.1",
        "#PADDING#",
        "#PADDING#",
        "#PADDING#",
        "#PADDING#",
        "#PADDING#",
    ]

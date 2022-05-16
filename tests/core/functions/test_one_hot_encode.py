from dataconverter.core.functions.OneHotEncode import OneHotEncode


def test_one_hot_encode():
    one_hot_encode = OneHotEncode(stat_dict={"unique": {"0": 123, "1": 30}})

    assert one_hot_encode.apply("0") == [1, 0]
    assert one_hot_encode.apply("1") == [0, 1]
    assert one_hot_encode.apply("2") == [1, 0]

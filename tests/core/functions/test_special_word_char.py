from dataconverter.core.functions.SpecialWordChar import SpecialWordChar


def test_special_word_char_sql():
    sw = SpecialWordChar(arg_list=[30, "SQL"])

    assert sw.apply(
        "/news/section/newsview.php?idxno=882273%25%27/**/aND/**/%278%27%3D%278"
    ) == [
        # /news/section/newsview.php?
        # idxno=882273%'/**/aND/**/'8'='8
        # fmt: off
        47.0, 47.0, 47.0, 46.0, 63.0,
        61.0, 37.0, 39.0, 47.0, 42.0,
        42.0, 47.0, 70.0, 47.0, 42.0,
        42.0, 47.0, 39.0, 39.0, 61.0,
        39.0, 255.0, 255.0, 255.0, 255.0,
        255.0, 255.0, 255.0, 255.0, 255.0,
        # fmt: on
    ]

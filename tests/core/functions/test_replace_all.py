from dataconverter.core.functions.ReplaceAll import ReplaceAll


def test_replace_regex():
    regex = ReplaceAll(arg_list=[r"[a-z]", ""])

    assert regex.apply("Korea") == ["K"]
    assert regex.apply("ATM") == ["ATM"]
    assert regex.apply("abc") == [""]
    assert regex.apply("") == [""]

    assert regex.apply(1) == [""]  # type: ignore
    assert regex.apply(1.0) == [""]  # type: ignore

from dataconverter.core.functions.Replace import Replace


def test_replace():
    rep = Replace(arg_list=["K", "C"])

    assert rep.apply("Korea") == ["Corea"]
    assert rep.apply("K-POP") == ["C-POP"]
    assert rep.apply(123) == [""]
    assert rep.apply(0.0) == [""]
    assert rep.apply(None) == [""]

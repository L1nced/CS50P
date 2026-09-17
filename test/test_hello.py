from hello import hello


def test_argument():
    assert hello("Ihud") == "hello, Ihud"


def test_default():
    assert hello() == "hello, world"
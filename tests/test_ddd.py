from ddd import answer


def test_answer():
    assert int(answer()) == 42


def test_t():
    assert 1 + 1 == 3


def test_c():
    assert True in (False)

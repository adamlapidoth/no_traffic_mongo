import pytest

from ddd import answer


@pytest.fixture
def yolo():
    return "you only live once"


def test_answer():
    assert int(answer()) == 42


def test_t():
    assert 1 + 1 == 2


def test_c():
    assert True in (False, True)


def test_c1(yolo):
    assert "o" in yolo

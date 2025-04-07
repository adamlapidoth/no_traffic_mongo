import pytest

from schema import Item


@pytest.fixture
def laptop():
    return Item(product_id="p001", name="laptop", price=1200, quantity=1)


@pytest.fixture
def mouse():
    return Item(product_id="p002", name="mouse", price=50, quantity=1)

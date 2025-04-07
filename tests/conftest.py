import pytest
from pymongo import MongoClient

from schema import Item, Shipment, User


@pytest.fixture
def laptop():
    return Item(product_id="p001", name="laptop", price=1200, quantity=1)


@pytest.fixture
def mouse():
    return Item(product_id="p002", name="mouse", price=50, quantity=1)


@pytest.fixture
def user_1():
    return User(name="Adam Lapidoth", user_id="U1233")


@pytest.fixture
def shipment(user_1, mouse, laptop):
    mouse.quantity = 3
    laptop.quantity = 2
    return Shipment(user_1, items=[mouse, laptop])


@pytest.fixture(scope="session")
def mongo_client():
    return MongoClient(host="localhost", port=27017)


@pytest.fixture(scope="session")
def db(mongo_client):
    db = mongo_client.my_tello
    return db

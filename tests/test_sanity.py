def test_mouse(mouse):
    assert mouse.name == "mouse"
    assert mouse.price == 50


def test_laptop(laptop):
    assert laptop.name == "laptop"
    assert laptop.price == 1200


def test_shipment(order):
    assert order.total_price == 2550


def test_db(db, mongo_client):
    assert db.name in mongo_client.list_database_names()

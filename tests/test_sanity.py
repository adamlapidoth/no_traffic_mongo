def test_mouse(mouse):
    assert mouse.name == "mouse"
    assert mouse.price == 50


def test_laptop(laptop):
    assert laptop.name == "laptop"
    assert laptop.price == 1200


def test_shipment(shipment):
    assert shipment.total_price == 2550

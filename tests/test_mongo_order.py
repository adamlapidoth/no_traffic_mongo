import pytest

from mongo_classes import MOrder


class TestMongoOrder:
    @pytest.mark.usefixtures("_clear_orders")
    def test_add(self, db, order):
        mongo_order = MOrder(db, order)
        ret = mongo_order.add()
        print(dir(ret))
        assert ret.acknowledged
        assert ret.inserted_id

    @pytest.mark.usefixtures("_clear_orders")
    def test_get(self, db, order):
        mongo_order = MOrder(db, order)
        mongo_order.add()
        order_dict = mongo_order.get()
        assert order_dict["status"] == "Pending"
        assert order_dict["user"]["name"] == order.user.name

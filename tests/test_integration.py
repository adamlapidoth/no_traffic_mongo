import pytest

from mongo_classes import MUser, MItem, MOrder
from schema import Order


@pytest.mark.usefixtures("_clear_users", "_clear_items", "_clear_orders")
def test_basic_order(db, user_1, mouse, laptop):
    mongo_user = MUser(db, user_1)
    mongo_user.add()
    mongo_item_1 = MItem(db, mouse)
    mongo_item_1.add()
    mongo_item_2 = MItem(db, laptop)
    mongo_item_2.add()
    mongo_item_2.edit("quantity", 10)
    new_order = Order(
        user_1, [mongo_item_2.from_mongo_to_obj(), mongo_item_1.from_mongo_to_obj()]
    )
    mongo_order = MOrder(db, new_order)
    mongo_order.add()

    mongo_order_obj = mongo_order.from_mongo_to_obj()
    assert mongo_order_obj.total_price == 12050
    assert mongo_order_obj == new_order

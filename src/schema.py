from typing import List


class Item:
    def __init__(self, product_id: str, name: str, price: int, quantity: int):
        self.product_it = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id


class Shipment:
    def __init__(self, user: User, items: List[Item] = None):
        if items is None:
            items = []
        self.items = items
        self.user_id = user.user_id
        self.status = "Pending"
        self.total_price = sum(it.price * it.quantity for it in items)

from typing import List


class Item:
    def __init__(self, product_id: str, name: str, price: int, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        if not isinstance(other, Item):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.product_id == other.product_id
            and self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )


class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    def __eq__(self, other):
        if not isinstance(other, User):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.user_id == other.user_id and self.name == other.name


class Order:
    def __init__(
        self,
        user: User,
        items: List[Item] = None,
        status: str = "Pending",
        total_price: float = None,
    ):
        self.user = user
        if items is None:
            items = []
        self.items = items
        self.status = status
        self.total_price = (
            sum(it.price * it.quantity for it in items)
            if total_price is None
            else total_price
        )

    def __eq__(self, other):
        if not isinstance(other, Order):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.user == other.user
            and self.items == other.items
            and self.status == other.status
            and self.total_price == other.total_price
        )

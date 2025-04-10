import copy
from datetime import datetime, timezone

from schema import User, Item, Order


class MCollection:
    def __init__(self, db, collection_name):
        self.col = getattr(db, collection_name)

    def create(self, my_obj):
        item_dict = copy.deepcopy(vars(my_obj))
        item_dict["create_date_utc"] = datetime.now(timezone.utc)
        ret = self.col.insert_one(item_dict)
        return ret

    def delete(self, my_obj):
        ret = self.col.delete_one({"name": my_obj.name})
        return ret

    def read(self, my_obj):
        ret = self.col.find_one({"name": my_obj.name})
        return ret

    def update(self, my_obj, field, new_val):
        update_dict = {"update_date_utc": datetime.now(timezone.utc), field: new_val}
        ret = self.col.update_one({"name": my_obj.name}, {"$set": update_dict})
        return ret


class MObj:
    def __init__(self, db, collection_name: str, obj):
        self.mongo_collection = MCollection(db, collection_name)
        self.obj = obj

    def add(self):
        return self.mongo_collection.create(self.obj)

    def edit(self, field, new_val):
        ret = self.mongo_collection.update(self.obj, field, new_val)
        setattr(self.obj, field, new_val)
        return ret

    def get(self):
        return self.mongo_collection.read(self.obj)

    def delete(self):
        return self.mongo_collection.delete(self.obj)


class MUser(MObj):
    def __init__(self, db, user: User):
        super().__init__(db, "users", user)

    def from_mongo_to_obj(self) -> User:
        user_dict = self.get()
        user_dict.pop("create_date_utc")
        user_dict.pop("_id")
        user_dict.pop("update_date_utc", None)
        return User(**user_dict)


class MItem(MObj):
    def __init__(self, db, item: Item):
        super().__init__(db, "items", item)
        self.cls = type(item)

    def from_mongo_to_obj(self) -> Item:
        item_dict = self.get()
        item_dict.pop("create_date_utc")
        item_dict.pop("_id")
        item_dict.pop("update_date_utc", None)
        return Item(**item_dict)


class MOrder(MObj):
    def __init__(self, db, order: Order):
        super().__init__(db, "orders", order)
        self.cls = Order

    def from_mongo_to_obj(self) -> Order:
        order_dict = self.get()
        order_dict.pop("create_date_utc")
        order_dict.pop("_id")
        order_dict.pop("update_date_utc", None)
        return Order(**order_dict)

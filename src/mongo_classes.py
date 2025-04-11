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

    def from_mongo_to_obj(self):
        obj_dict = self.get()
        obj_dict.pop("create_date_utc")
        obj_dict.pop("_id")
        obj_dict.pop("update_date_utc", None)
        return type(self.obj)(**obj_dict)


class MUser(MObj):
    def __init__(self, db, user: User):
        super().__init__(db, "users", user)


class MItem(MObj):
    def __init__(self, db, item: Item):
        super().__init__(db, "items", item)


class MOrder(MObj):
    def __init__(self, db, order: Order):
        super().__init__(db, "orders", order)

    def add(self):
        order_dict = copy.deepcopy(vars(self.obj))
        user = order_dict.pop("user")
        order_dict["user"] = copy.deepcopy(vars(user))
        items_list = order_dict.pop("items")
        order_dict["items"] = [copy.deepcopy(vars(it)) for it in items_list]
        order_dict["create_date_utc"] = datetime.now(timezone.utc)
        ret = self.mongo_collection.col.insert_one(order_dict)
        return ret

    def get(self):
        ret = self.mongo_collection.col.find_one({"user.name": self.obj.user.name})
        return ret

from schema import User


class MCollection:
    def __init__(self, db, collection_name):
        self.col = getattr(db, collection_name)

    def create(self, my_obj):
        item_dict = vars(my_obj)
        ret = self.col.insert_one(item_dict)
        return ret

    def delete(self, my_obj):
        ret = self.col.delete_one({"name": my_obj.name})
        return ret

    def read(self, my_obj):
        ret = self.col.find_one({"name": my_obj.name})
        return ret

    def update(self, my_obj, field, new_val):
        ret = self.col.update_one({"name": my_obj.name}, {"$set": {field: new_val}})
        return ret


class MUser:
    def __init__(self, db, collection_name: str, user: User):
        self.mongo_collection = MCollection(db, collection_name)
        self.user_obj = user

    def add(self):
        return self.mongo_collection.create(self.user_obj)

    def edit(self, field, new_val):
        ret = self.mongo_collection.update(self.user_obj, field, new_val)
        setattr(self.user_obj, field, new_val)
        return ret

    def get(self):
        return self.mongo_collection.read(self.user_obj)

    def delete(self):
        return self.mongo_collection.delete(self.user_obj)


class MItem(MCollection):
    pass


class MOrder(MCollection):
    pass

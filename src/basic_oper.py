def create_item(db, item):
    items_col = db.items
    item_dict = vars(item)
    ret = items_col.insert_one(item_dict)
    return ret


def get_item_by_name(db, item_name: str) -> dict:
    items_col = db.items
    ret = items_col.find_one({"name": item_name})
    return ret


def update_field_in_item(db, item_name, field, new_val):
    items_col = db.items
    ret = items_col.update_one({"name": item_name}, {"$set": {field: new_val}})
    return ret


def delete_item_by_name(db, item_name):
    items_col = db.items
    ret = items_col.delete_one({"name": item_name})
    return ret

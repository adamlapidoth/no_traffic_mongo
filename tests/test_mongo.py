from pymongo.results import InsertOneResult


def test_create_item(mouse, db):
    items_col = db.items
    item_dict = vars(mouse)
    ret: InsertOneResult = items_col.insert_one(item_dict)
    assert ret.acknowledged
    assert ret.inserted_id

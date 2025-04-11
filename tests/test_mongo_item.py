from mongo_classes import MItem


class TestMongoItem:
    def test_comparison_from_mongo_to_obj(self, db, laptop, _clear_items):
        mongo_laptop = MItem(db, laptop)
        mongo_laptop.add()
        assert mongo_laptop.from_mongo_to_obj() == laptop

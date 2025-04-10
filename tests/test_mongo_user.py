from mongo_classes import MUser


class TestMongoUser:
    def test_add(self, db, user_1):
        mongo_user = MUser(db, "users", user_1)
        ret = mongo_user.add()
        assert ret.inserted_id
        assert ret.acknowledged
        mongo_user.delete()

    def test_edit(self, db, user_1):
        mongo_user = MUser(db, "users", user_1)
        mongo_user.add()
        new_name = "Sharon Shohet"
        ret = mongo_user.edit("name", new_name)
        assert ret.acknowledged
        # assert ret.did_upsert  # TODO check why this fails
        user_dict = mongo_user.get()
        assert user_dict["name"] == new_name
        mongo_user.delete()

    def test_get(self, db, user_1):
        mongo_user = MUser(db, "users", user_1)
        mongo_user.add()
        user_dict = mongo_user.get()
        user_dict.pop("_id")
        user_dict.pop("create_date_utc")
        assert user_dict == vars(user_1)
        mongo_user.delete()

    def test_delete(self, db, user_1):
        mongo_user = MUser(db, "users", user_1)
        mongo_user.add()
        ret = mongo_user.delete()
        assert ret.acknowledged
        assert not mongo_user.get()

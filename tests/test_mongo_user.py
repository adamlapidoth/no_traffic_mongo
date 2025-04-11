import pytest

from mongo_classes import MUser
from schema import User


class TestMongoUser:
    @pytest.mark.usefixtures("_clear_users")
    def test_add(self, db, user_1):
        mongo_user = MUser(db, user_1)
        ret = mongo_user.add()
        assert ret.inserted_id
        assert ret.acknowledged

    @pytest.mark.usefixtures("_clear_users")
    def test_edit(self, db, user_1):
        mongo_user = MUser(db, user_1)
        mongo_user.add()
        new_name = "Sharon Shohet"
        ret = mongo_user.edit("name", new_name)
        assert ret.acknowledged
        # assert ret.did_upsert  # TODO check why this fails
        user_dict = mongo_user.get()
        assert user_dict["name"] == new_name

    @pytest.mark.usefixtures("_clear_users")
    def test_get(self, db, user_1):
        mongo_user = MUser(db, user_1)
        mongo_user.add()
        user_obj = mongo_user.from_mongo_to_obj()
        assert user_obj == user_1

    def test_delete(self, db, user_1):
        mongo_user = MUser(db, user_1)
        mongo_user.add()
        ret = mongo_user.delete()
        assert ret.acknowledged
        assert not mongo_user.get()

    @pytest.mark.usefixtures("_clear_users")
    def test_remove_all_users(self, db):
        mongo_user = MUser(db, User(name="Ilan", user_id="hhh"))
        mongo_user_1 = MUser(db, User(name="Omri", user_id="ooo"))
        mongo_user_2 = MUser(db, User(name="Sharon", user_id="sss"))
        mongo_user.add()
        mongo_user_1.add()
        mongo_user_2.add()

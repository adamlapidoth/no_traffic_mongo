from basic_oper import (
    get_item_by_name,
    create_item,
    update_field_in_item,
    delete_item_by_name,
)


def test_create_item(db, mouse):
    ret = create_item(db=db, item=mouse)
    assert ret.acknowledged
    assert ret.inserted_id
    delete_item_by_name(db=db, item_name=mouse.name)


def test_get_item_by_name(db, mouse):
    create_item(db, mouse)
    mouse_dict = get_item_by_name(db=db, item_name=mouse.name)
    assert mouse_dict["name"] == "mouse"
    assert mouse_dict["price"] == 50
    delete_item_by_name(db=db, item_name=mouse.name)


def test_update_field_in_item(db, laptop):
    create_item(db, laptop)
    new_price = 400
    assert update_field_in_item(
        db=db, item_name=laptop.name, field="price", new_val=new_price
    )
    laptop_dict = get_item_by_name(db=db, item_name=laptop.name)
    assert laptop_dict["price"] == new_price
    delete_item_by_name(db=db, item_name=laptop.name)


def test_delete_item_by_name(db, laptop):
    create_item(db, item=laptop)
    assert delete_item_by_name(db=db, item_name=laptop.name)
    assert not get_item_by_name(db=db, item_name=laptop.name)

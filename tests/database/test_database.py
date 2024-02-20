import pytest
from modules.common.database import Database
from sqlite3 import OperationalError
from datetime import datetime, timedelta


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name(name='Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    cookies_count = db.select_product_qnt_by_id(4)

    assert cookies_count[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('Замовлення', orders)

    # Check quantity of orders equals to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


# Індивідуальна частина
@pytest.mark.database
def test_detailed_orders_by_name(db):
    name = 'Sergii'
    orders = db.get_detailed_orders_by_name(name)
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'


@pytest.mark.database
def test_insert_invalid_product(db):
    products_start_len = len(db.get_all_products())
    try:
        db.insert_product(5, 'печиво', 'солоне', 'invalid_count')
    except OperationalError as err:
        print('Не записано!')
    products_end_len = len(db.get_all_products())

    assert products_start_len == products_end_len


@pytest.mark.database
def test_last_order_is_not_earlier_than_one_year(updated_orders):
    orders = updated_orders.get_detailed_orders()
    last_order_date = datetime.strptime(orders[-1][-1], "%Y-%m-%d %H:%M:%S")
    current_date = datetime.now()
    difference = current_date - last_order_date
    one_year = timedelta(days=365)
    assert difference < one_year


@pytest.mark.database
def test_update_order_date_by_id(db):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.update_order_date_by_id(1, current_date)
    date = db.get_detailed_orders()[0][4]
    assert date == current_date


@pytest.mark.database
def test_avg_quantity_more_than_10(db):
    avg_qnt = db.get_average_quantity_from_products()[0][0]
    assert avg_qnt > 10


@pytest.mark.database
def test_insert_multiple_products(db):
    values_to_insert_count = 10
    products_count_before_insert = db.get_products_count()
    db.insert_multiple_products(start=products_count_before_insert+1,
                                count=products_count_before_insert+values_to_insert_count)

    products_count_after_insert = db.get_products_count()
    assert products_count_after_insert > products_count_before_insert


@pytest.mark.database
def test_sort_products_by_description(db):
    """
    The test checks sorting by the 'description' field.
    It verifies if the items are sorted correctly by the length of the description.
    """
    products = db.sort_products_by_description_length()
    assert len(products[0][1]) > len(products[-1][1])


@pytest.mark.database
def test_sort_products_by_quantity(db):
    products = db.sort_products_by_quantity()
    assert products[0][1] > products[-1][1]

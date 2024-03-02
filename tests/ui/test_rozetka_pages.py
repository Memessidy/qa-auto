import pytest


@pytest.mark.ui
def test_product_founded(rozetka):
    product_to_found = "iPhone 15"
    rozetka.find_product(product_to_found)
    assert rozetka.product_link


@pytest.mark.ui
def test_add_product_to_cart(rozetka):
    rozetka.open_product_page()
    rozetka.save_product_price()
    rozetka.find_buy_button()
    rozetka.add_product_to_cart()
    # shows the price of this product
    assert rozetka.find_full_price() > 0


@pytest.mark.ui
def test_add_one_of_existing_products_to_cart(rozetka):
    count_in_the_cart_before = rozetka.get_product_count_in_cart()
    rozetka.add_one_more_product()
    count_in_the_cart_after = rozetka.get_product_count_in_cart()
    assert count_in_the_cart_after > count_in_the_cart_before


@pytest.mark.ui
def test_delete_one_of_existing_products_from_cart(rozetka):
    count_in_the_cart_before = rozetka.get_product_count_in_cart()
    rozetka.delete_one_more_product()
    count_in_the_cart_after = rozetka.get_product_count_in_cart()
    assert count_in_the_cart_after < count_in_the_cart_before


@pytest.mark.ui
def test_add_new_product_to_cart(rozetka):
    rozetka.add_new_product_to_cart('AirPods Pro')
    # calculate all prices
    assert rozetka.find_full_price() == sum(rozetka.prices.values())


@pytest.mark.ui
def test_delete_product_from_cart(rozetka_with_one_product):
    rozetka_with_one_product.delete_product_from_cart()
    assert rozetka_with_one_product.check_cart_is_empty()

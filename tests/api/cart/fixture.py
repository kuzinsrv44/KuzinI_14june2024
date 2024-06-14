import pytest
from page.service_page import cart


def create_product(client):
    global_id = 3038490
    """
    TODO create product
    """
    return global_id


@pytest.fixture(scope="function")
def precon_create_product(client):
    return create_product(client)


@pytest.fixture(scope="function")
def precon_add_product_to_cart(client):
    global_id = create_product(client)
    inner_id_book = cart.get_info(client).json()["products"][0]["id"]
    return inner_id_book, global_id

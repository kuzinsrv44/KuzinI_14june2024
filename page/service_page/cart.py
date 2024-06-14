import allure
from utils.api import Api

Service = "Cart"
Resource = "api/v1/cart"


def get_info(client, Param=None):
    api = Api(client=client)
    if Param is None:
        Param = {}
    with allure.step("Get info cart"):
        response = api.get(path=Resource, params=Param)
        return response


def add(client, body_):
    api = Api(client=client)
    with allure.step("Add product to cart"):
        response = api.post(path=Resource + "/product", json=body_)
        return response


def update(client, body_):
    api = Api(client=client)
    with allure.step("Update product in cart"):
        response = api.put(path=Resource, json=body_)
        return response


def delete(client, id):
    api = Api(client=client)
    with allure.step("Delete product from cart"):
        response = api.delete(path=Resource + "/product/" + str(id))
        return response

import allure
from utils import assertions as a

from page.service_page import cart
from validate_schema import validate_schema
from fixture import precon_create_product, precon_add_product_to_cart

epic = "Корзина"
feature = "Добавление товара в корзину"
story = "API"


class TestCartPositive:

    @allure.epic(epic)
    @allure.feature(feature)
    @allure.story(story)
    @allure.title("Пустая корзина")
    def test_clear_cart(self, client):
        response = cart.get_info(client)
        a.httpStatusEquals(response.status_code, 200, description="cart.get_info")
        response = response.json()
        validate_schema(response)
        a.equals(response["addBonuses"], 0, 'cost')
        a.equals(response["cost"], 0, 'cost')
        a.equals(response["costGiftWrap"], None, 'costGiftWrap')
        a.equals(response["costWithBonuses"], 0, 'costWithBonuses')
        a.equals(response["costWithSale"], 0, 'costWithSale')
        a.equals(response["disabledProducts"], [], 'disabledProducts')
        a.equals(response["discount"], 0, 'discount')
        a.equals(response["gifts"], [], 'gifts')
        a.equals(response["preorderProducts"], [], 'preorderProducts')
        a.equals(response["products"], [], 'products')
        a.equals(response["promoCode"], None, 'promoCode')
        a.equals(response["weight"], 0, 'weight')

    @allure.epic(epic)
    @allure.feature(feature)
    @allure.story(story)
    @allure.title("Добавить товар в корзину")
    def test_add_cart(self, client, precon_create_product):
        global_id = precon_create_product
        body_ = {
            "id": global_id,
            "adData": {
                "item_list_name": "index",
                "product_shelf": "Новинки литературы"
            }
        }
        response = cart.add(client, body_=body_)
        a.httpStatusEquals(response.status_code, 200, description="cart.add")
        response = cart.get_info(client)
        a.httpStatusEquals(response.status_code, 200, description="cart.get_info")
        response = response.json()
        validate_schema(response)
        a.equals(response["addBonuses"], 0, 'cost')
        a.equals(response["cost"], 794, 'cost')
        a.equals(response["costGiftWrap"], None, 'costGiftWrap')
        a.equals(response["costWithBonuses"], 662, 'costWithBonuses')
        a.equals(response["costWithSale"], 662, 'costWithSale')
        a.equals(response["disabledProducts"], [], 'disabledProducts')
        a.equals(response["discount"], 132, 'discount')
        a.equals(response["gifts"], [], 'gifts')
        a.equals(response["preorderProducts"], [], 'preorderProducts')
        a.equals(response["promoCode"], None, 'promoCode')
        a.equals(response["weight"], 410, 'weight')
        a.equals(response["products"][0]["goodsId"], global_id, 'goodsId')
        a.equals(response["products"][0]["quantity"], 1, 'goodsId')

    @allure.epic(epic)
    @allure.feature(feature)
    @allure.story(story)
    @allure.title("Изменить количество товара в корзину")
    def test_update_cart(self, client, precon_add_product_to_cart):
        inner_id_book, global_id = precon_add_product_to_cart
        body_ = [
            {
                "id": inner_id_book,
                "quantity": 3
            }
        ]
        response = cart.update(client, body_=body_)
        a.httpStatusEquals(response.status_code, 200, description="cart.update")
        response = cart.get_info(client)
        a.httpStatusEquals(response.status_code, 200, description="cart.get_info")
        response = response.json()
        validate_schema(response)
        a.equals(response["addBonuses"], 0, 'cost')
        a.equals(response["cost"], 2382, 'cost')
        a.equals(response["costGiftWrap"], None, 'costGiftWrap')
        a.equals(response["costWithBonuses"], 1905, 'costWithBonuses')
        a.equals(response["costWithSale"], 1905, 'costWithSale')
        a.equals(response["disabledProducts"], [], 'disabledProducts')
        a.equals(response["discount"], 477, 'discount')
        a.equals(response["gifts"], [], 'gifts')
        a.equals(response["preorderProducts"], [], 'preorderProducts')
        a.equals(response["promoCode"], None, 'promoCode')
        a.equals(response["weight"], 1230, 'weight')
        a.equals(response["products"][0]["goodsId"], global_id, 'goodsId')
        a.equals(response["products"][0]["quantity"], 3, 'goodsId')

    @allure.epic(epic)
    @allure.feature(feature)
    @allure.story(story)
    @allure.title("Удалить товар из корзины")
    def test_del_cart(self, client, precon_add_product_to_cart):
        inner_id_book, global_id = precon_add_product_to_cart
        response = cart.delete(client, id=inner_id_book)
        a.httpStatusEquals(response.status_code, 204, description="cart.delete")
        response = cart.get_info(client)
        a.httpStatusEquals(response.status_code, 200, description="cart.get_info")
        response = response.json()
        validate_schema(response)
        a.equals(response["addBonuses"], 0, 'cost')
        a.equals(response["cost"], 0, 'cost')
        a.equals(response["costGiftWrap"], None, 'costGiftWrap')
        a.equals(response["costWithBonuses"], 0, 'costWithBonuses')
        a.equals(response["costWithSale"], 0, 'costWithSale')
        a.equals(response["disabledProducts"], [], 'disabledProducts')
        a.equals(response["discount"], 0, 'discount')
        a.equals(response["gifts"], [], 'gifts')
        a.equals(response["preorderProducts"], [], 'preorderProducts')
        a.equals(response["products"], [], 'products')
        a.equals(response["promoCode"], None, 'promoCode')
        a.equals(response["weight"], 0, 'weight')

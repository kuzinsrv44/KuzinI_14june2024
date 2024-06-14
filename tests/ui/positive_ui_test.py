import allure
from utils import assertions as a
from page.ui_page.general import General

epic = "Корзина"
feature = "Добавление товара в корзину"
story = "UI"


class TestUICartPositive:

    @allure.epic(epic)
    @allure.feature(feature)
    @allure.story(story)
    @allure.title("Добавить товар в корзину")
    def test_add_product_to_cart(self, client):
        page = General(client)
        page.open()
        with allure.step('Нажать на первый товар на странице'):
            page.click_element(*page.first_product_slider_selector)
        with allure.step('Нажать купить'):
            page.click_element(*page.button_product_offer_selector)
        with allure.step('Проверить уведомления в корзине'):
            page.is_element_present(*page.cart_count_product_selector)
            count_product = page.get_element_value(*page.cart_count_product_selector)
            a.equals(count_product, "1", "Корзина должна содержать 1 товар")
        with allure.step('Перейти в корзину'):
            page.click_element(*page.button_cart_selector)
        with allure.step('Проверить тему'):
            page.wait_for_element(*page.title_selector)
            page.is_element_present(*page.title_selector)
            title = page.get_element_value(*page.title_selector)
            a.regexp(title, r"КОРЗИНА\s.*?1", "Заголовок")
        with allure.step('Проверить наличие элементов на странице'):
            page.is_element_present(*page.button_confirm_selector)
            page.is_element_present(*page.button_trash_selector)
            page.is_element_present(*page.minus_quantity_selector)
            page.is_element_present(*page.plus_quantity_selector)
            page.is_element_present(*page.cart_info_selector)


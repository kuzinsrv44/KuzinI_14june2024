from selenium.webdriver.common.by import By
from page.ui_page.base import Base
import allure

class General(Base):
    # Селектор кнопки "Добавить в корзину"
    first_product_slider_selector = (By.CSS_SELECTOR, '[data-chg-slider-type="novelty"] .slider__item:nth-child(1) .product-picture')
    button_product_offer_selector = (By.CSS_SELECTOR, '.product-offer-button')
    add_to_cart_button_selector = (By.CSS_SELECTOR, '.action-button.blue:not(.action-button--pre-order)')
    button_cart_selector = (By.CSS_SELECTOR, '[href="/cart"]')
    cart_count_product_selector = (By.CSS_SELECTOR, '.header-cart__badge')
    title_selector = (By.CSS_SELECTOR, 'h1')
    button_confirm_selector = (By.CSS_SELECTOR, '.cart-sidebar__order-button')
    plus_quantity_selector = (By.CSS_SELECTOR, '.product-quantity__button--right')
    minus_quantity_selector = (By.CSS_SELECTOR, '.product-quantity__button--left')
    button_trash_selector = (By.CSS_SELECTOR, '.cart-item__actions-button--delete')
    cart_info_selector = (By.CSS_SELECTOR, '.cart-sidebar__info')

    def __init__(self, client):
        super().__init__()
        self.client = client

    def open(self):
        # Открываем страницу каталога
        with allure.step("Открываем страницу каталога"):
            general_url = self.client["host_ui"]
            self.open_url(general_url)

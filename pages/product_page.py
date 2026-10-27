from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    # Новый метод: получает название товара со страницы
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Новый метод: получает цену товара со страницы
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Обновленный метод: принимает название товара как аргумент
    def should_be_success_message(self, product_name):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in success_message, f"Название товара '{product_name}' не найдено в сообщении '{success_message}'"

    # Обновленный метод: принимает цену товара как аргумент
    def should_be_correct_basket_total(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Цена товара '{product_price}' не совпадает со стоимостью корзины '{basket_total}'"
from .locators import BasePageLocators
from .base_page import BasePage
import pytest

class BasketPage(BasePage):
    def should_be_not_product_in_the_basket(self):
        assert self.is_not_element_present(*BasePageLocators.REMAINDER_PRODUCT), 'there is a product in the basket'
    
    def should_be_the_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_YOUR_BASKET_IS_EMPTY), 'basket is not empty'
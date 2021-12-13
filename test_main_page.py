from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.locators import BasePageLocators
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import pytest

HOME_PAGE = "http://selenium1py.pythonanywhere.com/"
@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"    
    page = MainPage(browser, HOME_PAGE)   # browser, инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open(browser)               # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, HOME_PAGE)
    page.open(browser)
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    browser.get(HOME_PAGE)
    base_page = BasePage(browser, browser.current_url)
    base_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_product_in_the_basket()
    basket_page.should_be_the_basket_is_empty()

    



  


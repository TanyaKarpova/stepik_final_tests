from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.locators import ProductPageLocators
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
import time
import pytest


LINK_PRODUCT = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LINK_PRODUCT2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
LINK_PRODUCT_WITH_ALERT = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    
    browser.get(LINK_PRODUCT_WITH_ALERT)
    name1 = browser.find_element(By.CSS_SELECTOR,'.product_main h1').text
    browser.find_element(By.CSS_SELECTOR,'.btn.btn-add-to-basket').click() 
    base_page = BasePage(browser, LINK_PRODUCT_WITH_ALERT)
    base_page.solve_quiz_and_get_code()
    time.sleep(2)

    name2 = browser.find_element(By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong').text
    price1 = browser.find_element(By.CSS_SELECTOR,'p.price_color').text
    price2 = browser.find_element(By.CSS_SELECTOR,'div.alert > div > p:nth-child(1) > strong').text
    
    assert name1 == name2, 'Names of book are different'
    assert price1 == price2, 'Prices of book are different'

@pytest.mark.skip 
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.get(link)
    name1 = browser.find_element(By.CSS_SELECTOR,'.product_main h1').text
    
    browser.find_element(By.CSS_SELECTOR,'.btn.btn-add-to-basket').click() 
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    time.sleep(2)

    name2 = browser.find_element(By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong').text
    price1 = browser.find_element(By.CSS_SELECTOR,'p.price_color').text
    price2 = browser.find_element(By.CSS_SELECTOR,'div.alert > div > p:nth-child(1) > strong').text
    
    assert name1 == name2, 'Names of book are different'
    assert price1 == price2, 'Prices of book are different'


@pytest.mark.skip 
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    browser.get(LINK_PRODUCT)
    browser.find_element(By.CSS_SELECTOR,'.btn.btn-add-to-basket').click()
    page = BasePage(browser, browser.current_url)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented in basket, but should not be"

@pytest.mark.skip 
def test_guest_cant_see_success_message(browser):
    browser.get(LINK_PRODUCT)
    page = BasePage(browser, browser.current_url)
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented in page product, but should not be"

@pytest.mark.skip 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    browser.get(LINK_PRODUCT)
    button_add = browser.find_element(By.CSS_SELECTOR,'.btn.btn-add-to-basket').click() 
    page = BasePage(browser, browser.current_url)
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented in basket, but should not be"


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = BasePage(browser, LINK_PRODUCT2)
    page.open(browser)
    page.should_be_login_link()
     
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, LINK_PRODUCT2)
    page.open(browser)
    assert page.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link not found'
    browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    login_page = LoginPage(browser, LINK_PRODUCT2)
    login_page.should_be_login_url()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.get(LINK_PRODUCT)
    base_page = BasePage(browser, browser.current_url)
    base_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_not_product_in_the_basket()
    basket_page.should_be_the_basket_is_empty()

    
    


    




    




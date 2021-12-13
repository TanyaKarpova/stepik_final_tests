from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BUTTON_BASKET = (By.CSS_SELECTOR, 'span a.btn-default')
    # REMAINDER_PRODUCT = (By.CLASS_NAME, 'availability')  # те же самые в BasePageLocators
    # MESSAGE_YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p') 
    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BASKET = (By.CSS_SELECTOR, 'span a.btn-default')
    REMAINDER_PRODUCT = (By.CLASS_NAME, 'availability')
    MESSAGE_YOUR_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p') 
    

    
    
    
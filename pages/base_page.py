
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        # url = "http://selenium1py.pythonanywhere.com/"
        self.url = url

    def open(self, browser):
        self.browser.get(self.url)

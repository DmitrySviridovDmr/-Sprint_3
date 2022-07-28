from selenium.common.exceptions import NoSuchElementException


class Base:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

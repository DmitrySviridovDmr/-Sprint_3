from main import *


class TestRegistration:
    def test_registration_success(self, browser):
        page = Main(browser)
        page.registration_success()

    def test_registration_failed(self, browser):
        page = Main(browser)
        page.registration_already_exist()

    def test_wrong_password(self, browser):
        page = Main(browser)
        page.wrong_password()


class TestLogins:
    def test_login_from_main_page(self, browser):
        page = Main(browser)
        page.login_from_main_page()

    def test_login_from_personal_area(self, browser):
        page = Main(browser)
        page.login_from_personal_area()

    def test_login_from_register_page(self, browser):
        page = Main(browser)
        page.login_from_register_page()

    def test_login_from_forgot_password(self, browser):
        page = Main(browser)
        page.login_from_forgot_password()


class TestPersonalArea:
    def test_redirect_to_personal_area(self, browser):
        page = Main(browser)
        page.redirect_to_personal_area()

    def test_redirect_to_constructor_from_personal_area(self, browser):
        page = Main(browser)
        page.redirect_to_constructor_from_personal_area()

    def test_exit_from_account(self, browser):
        page = Main(browser)
        page.logout_from_account()


class TestConstructor:
    def test_constructor_bun(self, browser):
        page = Main(browser)
        page.constructor_bun()

    def test_constructor_sauce(self, browser):
        page = Main(browser)
        page.constructor_sauce()

    def test_constructor_filling(self, browser):
        page = Main(browser)
        page.constructor_filling()

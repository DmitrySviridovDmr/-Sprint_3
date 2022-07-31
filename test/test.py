from main import *
from locators import *


class TestRegistration:
    def test_registration_success(self, browser):
        page = Main(browser)
        page.open("register")
        page.registration_success()
        assert browser.current_url == Registration.registerLink, "Failed registration"

    def test_registration_already_exist(self, browser):
        page = Main(browser)
        page.open("register")
        page.registration_already_exist()
        error_registration = browser.find_element(*Registration.error_registration_message)
        assert "Такой пользователь уже существует" in error_registration.text

    def test_wrong_password(self, browser):
        page = Main(browser)
        page.open("register")
        page.wrong_password()
        error_password = browser.find_element(*Registration.error_password_message)
        assert "Некорректный пароль" in error_password.text


class TestLogins:
    def test_login_from_main_page(self, browser):
        page = Main(browser)
        page.open("main")
        page.login_from_main_page()
        assert browser.find_element(*MainPage.checkout), "Login Failed"

    def test_login_from_personal_area(self, browser):
        page = Main(browser)
        page.open("login")
        page.login_from_personal_area()
        assert browser.find_element(*MainPage.checkout), "Login Failed"

    def test_login_from_register_page(self, browser):
        page = Main(browser)
        page.open("register")
        page.login_from_register_page()
        assert browser.find_element(*MainPage.checkout), "Login Failed"

    def test_login_from_forgot_password(self, browser):
        page = Main(browser)
        page.open("forgot_password")
        page.login_from_forgot_password()
        assert browser.find_element(*MainPage.checkout), "No login"


class TestPersonalArea:
    def test_redirect_to_personal_area(self, browser):
        page = Main(browser)
        page.open("main")
        page.redirect_to_personal_area()
        assert browser.current_url == Registration.registerLink, "No redirect to Personal Area"

    def test_redirect_to_constructor_from_personal_area(self, browser):
        page = Main(browser)
        page.open("login")
        page.redirect_to_constructor_from_personal_area()
        message = browser.find_element(*MainPage.titleBurg)
        assert "Соберите бургер" in message.text, "No redirect to main page"

    def test_exit_from_account(self, browser):
        page = Main(browser)
        page.open("login")
        page.logout_from_account()
        assert browser.current_url == Registration.registerLink


class TestConstructor:
    def test_constructor_bun(self, browser):
        page = Main(browser)
        page.open("main")
        page.constructor_bun()
        bun_message = browser.find_element(*MainPage.titleBun)
        assert "Булки" in bun_message.text

    def test_constructor_sauce(self, browser):
        page = Main(browser)
        page.open("main")
        page.constructor_sauce()
        sauce_message = browser.find_element(*MainPage.titleSauce)
        assert "Соусы" in sauce_message.text

    def test_constructor_filling(self, browser):
        page = Main(browser)
        page.open("main")
        page.constructor_filling()
        filling_message = browser.find_element(*MainPage.titleFilling)
        assert "Начинки" in filling_message.text

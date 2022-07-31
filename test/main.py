from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
import random
from base import *

some = "qwertyuiopasdfghjklzxcvbnm"
some_random = ''.join(random.choice(some) for i in range(6))
some_random_mail = ''.join(random.choice(some) for x in range(14))


class Main(Base):
    def open(self, link):
        if link == "main":
            self.browser.get("https://stellarburgers.nomoreparties.site/")
        elif link == "register":
            self.browser.get("https://stellarburgers.nomoreparties.site/register")
        elif link == "login":
            self.browser.get("https://stellarburgers.nomoreparties.site/login")
        elif link == "forgot_password":
            self.browser.get("https://stellarburgers.nomoreparties.site/forgot-password")

    def registration_success(self):
        self.browser.find_element(*Registration.nameReg).send_keys(some_random)
        self.browser.find_element(*Registration.emailReg).send_keys(some_random_mail + "1333@mail.ru")
        self.browser.find_element(*Registration.passwordReg).send_keys(some_random)
        self.browser.find_element(*Registration.registerButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/register"))

    def registration_already_exist(self):
        self.browser.find_element(*Registration.nameReg).send_keys(some_random)
        self.browser.find_element(*Registration.emailReg).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*Registration.passwordReg).send_keys("qwerty")
        self.browser.find_element(*Registration.registerButton).click()
        self.browser.execute_script("window.scrollBy(0, 300);")
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(Registration.error_registration_message))

    def wrong_password(self):
        self.browser.find_element(*Registration.nameReg).send_keys(some_random)
        self.browser.find_element(*Registration.emailReg).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*Registration.passwordReg).send_keys("qwer")
        self.browser.find_element(*Registration.registerButton).click()

    def login_from_main_page(self):
        self.browser.find_element(*MainPage.loginButton).click()
        self.browser.find_element(*LoginPage.emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*LoginPage.passwordLog).send_keys("qwerty")
        self.browser.find_element(*LoginPage.enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

    def login_from_personal_area(self):
        self.browser.find_element(*LoginPage.emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*LoginPage.passwordLog).send_keys("qwerty")
        self.browser.find_element(*LoginPage.enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

    def login_from_register_page(self):
        self.browser.find_element(*Registration.loginFromRegister).click()
        self.browser.find_element(*LoginPage.emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*LoginPage.passwordLog).send_keys("qwerty")
        self.browser.find_element(*LoginPage.enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

    def login_from_forgot_password(self):
        self.browser.find_element(*Registration.loginFromRegister).click()
        self.browser.find_element(*LoginPage.emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*LoginPage.passwordLog).send_keys("qwerty")
        self.browser.find_element(*LoginPage.enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

    def redirect_to_personal_area(self):
        self.browser.find_element(*MainPage.personalArea).click()

    def redirect_to_constructor_from_personal_area(self):
        self.browser.find_element(*PersonalArea.constructorButton).click()

    def logout_from_account(self):
        self.browser.find_element(*LoginPage.emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*LoginPage.passwordLog).send_keys("qwerty")
        self.browser.find_element(*LoginPage.enterButton).click()
        self.browser.find_element(*MainPage.personalArea).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(PersonalArea.exitButton))
        self.browser.find_element(*PersonalArea.exitButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/account/profile"))

    def constructor_bun(self):
        self.browser.find_element(*MainPage.fillingButton).click()
        self.browser.find_element(*MainPage.bunButton).click()

    def constructor_sauce(self):
        self.browser.find_element(*MainPage.fillingButton).click()
        self.browser.find_element(*MainPage.sauceButton).click()

    def constructor_filling(self):
        self.browser.find_element(*MainPage.fillingButton).click()

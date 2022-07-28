from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
import random
from base import *

some = "qwertyuiopasdfghjklzxcvbnm"
some_random = ''.join(random.choice(some) for i in range(6))
some_random_mail = ''.join(random.choice(some) for x in range(14))


class Main(Base):
    def registration_success(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/register")
        self.browser.find_element(*nameReg).send_keys(some_random)
        self.browser.find_element(*emailReg).send_keys(some_random_mail + "1333@mail.ru")
        self.browser.find_element(*passwordReg).send_keys(some_random)
        self.browser.find_element(*registerButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/register"))
        assert self.browser.current_url == "https://stellarburgers.nomoreparties.site/login", "Failed registration"

    def registration_already_exist(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/register")
        self.browser.find_element(*nameReg).send_keys(some_random)
        self.browser.find_element(*emailReg).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordReg).send_keys("qwerty")
        self.browser.find_element(*registerButton).click()
        self.browser.execute_script("window.scrollBy(0, 300);")
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > p")))
        error_message = self.browser.find_element(By.CSS_SELECTOR, "#root > div > main > div > p")
        assert "Такой пользователь уже существует" in error_message.text, "No error messsage"

    def wrong_password(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/register")
        self.browser.find_element(*nameReg).send_keys(some_random)
        self.browser.find_element(*emailReg).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordReg).send_keys("qwer")
        self.browser.find_element(*registerButton).click()
        error_password = self.browser.find_element(By.CSS_SELECTOR,
                                                   "#root > div > main > div > form > fieldset:nth-child(3) > div > p")
        assert "Некорректный пароль" in error_password.text, "No error message"

    def login_from_main_page(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")
        self.browser.find_element(*loginButton).click()
        self.browser.find_element(*emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordLog).send_keys("qwerty")
        self.browser.find_element(*enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.browser.find_element(By.CSS_SELECTOR,
                                         "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button"), "No login"

    def login_from_personal_area(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/login")
        self.browser.find_element(*emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordLog).send_keys("qwerty")
        self.browser.find_element(*enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.browser.find_element(By.CSS_SELECTOR,
                                         "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button"), "No login"

    def login_from_register_page(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/register")
        self.browser.find_element(*loginFromRegister).click()
        self.browser.find_element(*emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordLog).send_keys("qwerty")
        self.browser.find_element(*enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.browser.find_element(By.CSS_SELECTOR,
                                         "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button"), "No login"

    def login_from_forgot_password(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/forgot-password")
        self.browser.find_element(*loginFromRegister).click()
        self.browser.find_element(*emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordLog).send_keys("qwerty")
        self.browser.find_element(*enterButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))
        assert self.browser.find_element(By.CSS_SELECTOR,
                                         "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button"), "No login"

    def redirect_to_personal_area(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")
        self.browser.find_element(*personalArea).click()
        assert self.browser.current_url == "https://stellarburgers.nomoreparties.site/login", "No redirect to Personal Area"

    def redirect_to_constructor_from_personal_area(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/login")
        self.browser.find_element(*constructorButton).click()
        message = self.browser.find_element(By.CSS_SELECTOR,
                                            "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1")
        assert "Соберите бургер" in message.text, "No redirect to main page"

    def logout_from_account(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/login")
        self.browser.find_element(*emailLog).send_keys("dmitrysviridov1333@mail.ru")
        self.browser.find_element(*passwordLog).send_keys("qwerty")
        self.browser.find_element(*enterButton).click()
        self.browser.find_element(*personalArea).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(3) > button")))
        self.browser.find_element(*exitButton).click()
        WebDriverWait(self.browser, 5).until(
            expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/account/profile"))
        assert self.browser.current_url == "https://stellarburgers.nomoreparties.site/login"

    def constructor_bun(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")
        self.browser.find_element(*fillingButton).click()
        self.browser.find_element(*bunButton).click()
        bun_message = self.browser.find_element(By.CSS_SELECTOR,
                                                "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(1)")
        assert "Булки" in bun_message.text

    def constructor_sauce(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")
        self.browser.find_element(*fillingButton).click()
        self.browser.find_element(*sauceButton).click()
        sauce_message = self.browser.find_element(By.CSS_SELECTOR,
                                                  "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(3)")
        assert "Соусы" in sauce_message.text

    def constructor_filling(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")
        self.browser.find_element(*fillingButton).click()
        filling_message = self.browser.find_element(By.CSS_SELECTOR,
                                                    "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(5)")
        assert "Начинки" in filling_message.text

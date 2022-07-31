from selenium.webdriver.common.by import By


# форма регистрации
class Registration:
    nameReg = By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input"  # поле ввода Имя
    emailReg = (
        By.CSS_SELECTOR,
        "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input")  # поле ввода email
    passwordReg = (
        By.CSS_SELECTOR,
        "#root > div > main > div > form > fieldset:nth-child(3) > div > div > input")  # поле ввода Пароль
    registerButton = (By.CSS_SELECTOR, "#root > div > main > div > form > button")  # Кнопка Зарегистрироваться
    loginFromRegister = (By.CSS_SELECTOR, "#root > div > main > div > div > p > a")  # кнопка Войти
    registerLink = "https://stellarburgers.nomoreparties.site/login"  # url страницы логина
    error_registration_message = (
        By.CSS_SELECTOR, "#root > div > main > div > p")  # сообщение Такой пользователь уже существует
    error_password_message = (By.CSS_SELECTOR,
                              "#root > div > main > div > form > fieldset:nth-child(3) > div > p")  # сообщение Некорректный пароль


# главная страница
class MainPage:
    loginButton = (By.CSS_SELECTOR,
                   "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button")  # кнопка Войти в аккаунт
    checkout = (By.CSS_SELECTOR,
                "#root > div > main > section.BurgerConstructor_basket__29Cd7.mt-25 > div > button")  # кнопка Оформить заказ
    personalArea = (By.CSS_SELECTOR, "#root > div > header > nav > a > p")  # кнопка Личный кабинет
    bunButton = (By.CSS_SELECTOR,
                 "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(1) > span")  # кнопка Булки
    sauceButton = (By.CSS_SELECTOR,
                   "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(2) > span")  # кнопка Соусы
    fillingButton = (By.CSS_SELECTOR,
                     "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2) > div:nth-child(3) > span")  # Кнопка Начинки
    titleBurg = (By.CSS_SELECTOR,
                 "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > h1")  # надпись Соберите бургер
    titleBun = (By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(1)")# надпись Булки
    titleSauce = (By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(3)")# надпись Соусы
    titleFilling = (By.CSS_SELECTOR, "#root > div > main > section.BurgerIngredients_ingredients__1N8v2 > div.BurgerIngredients_ingredients__menuContainer__Xu3Mo > h2:nth-child(5)")# надпись Начинки


# личный кабинет
class PersonalArea:
    restorePassword = (
        By.CSS_SELECTOR, "#root > div > main > div > div > p:nth-child(2) > a")  # кнопка восстановить пароль
    constructorButton = (
        By.CSS_SELECTOR, "#root > div > header > nav > ul > li:nth-child(1) > a > p")  # кнопка Конструктор
    exitButton = (By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(3) > button")  # кнопка Выход


# страница логирования
class LoginPage:
    emailLog = (
        By.CSS_SELECTOR,
        "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input")  # поле ввода email
    passwordLog = (
        By.CSS_SELECTOR,
        "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input")  # поле ввода Пароль
    enterButton = (By.CSS_SELECTOR, "#root > div > main > div > form > button")  # кнопка Войти

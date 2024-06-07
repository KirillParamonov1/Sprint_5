from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Форма регистрации
    USER_NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]")  # имя
    USER_EMAIL_INPUT = (By.XPATH, "(.//input[@name='name'])[2]")  # логин
    USER_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # пароль
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    REG_PAGE_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # кнопка "Войти"
    REG_PAGE_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")

    # Кнопка "Войти в аккаунт"/"Оформить заказ" на Главной странице
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ" на главной странице

    # Раздел Конструктор
    MAIN_PAGE_BREAD_TAB = (By.XPATH, ".//body//main//span[text()='Булки']")  # Вкладка Булки
    MAIN_PAGE_SOUCES_TAB = (By.XPATH, ".//body//main//span[text()='Соусы']")  # Вкладка Соусы
    MAIN_PAGE_FILLINGS_TAB = (By.XPATH, ".//body//main//span[text()='Начинки']")  # Вкладка Начинки
    MAIN_PAGE_TAB_CONSTRUCTOR = (By.XPATH, ".//div[contains(@class, 'current')]/span")  # выбранный таб в конструкторе

    # Личный кабинет
    PROFILE_PAGE_LOGO_LINK = (By.XPATH, ".//body//header//div/a[@href='/']")  # Ссылка на Лого на странице Личный кабинет
    PROFILE_PAGE_CONSTRUCTOR_LINK = (By.XPATH, ".//body//header//p[text()='Конструктор']")  # Сссылка на Конструктор на странице Личный кабинет
    PROFILE_PAGE_SAVE_BUTTON = (By.XPATH, ".//body//main//button[text()='Сохранить']")  # Кнопка "Сохранить" на странице Личный кабинет
    PROFILE_PAGE_EXIT_BUTTON = (By.XPATH, ".//body//main//button[text()='Выход']")  # Кнопка "Выход" на странице Личный кабинет

    MAIN_PAGE_PROFILE_LINK = (By.XPATH, ".//header//a[@href='/account']")  # Ссылка "Личный Кабинет" на главной странице
    MAIN_MENU_ITEM_PROFILE = (By.XPATH, ".//a[text()='Профиль']") #Ссылка на "Профиль" в личном кабинете

    # Форма авторизации
    AUTH_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" на странице авторизации
    AUTH_PAGE_LOGIN_FIELD = (By.XPATH, ".//input[@name='name']")  # Поле ввода логина
    AUTH_PAGE_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввода пароля
    AUTH_FORM = (By.XPATH, ".//main//form")  # Форма ввода на странице авторизации
    HEADER_LOGIN = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок "Вход" на странице авторизации

    # Форма восстановления пароля
    RECOVER_PAGE_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка "Войти" на странице восстановления пароля
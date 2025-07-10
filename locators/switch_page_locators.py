from selenium.webdriver.common.by import By


class SwitchPageLocators:

    YANDEX_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")][.//img[@alt="Yandex"]]']
    DZEN_WINDOW_FIND_BUTTON = [By.XPATH, '//*[text() = "Найти"]']

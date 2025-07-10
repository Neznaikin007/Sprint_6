from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIES_BUTTON = [By.XPATH, '//button[contains(@class, "App_CookieButton")]']
    QUESTIONS = [By.XPATH, '//div[@id="accordion__heading-{}"]']
    ANSWERS = [By.XPATH, '//div[@id="accordion__panel-{}"]']
    LAST_QUESTIONS = [By.XPATH, '//div[@id="accordion__heading-7"]']
    HEADER_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Header_Nav")]//button[text()="Заказать"]']
    MAIN_BLOCK_ORDER_BUTTON = [By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]']
    QUESTIONS_TEXT = [By.XPATH, '//div[contains(@class, "Home_SubHeader") and contains(text(), "Вопросы о важном")]']
    SCOOTER_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']

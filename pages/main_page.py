import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Акцептировать куки')
    def cookies_accept(self):
        self.click_to_element(MainPageLocators.COOKIES_BUTTON)

    @allure.step('Клик на вопрос')
    def click_to_questions(self, num):
        locator_questions_formatted = self.format_locators(MainPageLocators.QUESTIONS, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTIONS)
        return self.click_to_element(locator_questions_formatted)

    @allure.step('Получить ответ')
    def get_answers(self, num):
        locator_answers_formatted = self.format_locators(MainPageLocators.ANSWERS, num)
        return self.get_text_from_element(locator_answers_formatted)

    @allure.step('Создать заказ')
    def create_order(self, button_locator):
        self.scroll_to_element(button_locator)
        self.click_to_element(button_locator)
        order_page = OrderPage(self.driver)
        order_page.set_first_name()
        order_page.set_last_name()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button_get_about_rent()
        order_page.set_delivery_date()
        order_page.set_rental_period()
        order_page.set_scooter_color()
        order_page.set_comment()
        order_page.click_order_and_confirm_buttons()
        order_page.click_see_status()

    @allure.step('Переход на главную страницу по клику на лого самоката')
    def get_main_page_via_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)
        self.scroll_to_element(MainPageLocators.QUESTIONS_TEXT)
        return self.get_text_from_element(MainPageLocators.QUESTIONS_TEXT)
    
import allure
from pages.base_page import BasePage
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
    
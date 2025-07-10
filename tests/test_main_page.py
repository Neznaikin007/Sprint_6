import pytest
import allure
from data import *
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Тестирование получения ответов на вопросы о важном')
    @allure.description('Тестирование получения ответов на вопросы о важном')
    @pytest.mark.parametrize('num, expected_answer', [
        (0, Answers.Answer_0),
        (1, Answers.Answer_1),
        (2, Answers.Answer_2),
        (3, Answers.Answer_3),
        (4, Answers.Answer_4),
        (5, Answers.Answer_5),
        (6, Answers.Answer_6),
        (7, Answers.Answer_7)
    ])
    def test_get_answers_for_questions(self, driver, num, expected_answer):
        main_page = MainPage(driver)
        main_page.cookies_accept()
        main_page.click_to_questions(num)
        assert main_page.get_answers(num) == expected_answer


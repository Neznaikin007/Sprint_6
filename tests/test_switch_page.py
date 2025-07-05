import allure
from pages.switch_page import SwitchPage


class TestSwitchPage:

    @allure.title('Тестирование перехода на страницу "Дзен"')
    def test_go_to_dzen_via_yandex_logo(self, driver):
        switch_page = SwitchPage(driver)
        switch_page.get_dzen_via_yandex_logo()
        actual_result = switch_page.get_find_button_on_dzen()
        expected_result = 'Найти'
        assert actual_result == expected_result

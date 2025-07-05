import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.title('Тестирование создания заказа')
@allure.description('Тестирование создания заказа и перехода на главную страницу по клику на логотип Самоката')
@pytest.mark.parametrize('button_order_locator',
                         [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.MAIN_BLOCK_ORDER_BUTTON])
def test_go_to_main_page_via_scooter_logo(driver, button_order_locator):
        main_page = MainPage(driver)
        main_page.cookies_accept()
        main_page.create_order(button_order_locator)
        actual_result = main_page.get_main_page_via_scooter_logo()
        expected_result = 'Вопросы о важном'
        assert actual_result == expected_result
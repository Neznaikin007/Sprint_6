import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage


@allure.title('Тестирование создания заказа')
@allure.description('Тестирование создания заказа и перехода на главную страницу по клику на логотип Самоката')
@pytest.mark.parametrize('button_order_locator',
                         [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.MAIN_BLOCK_ORDER_BUTTON])
def test_go_to_main_page_via_scooter_logo(driver, button_order_locator):
        order_page = OrderPage(driver)
        order_page.create_order(button_order_locator)
        actual_result = order_page.get_main_page_via_scooter_logo()
        expected_result = 'Вопросы о важном'
        assert actual_result == expected_result
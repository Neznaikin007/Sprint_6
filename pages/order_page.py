import allure
from pages.base_page import BasePage
from pages.main_page import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнено поле 'Имя'")
    def set_first_name(self, first_name='Петя'):
         self.add_text_to_element(OrderPageLocators.CUSTOMER_FIRST_NAME, first_name)
        
    @allure.step("Заполнено поле 'Фамилия'")
    def set_last_name(self, last_name='Петров'):
        self.add_text_to_element(OrderPageLocators.CUSTOMER_LAST_NAME, last_name)

    @allure.step("Заполнено поле 'Адрес: куда привезти заказ'")
    def set_address(self, address='улица Пушкина'):
        self.add_text_to_element(OrderPageLocators.CUSTOMER_ADDRESS, address)

    @allure.step("Выбрана станция метро")
    def set_metro_station(self):
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_to_element(OrderPageLocators.DROP_DOWN_STATION_NAME)

    @allure.step("Заполнено поле 'Телефон'")
    def set_phone_number(self, phone_number='12345678909'):
        self.add_text_to_element(OrderPageLocators.CUSTOMER_PHONE, phone_number)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button_get_about_rent(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнено поле с датой 'Куда привезти заказ'")
    def set_delivery_date(self, delivery_data='29.11.2024'):
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_data)

    @allure.step("Выбран срок Аренды")
    def set_rental_period(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECT)

    @allure.step("Выбран цвет самоката")
    def set_scooter_color(self, scooter_color='чёрный жемчуг'):
        self.add_text_to_element(OrderPageLocators.SCOOTER_COLOR, scooter_color)

    @allure.step("Заполнено поле 'Комментарий для курьера'")
    def set_comment(self, comment='нужен сегодня'):
        self.add_text_to_element(OrderPageLocators.COMMENT, comment)

    @allure.step("Клик по кпопкам 'Заказать' и 'Да'")
    def click_order_and_confirm_buttons(self):
        self.click_to_element(OrderPageLocators.FORM_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)

    @allure.step("Клик по кнопке 'Посмотреть статус'")
    def click_see_status(self):
        self.click_to_element(OrderPageLocators.ORDER_STATUS_BUTTON)

    @allure.step("Создать заказ")
    def create_order(self, button_locator):
        self.scroll_to_element(button_locator)
        self.click_to_element(button_locator)
        self.set_first_name()
        self.set_last_name()
        self.set_address()
        self.set_metro_station()
        self.set_phone_number()
        self.click_next_button_get_about_rent()
        self.set_delivery_date()
        self.set_rental_period()
        self.set_scooter_color()
        self.set_comment()
        self.click_order_and_confirm_buttons()
        self.click_see_status()

    @allure.step('Переход на главную страницу по клику на лого самоката')
    def get_main_page_via_scooter_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)
        self.scroll_to_element(MainPageLocators.QUESTIONS_TEXT)
        return self.get_text_from_element(MainPageLocators.QUESTIONS_TEXT)

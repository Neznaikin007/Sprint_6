import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helpers import Generators


class OrderPage(BasePage):

    @allure.step("Заполнено поле 'Имя'")
    def set_first_name(self):
        generators = Generators()
        first_name = generators.generate_first_name()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_FIRST_NAME, first_name)

    @allure.step("Заполнено поле 'Фамилия'")
    def set_last_name(self):
        generators = Generators()
        last_name = generators.generate_last_name()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_LAST_NAME, last_name)

    @allure.step("Заполнено поле 'Адрес: куда привезти заказ'")
    def set_address(self):
        generators = Generators()
        address = generators.generate_address()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_ADDRESS, address)

    @allure.step("Выбрана станция метро")
    def set_metro_station(self):
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_to_element(OrderPageLocators.DROP_DOWN_STATION_NAME)

    @allure.step("Заполнено поле 'Телефон'")
    def set_phone_number(self):
        generators = Generators()
        phone_number = generators.generate_phone_number()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_PHONE, phone_number)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button_get_about_rent(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнено поле с датой 'Куда привезти заказ'")
    def set_delivery_date(self):
        generators = Generators()
        delivery_data = generators.generate_delivery_date()
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_data)

    @allure.step("Выбран срок Аренды")
    def set_rental_period(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECT)

    @allure.step("Выбран цвет самоката")
    def set_scooter_color(self):
        generators = Generators()
        scooter_color = generators.generate_scooter_color()
        self.add_text_to_element(OrderPageLocators.SCOOTER_COLOR, scooter_color)

    @allure.step("Заполнено поле 'Комментарий для курьера'")
    def set_comment(self):
        generators = Generators()
        comment = generators.generate_comment()
        self.add_text_to_element(OrderPageLocators.COMMENT, comment)

    @allure.step("Клик по кпопкам 'Заказать' и 'Да'")
    def click_order_and_confirm_buttons(self):
        self.click_to_element(OrderPageLocators.FORM_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)

    @allure.step("Клик по кнопке 'Посмотреть статус'")
    def click_see_status(self):
        self.click_to_element(OrderPageLocators.ORDER_STATUS_BUTTON)

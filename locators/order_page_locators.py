from selenium.webdriver.common.by import By


class OrderPageLocators:

    CUSTOMER_FIRST_NAME = [By.XPATH, '//input[contains(@placeholder, "* Имя")]']
    CUSTOMER_LAST_NAME = [By.XPATH, '//input[contains(@placeholder, "* Фамилия")]']
    CUSTOMER_ADDRESS = [By.XPATH, '//input[contains(@placeholder, "* Адрес: куда привезти заказ")]']
    METRO_STATION_FIELD = (By.XPATH, '//input[@class="select-search__input"]')
    DROP_DOWN_STATION_NAME = (By.XPATH, '//li[contains(@class, "select-search__row")]//button[.//div[contains(@class, '
                                        '"Order_Text") and text()="Черкизовская"]]')
    CUSTOMER_PHONE = [By.XPATH, '//input[contains(@placeholder, "* Телефон: на него позвонит курьер")]']
    NEXT_BUTTON = [By.XPATH, '//div[contains(@class, "Order_NextButton")]//button[contains(@class, "Button_Button") '
                             'and contains(@class, "Button_Middle") and text()="Далее"]']
    DELIVERY_DATE_FIELD = [By.XPATH, '//div[contains(@class, "react-datepicker__input-container")]//input[contains('
                                     '@class, "Input_Input")]']
    RENTAL_PERIOD = (By.XPATH, '//div[@class="Dropdown-arrow-wrapper"]/span[@class="Dropdown-arrow"]')
    RENTAL_PERIOD_SELECT = (By.XPATH, '//div[@class="Dropdown-option" and text()="трое суток"]')
    SCOOTER_COLOR = [By.XPATH, '//div[contains(@class, "Order_Checkboxes")]//label[contains(@class, '
                               '"Checkbox_Label")]/input[@type="checkbox"]']
    COMMENT = [By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]']
    FORM_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[contains(@class, '
                                   '"Button_Button") and not(contains(@class, "Button_Inverted")) and text('
                                   ')="Заказать"]']
    ORDER_CONFIRM_BUTTON = [By.XPATH, '//button[contains(@class, "Button_Button") and contains(@class, '
                                      '"Button_Middle") and text()="Да"]']
    ORDER_STATUS_BUTTON = [By.XPATH, '//button[contains(@class, "Button_Button") and contains (@class, '
                                     '"Button_Middle") and text()="Посмотреть статус"]']
                                     

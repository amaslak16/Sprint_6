from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']",
    )
    FAQ_QUESTION = (
        By.XPATH,
        ".//div[@id='accordion__heading-{index}']",
    )
    FAQ_ANSWER = (
        By.XPATH,
        ".//div[@id='accordion__panel-{index}']/p",
    )


class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_OPTION = (
        By.XPATH,
        ".//button[contains(@class, 'Order_SelectOption')]/div[text()='{station}']",
    )
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    DELIVERY_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_PERIOD_OPTION = (By.XPATH, ".//div[@class='Dropdown-option' and text()='{period}']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    CREATE_ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']",
    )
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")


class HeaderLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (
        By.XPATH,
        ".//*[contains(@class, 'Header_LogoYandex')]/ancestor-or-self::a[1]",
    )

from Lesson_24_pop.source_code.pages.base_page import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.CARDS_BUTTON = "//*[@href='/cards']"
        self.RED_CARD = "//*[text()='Онлайн оформление карты']/..//*[" \
                   "@alt='Красная карта 2.0']"
        self.TEL_INPUT = "//*[@type='tel']"
        self.CONFIRM_BUTTON = "//*[@type='submit']"
        self.BUTTON_MIS = "//*[@type='button']"

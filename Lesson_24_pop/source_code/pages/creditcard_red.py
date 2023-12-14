from Lesson_24_pop.source_code.pages.common_page import CommonPage


class CreditCardRed(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_phone(self):
        tel_input = self.find_element(self.TEL_INPUT)
        self.send_keys(tel_input, "299402265")

    def click_confirm(self):
        self.click(self.CONFIRM_BUTTON)

    def asser_text_ident(self, xpath, expected_text):
        actual_text = self.find_element(xpath).text
        self.assert_present_element(actual_text, expected_text)

    def color_button(self, xpath):
        self.find_element(xpath).value_of_css_property("background-color")
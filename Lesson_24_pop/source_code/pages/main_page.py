from Lesson_24_pop.source_code.pages.common_page import CommonPage


class MainPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open_site()

    def hover_cards_button(self):
        self.hover_element(self.CARDS_BUTTON)

    def click_red_card(self):
        self.click(self.RED_CARD)

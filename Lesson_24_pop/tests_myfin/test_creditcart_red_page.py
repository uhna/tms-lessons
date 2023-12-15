from Lesson_24_pop.source_code.pages.creditcard_red import CreditCardRed
from Lesson_24_pop.source_code.pages.main_page import MainPage
import allure


class TestCrediCardRed:
    def test_credit_card(self, driver):
        main_page = MainPage(driver)
        credidcard_red = CreditCardRed(driver)
        TEXT_IDENT = "//*[@class='title']"
        BUTTON_MIS = "//*[@type='button']"
        COLOR_BUTTON = "rgba(239, 49, 36, 1)"

        with allure.step("1. Открываем главную"):
            main_page.open_main_page()

        with allure.step('2. Наводимся на кнопку "Карты"'):
            main_page.hover_cards_button()

        with allure.step('3. Нажимаем кнопку "Красная карта"'):
            main_page.click_red_card()

        with allure.step('4. Переключаемся на другое окно'):
            main_page.switch_to_window(driver)

        with allure.step('5. Вводим номер телефона'):
            credidcard_red.enter_phone()

        with allure.step('6. Нажимаем на кнопку "Подтвердить"'):
            credidcard_red.click_confirm()

        with allure.step('7. Проверяем надпись "Пройдите идентификацию"'):
            credidcard_red.assert_present_element(TEXT_IDENT, "Пройдите идентификацию")

        with allure.step('8. Проверяем, что кнопка "Перейти в МСИ" появилась'):
            credidcard_red.assert_present_element(BUTTON_MIS, "Пройдите идентификацию")

        with allure.step('9. Проверяем что кнопка "Перейти в МСИ" цвета #ef3124'):
            actual_color_button = credidcard_red.color_button(BUTTON_MIS)
            credidcard_red.assert_present_element(actual_color_button, COLOR_BUTTON)





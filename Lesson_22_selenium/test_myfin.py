import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def assert_element(driver, xpath_value, clickable=False, wait_timeout=15):
    xpath = (By.XPATH, xpath_value)
    wait = WebDriverWait(driver, wait_timeout)
    wait.until(EC.presence_of_element_located(xpath))
    wait.until(EC.visibility_of_element_located(xpath))

    if clickable:
        wait.until(EC.element_to_be_clickable(xpath))
    result = driver.find_element(*xpath)
    return result


def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)
    element.click()


class TestMyfin:
    def test_myfin(self, driver):
        driver.get("https://myfin.by/")
        cards_xpath = "//*[@href='/cards']"
        red_card_xpath = "//*[text()='Онлайн оформление карты']/..//*[@alt='Красная карта 2.0']"
        input_tel_xpath = "//*[@type='tel']"
        button_confirm_xpath = "//*[@type='submit']"
        text_ident_xpath = "//*[@class='title']"
        expected_text_ident = "Пройдите идентификацию"
        button_MIS_xpath = "//*[@type='button']"
        expected_color_button = "rgba(239, 49, 36, 1)"

        cards = assert_element(driver, cards_xpath)
        action = ActionChains(driver)
        action.move_to_element(cards).perform()

        click(driver, red_card_xpath)
        driver.switch_to.window(driver.window_handles[-1])
        input_tel = assert_element(driver, input_tel_xpath)
        input_tel.send_keys("299402265")
        click(driver, button_confirm_xpath)
        time.sleep(2)

        actual_text_ident = assert_element(driver, text_ident_xpath).text
        assert actual_text_ident == expected_text_ident, f"Надпись" \
                                                          f" {expected_text_ident} не появилась"
        button_MIS = assert_element(driver, button_MIS_xpath)
        assert button_MIS is not None, "Кнопка 'Перейти в МСИ' не появилась"

        color_button = assert_element(driver, button_MIS_xpath).value_of_css_property(
            "background-color")
        assert color_button == expected_color_button, "Цвет кнопки не совпадает"
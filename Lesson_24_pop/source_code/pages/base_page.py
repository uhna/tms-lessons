from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson_24_pop.source_code.constans_url import Host


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Host.MY_FIN

    def open_site(self):
        self.driver.get(self.url)

    def find_element(self, xpath):
        driver = self.driver
        xpath_locator = (By.XPATH, xpath)
        wait = WebDriverWait(driver, 15)
        element = wait.until(EC.presence_of_element_located(xpath_locator))
        wait.until(EC.visibility_of_element_located(xpath_locator))

        return element

    def hover_element(self, xpath):
        actions = ActionChains(self.driver)
        element = self.find_element(xpath)
        actions.move_to_element(element).perform()

    def click(self, xpath):
        element = self.find_element(xpath)
        element.click()

    def clear_input(self, element):
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(Keys.HOME)

    def send_keys(self, element, text):
        self.clear_input(element)
        element.send_keys(text)

    def switch_to_window(self, driver):
        driver.switch_to.window(driver.window_handles[-1])

    def assert_url_includes(self, target_url):
        current_url = self.driver.current_url
        assert target_url in current_url, f"{target_url} не содержится в" \
                                          f" {current_url}"

    def assert_present_element(self, actual_element, expected_element):
        assert actual_element == expected_element, f"{actual_element} не " \
                                                   f"соответствует {expected_element}"

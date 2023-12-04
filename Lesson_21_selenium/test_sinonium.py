from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(driver, xpath_value, wait_timeout=10):
    xpath = (By.XPATH, xpath_value)
    wait = WebDriverWait(driver, wait_timeout)
    for condition in [
        EC.presence_of_element_located,
        EC.visibility_of_element_located,
        EC.element_to_be_clickable,
    ]:
        wait.until(condition(xpath))
    element = driver.find_element(*xpath)
    return element


class FindSynonym:
    def test_synonym_love(self, driver):
        driver.get("https://www.thesaurus.com/")
        search_field = find_element(driver, "//*[@id='global-search']")
        search_field.send_keys("love")

        search_button = find_element(driver, "//*[@class='SFL_CJwX_oOmq1DF63xo']")
        search_button.click()

        sixth_word = find_element(driver, "(//a[text()='friendship'])[1]")
        print(sixth_word.text)

        all_words = driver.find_elements(By.XPATH, "//a[@data-linkid='y2woe7']")
        array_words = [one_word.text for one_word in all_words]
        print(array_words)

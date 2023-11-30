import pytest
import datetime
# 1 - открывает в любом браузере* сайты https://www.amazon.com/, https://www.apple.com/, https://www.google.com/
# 2 - Проверяет, что на сайте заголовке окна для сайта Амазона - Amazon, для Эпла - Apple, для Гугла - Google
# 3 - тест должен быть параметризированным. Т.е. должны быть две переменные url и page_title, которые меняются
# 4 - на каждый сайт запускается новый тест
# * Можете попробовать запускать разные браузеры на разные сайты, например: для Амазона и Эпла - Firefox, для Гугла - хром
# ** В конце теста можно делать скриншот страницы. Делается это через driver. save_screenshot()
# *** (для самых отчаянных!) Попробуйте написать фикстуру драйвера так, чтобы скриншот делался при падении. Падение можно организовать через raise Exception("Something is wrong") в теле теста


class TestSelenium:
    @pytest.mark.parametrize("url", ["https://www.amazon.com/",
                                     "https://www.apple.com/",
                                     "https://www.google.com/"])
    @pytest.mark.parametrize("page_title", ["Amazon", "Apple", "Google"])
    def test_website(self, driver, url, page_title):
        driver.get(url)
        website_title = driver.title
        now_datetime = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        driver.save_screenshot(f"screenshot_{now_datetime}.png")
        assert website_title == page_title, f"Wrong title {page_title} of " \
                                            f"website {website_title}"


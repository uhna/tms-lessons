from playwright.sync_api import expect


class TestClass:
    def test_one(self, page):
        page.goto("https://blizko.by/")

        catalog_page = page.get_by_role("link", name="Каталог")
        drop_down_home = page.get_by_text("Дом", exact=True)
        house_products = page.locator("li").filter(has_text="Товары для дома")
        phone_button = page.get_by_role("link", name="Телефоны").first
        title = page.locator("//*[@id='modalSet']//*[@class='ttl']")
        address = page.locator("//*[@id='modalSet']//*[@class='descr']")
        phones_list = page.locator("//*[@id='modalSet']//a[@class='link']").element_handles()
        close_button = page.get_by_role("link", name="×")
        footer = page.locator("//*[@id='modalSet']//*[@class='pmi__footer']")

        catalog_page.click()
        drop_down_home.click()
        house_products.click()
        phone_button.click()

        expect(title).to_be_visible()
        expect(address).to_be_visible()
        for phone in phones_list:
            assert phone.is_visible()
        expect(close_button).to_be_visible()
        expect(footer).to_have_text("Пожалуйста, сообщите администратору, "
                                 "что нашли этот телефон на Blizko.by")
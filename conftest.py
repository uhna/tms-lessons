import pytest

from selenium import webdriver


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    with webdriver.Chrome(chrome_options) as driver:
        driver.maximize_window()
        yield driver


@pytest.fixture
def person():
    return "John"


@pytest.fixture
def end_of_story():
    yield
    print("\nThe end")


@pytest.fixture(scope="class", autouse=False)
def big_end_of_story():
    yield
    print("\nEnd of story")

# Fixtures for homework


@pytest.fixture
def random_age():
    age = randint(0, 100)
    return age


@pytest.fixture
def before_test(random_age):
    print(f"\nRandom age is {random_age}")
    yield


@pytest.fixture
def after_test(random_age):
    yield
    print(f"\nDeleting random age... Done")

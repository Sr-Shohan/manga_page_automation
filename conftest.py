from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="session", autouse=True)
def driver():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # Initialize the WebDriver instance using webdriver-manager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

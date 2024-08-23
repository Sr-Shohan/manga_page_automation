from pages.base_page import BasePage


class homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def load_URL(self):
        self.driver.get('https://myalice-automation-test.netlify.app/')
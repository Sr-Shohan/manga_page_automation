from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def set_value_into_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                             "Web element was not available within the specific time out. "
                                             "Locator: '" + str(locator) + "'")
        self.clear_input_field(locator)
        self.wait_for_presence_of_element(locator).send_keys(text)

    def clear_input_field(self, locator):
        self.wait_for_presence_of_element(locator)
        input_element = self.driver.find_element(*locator)
        input_element.clear()

    def click_on_element(self, locator, locator_initialization=False, time_out=10):
        if locator_initialization:
            locator = (By.XPATH, locator)
        else:
            WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                       "Web element was not available within the specific time out. "
                                                       "Locator: '" + str(locator) + "'")
            self.wait_for_element_to_be_clickable(locator).click()

    def wait_for_element_to_be_clickable(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator),
                                                          "Web element was not clickable within the specific time "
                                                          "out. Locator: '" + str(locator) + "'")

    def wait_for_presence_of_element(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                          "Web element was not present within the specific time "
                                                          "out. "
                                                          "Locator: '" + str(locator) + "'")

    def get_element_text(self, locator, time_out=1,
                         locator_initialization=False, input_tag=False):
        if locator_initialization:
            if "//" in locator:
                locator = (By.XPATH, locator)
            else:
                locator = (By.ID, locator)
        else:
            if '//' in locator[1] or By.ID == locator[0]:
                locator = locator
            else:
                locator = (By.XPATH, "//*[@data-qa='" + locator + "']")
        if input_tag:
            element_text = self.wait_for_visibility_of_element(
                locator,
                time_out).get_attribute(
                "value")
        else:
            WebDriverWait(self.driver, time_out).until(
                EC.presence_of_element_located(locator),
                "Web element was not available within the specific time out. "
                "Locator: '" + str(locator) + "'")
            element_text = self.wait_for_presence_of_element(
                locator,
                time_out).text
        return element_text

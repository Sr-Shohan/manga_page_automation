from selenium.webdriver.common.by import By


class HomepageLocators:
    user_locator = (By.XPATH, '//input[@id="username"]')
    password_locator = (By.XPATH, '//input[@id="password"]')
    btn_locator = (By.XPATH, '//button[@id="login-btn"]')
    search_locator = (By.XPATH, '//button[contains(text(),"Search")]')
    search_input_locator = (By.XPATH, '//input[@id="manga-search"]')
    manga_name_locator = (By.XPATH, '//h3[@id="manga-name"]')
    not_found_locator =(By.XPATH, '//p[contains(text(),"No manga found")]')
    details_locator = (By.XPATH, '//span[contains(text(),"Details")]')
    modal_title_locator = (By.XPATH, '//h3[following-sibling::button]')
    modal_body_locator = (By.XPATH, '//p[following-sibling::button]')
    modal_close_locator = (By.XPATH, '//button[contains(text(),"Close")]')




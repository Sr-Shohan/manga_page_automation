import json
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Home.home_page import homepage
from locator.form_locators import HomepageLocators


def test_manga_page(driver):
    home_page = homepage(driver)
    home_page.load_URL()
    project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.chdir(project_directory)
    with open('assets/login_data.json') as json_file:
        register_data = json.load(json_file)
    # [START] Verify that the login functionality works correctly.
    home_page.set_value_into_element(HomepageLocators.user_locator, register_data['registration']['username'])
    home_page.set_value_into_element(HomepageLocators.password_locator, register_data['registration']['password'])
    home_page.click_on_element(HomepageLocators.btn_locator)
    # [END] Verify that the login functionality works correctly.

    # [START] Verify that searching for manga returns the correct results.
    home_page.set_value_into_element(HomepageLocators.search_input_locator, "Naruto")
    home_page.click_on_element(HomepageLocators.search_locator)
    assert "Naruto" in home_page.get_element_text(HomepageLocators.manga_name_locator)

    home_page.set_value_into_element(HomepageLocators.search_input_locator, "One Piece")
    home_page.click_on_element(HomepageLocators.search_locator)
    assert "One Piece" in home_page.get_element_text(HomepageLocators.manga_name_locator)

    home_page.set_value_into_element(HomepageLocators.search_input_locator, "Seven Deadly Sins")
    home_page.click_on_element(HomepageLocators.search_locator)
    assert "No manga found" in home_page.get_element_text(HomepageLocators.not_found_locator)
    # [END] Verify that searching for manga returns the correct results.

    # [START] Verify that the modal displays the correct manga details.
    home_page.set_value_into_element(HomepageLocators.search_input_locator, "Attack on Titan")
    home_page.click_on_element(HomepageLocators.search_locator)
    home_page.click_on_element(HomepageLocators.details_locator)
    assert "Attack on Titan" in home_page.get_element_text(HomepageLocators.modal_title_locator)
    assert "Humanity fights for survival against" in home_page.get_element_text(HomepageLocators.modal_body_locator)
    home_page.click_on_element(HomepageLocators.modal_close_locator)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(HomepageLocators.modal_close_locator)
    )
    is_invisible = EC.invisibility_of_element_located(HomepageLocators.modal_close_locator)
    assert is_invisible(driver), "The modal button locator is still visible!"
    # [END] Verify that the modal displays the correct manga details.

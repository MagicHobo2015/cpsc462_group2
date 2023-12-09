# ******************************************************************************
#           CPSC 462 - Software Testing - Group 2                              *
#   Python Driver For Keyword Driven Testing of Odoo With Selenuim Web Driver. *
#   Author: Joshua Land, -- Group 2                                            *
#                                                                              *
#       Description: Odoo Testing using Selenium with Keyword Driven Tests.    *
#         RobotFramework Requires: a library, a resource file, and robot.      *
#  *****************************************************************************

# imports
import subprocess
from time import sleep
from selenium import webdriver
from robot.api.logger import info
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


class Odoo_Keyword_Driven_Tests:
    '''
    
    This is Group 2's Custom Keyword Library for testing Odoo.
    
    '''

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        # set it, but dont call it. because once you call it browser launches
################################################# EDIT THIS TO MATCH YOURE DRIVER
        self.user_defined_webdriver = webdriver.Firefox


    # This is Sleep all through the robot code.
    def pause_to_view(self, time_to_sleep: float) -> None:
        sleep( time_to_sleep )


    def text_to_field( self, field_name, field_value) -> None:
        field = self.webdriver.find_element(By.NAME, value=field_name)
        field.clear()
        field.send_keys(field_value)


    def text_to_id(self, id, text):
        field = self.webdriver.find_element(By.ID, id)
        field.clear()
        field.send_keys(text)


    def back(self) -> None:
        self.webdriver.back()


    # this works on patient data, I have not tested other fields yet.
    def get_field(self, field_xpath, should_be):
        field_to_check = self.webdriver.find_element(By.NAME, field_xpath)
        return  field_to_check.get_attribute('data-tooltip')


    def check_the_box(self, id):
        box = self.webdriver.find_element(By.ID, id)
        box.click()


    #   Checks the page source for the element by xpath
    def not_on_page(self, thing_to_check):
        try:
            self.webdriver.find_element(By.XPATH, '//*[contains(text(), thing_to_check)]')
            return False
        except NoSuchElementException:
            return True


    def look_for_error(self, error_to_look_for):
        if self.not_on_page(error_to_look_for):
            return False
        else:
            return True


    #   This will click action and delete so patients to be deleted should already be
    #       Selected.
    def click_action_then_delete(self):
        # get the action button.
        button = self.webdriver.find_element(By.XPATH, '//button[@data-hotkey="u"]')
        button.click()
        sleep(1)
        self.click_button("//span[contains(text(), 'Delete')]")
        # wait for confirmation popup.
        sleep(1)
        # Confirm.
        modal = self.webdriver.find_element(By.XPATH, '//button[contains(text(), "Ok")]')
        modal.send_keys(Keys.RETURN)


    def select_dropdown(self, dropdown_id, text_to_select):
        dropdown = Select(self.webdriver.find_element(By.ID, dropdown_id))
        dropdown.select_by_visible_text(text_to_select)


    def verify(self, value_one, value_two):
        assert value_one == value_two


        # shutdown Selenium
    def cleanup_shutdown(self) -> None:
        self.webdriver.close()


    # Opens the browser.
    def open_connection(self):
        self.webdriver = self.user_defined_webdriver()


    # Requires the browser open, just goes to odoo
    def goto_odoo(self):
        # open the page, then check it opened
        self.webdriver.get(self.odoo_url)
        assert "Odoo" in self.webdriver.title


    def click_button(self, xpath: str) -> None:
        button = self.webdriver.find_element(By.XPATH, value = xpath)
        button.click()

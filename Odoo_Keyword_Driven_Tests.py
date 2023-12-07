# ******************************************************************************
#           CPSC 462 - Software Testing - Group 2                              *
#   Python Driver For Keyword Driven Testing of Odoo With Selenuim Web Driver. *
#   Author: Joshua Land, -- Group 2                                            *
#                                                                              *
#       Description: Odoo Testing using Selenium with Keyword Driven Tests.    *
#         RobotFramework Requires: a library, a resource file, and robot.      *
#  *****************************************************************************

# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from robot.api.logger import info
import subprocess

from time import sleep


class Odoo_Keyword_Driven_Tests:
    '''
    
    This is Group 2's Custom Keyword Library for testing Odoo.
    
    '''

    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def __init__(self) -> None:
        self.odoo_port: int = 8069
        self.odoo_url: str = f'http://localhost:{ self.odoo_port }/web'
        self.odoo: subprocess = None
        
# ************************** YOU MAY NEED TO CHANGE THESE TO MATCH YOUR CONFIG.
        # change these as neede for your system.
        self.odoo_command = 'odoo-bin --addons-path=addons -d mydb'
        self.odoo_bin_location = '/home/magichobo/development/python/odoo/'
        
        # Turn on extra console output helpful for debugging.
        self.debug = True
        self.launch_odoo = False # turn this off to just run odoo yourself
        self.viewtime = 3.5

# ***************** END STUFF YOU MAY NEED TO CHANGE **************************

    def set_username(self, username: str) -> None:
        self.username = username
        # for development.
        if self.debug:
            print(f'Username has now been set as { self.password }')


    def set_password(self, password: str) -> None:
        self.password = password
        
        # for development.
        if self.debug:
            print(f'Password has now been set as { self.password }')

    # only so many names for it.
    def pause_to_view(self, time_to_sleep: float) -> None:
        if self.debug:
            print(f'Stopping the system for: { time_to_sleep }')
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

    def select_dropdown(self, dropdown_id, text_to_select):
        dropdown = Select(self.webdriver.find_element(By.ID, dropdown_id))
        dropdown.select_by_visible_text(text_to_select)

    def verify(self, value_one, value_two):
        assert value_one == value_two

    # TODO: MAKE THIS WORK ********************************************
    def start_odoo(self):
        if self.launch_odoo:
            if self.debug:
                print(f'Starting Up odoo..')
                print(f'Using the command: \n { self.odoo_bin_location + self.odoo_command }')

                # spawn odoo.
                self.odoo = subprocess.Popen(args=[self.odoo_bin_location, self.odoo_command], shell=True )



    # all shutdown procs go here.
    def cleanup_shutdown(self) -> None:
        if self.debug:
            print(f'Cleaning Up Odoo..')
            print(f'Shutting Down webDriver.')
        # kill the subprocess if this is managing odoo for you.
        if self.launch_odoo:
            self.odoo.kill()

        # shutdown Selenium
        self.webdriver.close()
    
    def open_connection(self):
        if self.debug:
            print(f'Using WebDriver to open Connection.')
        # Choose your Driver Here.
        self.webdriver = webdriver.Firefox() # webdriver.Chorme()
    
    def goto_odoo(self):
        self.webdriver.get(self.odoo_url)
                # make sure that worked.
        assert "Odoo" in self.webdriver.title

    def click_button(self, xpath: str) -> None:
        button = self.webdriver.find_element(By.XPATH, value = xpath)
        button.click()
    

# This is scratch down here for debuging, not ment to be run by others so may or maynot even work. 
def main():
    # create our test object.
    odoo_object = Odoo_Keyword_Driven_Tests()
    
    # work in progress, allow this script to manage odoo.
    odoo_object.start_odoo()
    
    odoo_object.login_odoo()
    sleep( odoo_object.viewtime )
    
    odoo_object.cleanup_shutdown()


# some driver code for self/unit testing.
if __name__ == "__main__":
    main()

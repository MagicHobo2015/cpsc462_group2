# ******************************************************************************
#           CPSC 462 - Software Testing - Group 2                              *
#   Python Driver For Keyword Driven Testing of Odoo With Selenuim Web Driver. *
#   Author: Joshua Land, -- Group 2                                            *
#                                                                              *
#       Description: Odoo Testing using Selenium with Keyword Driven Tests.    *
#                                                                              *
#  *****************************************************************************

# imports
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.google.com")

sleep(5.0)

driver.close()
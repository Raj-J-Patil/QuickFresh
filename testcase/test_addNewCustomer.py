from selenium import webdriver
from pageobjects.addNewCustomer_page import AddNewCustomer

def test_addNewCustomer(setup):
    driver = setup
    ad = AddNewCustomer(driver)
    ad.logIn()
import pytest
from pageobjects.loginPage_page import login
from selenium import webdriver
from testcase.conftest import setup
from utilities.readProperty import ReadConfig
from utilities.customlogger import LogGen


application_id = ReadConfig.get_id()
password = ReadConfig.get_password()
link = ReadConfig.get_url()
logger = LogGen.loggen()

def test_login_page(setup):
    logger.info("******************** 1st test case start ********************")
    logger.info("******************** Verifying Home page title  ********************")
    driver = setup
    driver.get(link)
    title = driver.title
    if title == "Your store. Login":
        assert True
        logger.info("******************** Home page title Test Case Passed ********************")

    else:
        driver.save_screenshot("C:\\Users\\shivr\\PycharmProjects\\QuickFresh\\screenshots\\test_loginpage.png")
        logger.info("******************** Home page title Test Case Failed ********************")
        assert False


def test_login(setup):
    logger.info("******************** Verifying Admin can Log in to application  ********************")
    driver = setup
    driver.get(link)
    lp = login(driver)
    lp.setusername(application_id)
    lp.setpassword(password)
    lp.clickloginbutton()
    title = lp.loninpagetile()
    if title == "Dashboard / nopCommerce administration":
        assert True
        logger.info("******************** Log in Test Case Passed ********************")
    else:
        driver.save_screenshot("C:\\Users\\shivr\\PycharmProjects\\QuickFresh\\screenshots\\test_login.png")
        logger.info("******************** Log in Test Case Failed ********************")
        logger.info("******************** 1st test case end ********************")
        assert False
    lp.logout()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("/configuration\\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")


button_loin_xpath = "//button[text()='Log in']"
link_logout_linktext = "Logout"

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,button_loin_xpath).click()
title=driver.title
if title == "Dashboard / nopCommerce administration":
    print("pass")
else:
    driver.save_screenshot("C:\\Users\\shivr\\PycharmProjects\\QuickFresh\\screenshots\\test_login.png")
    print("failed")
driver.find_element(By.LINK_TEXT,link_logout_linktext).click()
driver.quit()
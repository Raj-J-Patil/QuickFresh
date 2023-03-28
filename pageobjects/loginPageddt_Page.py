from selenium.webdriver.common.by import By

class LoginPage:
    driver = None

    def __init__(self,driver):
        self.driver = driver

    textbox_email_id = "Email"
    textbox_password_id= "Password"
    button_login_xpath="//button[text()='Log in']"
    button_logout_xpath = "//a[text()='Logout']"

    def setUserEmail(self, email):
        textbox_email = self.driver.find_element(By.ID, self.textbox_email_id)
        textbox_email.clear()
        textbox_email.send_keys(email)

    def setUserPassword(self, password):
        textbox_password = self.driver.find_element(By.ID, self.textbox_password_id)
        textbox_password.clear()
        textbox_password.send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def getTitle(self):
        page_title = self.driver.title
        return page_title


    def logOut(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

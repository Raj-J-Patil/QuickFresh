from selenium.webdriver.common.by import By

class LoginPage:
    driver = None

    def __init__(self,driver):
        self.driver = driver

    textbox_email_id = "Email"
    textbox_password_id= "Password"
    button_login_xpath="//button[text()='Log in']"
    link_logout_linktext = "a"
    message_unsuccesfullogin_xpath = "//div[contains(text(),'Login was unsuccessful')]"

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
        if(page_title=='Dashboard / nopCommerce administration'):
            flag ='pass'
            return flag
        else:
            flag = 'fail'
            return flag


    def logOut(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def unsucessloginMessage(self):
        message = self.driver.find_element(By.XPATH, self.message_unsuccesfullogin_xpath).text
        if(message =='''Login was unsuccessful. Please correct the errors and try again.
The credentials provided are incorrect'''):
            flag = "fail"
            return flag
        else:
            flag = "pass"
            return flag

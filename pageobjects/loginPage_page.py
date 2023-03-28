from selenium import webdriver
class login():

    def __init__(self,driver):
        self.driver = driver

    textbox_email_id = "Email"
    textbox_pass_id = "Password"
    button_loin_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    def setusername(self,id):
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID,self.textbox_email_id).send_keys(id)

    def setpassword(self,password):
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.ID, self.textbox_pass_id).clear()
        self.driver.find_element(By.ID, self.textbox_pass_id).send_keys(password)

    def clickloginbutton(self):
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.XPATH, self.button_loin_xpath).click()

    def loninpagetile(self):
        title= self.driver.title
        return title

    def logout(self):
        from selenium.webdriver.common.by import By
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
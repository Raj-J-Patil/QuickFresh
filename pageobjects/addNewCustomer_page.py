from selenium.webdriver.common.by import By


class AddNewCustomer:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    textBox_Email_id = "Email"
    textBox_Password_id = "Password"
    button_Login_xpath = "//button[text()='Log in']"

    def logIn(self):
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.find_element(By.ID, self.textBox_Email_id).clear()
        self.driver.find_element(By.ID, self.textBox_Email_id).send_keys("admin@yourstore.com")
        self.driver.find_element(By.ID, self.textBox_Password_id).clear()
        self.driver.find_element(By.ID, self.textBox_Password_id).send_keys("admin")
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

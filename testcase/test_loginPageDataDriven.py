from pageobjects.loginPageDataDriven_Page import LoginPage
from utilities.readProperty import ReadConfig
from utilities.excelUtils import Excel

baseUrl = ReadConfig.get_url()
path = "C:\\Users\\shivr\\PycharmProjects\\QuickFresh\\testdata\\login.xlsx"
sheetName = "data"

def test_loginPage(setup, self=None):
    driver = setup
    driver.get(baseUrl)
    lp= LoginPage(driver)
    # Excel.get_cell_value(self,path,sheetName,2,1)
    userEmail = Excel.get_cell_value(self,path, sheetName, 2, 1)
    userPassword = Excel.get_cell_value(self,path, sheetName,2, 2)
    lp.setUserEmail(userEmail)
    lp.setUserPassword(userPassword)
    lp.clickLoginButton()
    try:
        flag = lp.unsucessloginMessage()
        expected_result= Excel.get_cell_value(self,path, sheetName,2, 3)
        if(expected_result==flag):
            assert True
        else:
            assert False
    except Exception as e:
        flag = lp.getTitle()
        expected_result = Excel.get_cell_value(self,path, sheetName,2, 3)
        if (expected_result == flag):
            assert True
            lp.logOut()
        else:
            assert False


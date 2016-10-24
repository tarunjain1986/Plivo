
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class LoginPage(object):
    
    '''
    classdocs
    @author: Tarun Jain
    Provides element of the login page and the associated methods.
    '''

    def __init__(self):
        logger.info("Initializing Login Page's Element")
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        self.emailAddress = self.driver.find_element_by_css_selector("#id_username")
        self.passwordField = self.driver.find_element_by_css_selector("#id_password")
        self.loginButton = self.driver.find_element_by_css_selector('#login-sub')
        
    def userLogin(self, UserID, LoginPwd):
        self.enterLoginEmail(UserID)
        self.enterLoginPassword(LoginPwd)
        self.clickLoginButton()
        BuiltIn().import_library(self.home_path+"/PageObjects/DashboardPage.py")
        
    def enterLoginEmail(self, UserID):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.emailAddress))
        self.emailAddress.send_keys(str(UserID))
        logger.info("Email at Login page entered!")
        
    def enterLoginPassword(self,LoginPwd): 
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.passwordField))
        self.passwordField.send_keys(str(LoginPwd))
        logger.info("Password at Login page entered!")
        
    def clickLoginButton(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.loginButton))
        self.loginButton.click()
        logger.info("Login Button at Login page clicked!")
        
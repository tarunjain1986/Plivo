
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from robot.utils.asserts import assert_false


class DashboardPage(object):
    
    '''
    classdocs
    @author: Tarun Jain
    Provides element of the Dashboard page and the associated methods.
    '''

    def __init__(self):
        logger.info("Initializing Dashboard Page's Element")
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        self.loginNav = self.driver.find_element_by_css_selector(".loginnav")
    
    
    def verifyLoggedinUser(self, UserID):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.loginNav))
        if (self.loginNav.find_elements_by_tag_name("li")[0].text == "("+UserID+")"):
            logger.info("User %s logged in successfully!" % (str(UserID)))
        else:
            assert_false(True,"User login failed!")
            
    def clickDashboardNavigation(self, DashNavItem):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.loginNav))
        self.anchorList = self.loginNav.find_elements_by_tag_name("a")
        for anchor in self.anchorList:
            if(DashNavItem.lower() in anchor.get_attribute("href")):
                logger.info("Clicked on %s" % (str(DashNavItem)))
                anchor.click()
                logger.info("Opening Page: " + self.home_path+"/PageObjects/"+str(DashNavItem)+"Page.py")
                BuiltIn().import_library(self.home_path+"/PageObjects/"+str(DashNavItem)+"Page.py")
                break
            
        
            
            
            
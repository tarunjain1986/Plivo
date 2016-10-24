from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from robot.utils.asserts import assert_false


class AccountPage(object):
    
    '''
    classdocs
    Created on Oct 23, 2016
    @author: tarun
    Provides element of the Account page and the associated methods.
    '''
    
    def __init__(self):
        logger.info("Initializing Account Page's Element")
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        self.dashNav = self.driver.find_element_by_css_selector("#dashnav >ul")
        
    def clickAccountNavigation(self, AccountNavItem):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.dashNav))
        self.anchorList = self.dashNav.find_elements_by_tag_name("a")
        for anchor in self.anchorList:
            if(AccountNavItem.lower() in anchor.get_attribute("href")):
                logger.info("Clicked on %s" % (str(AccountNavItem)))
                anchor.click()
                logger.info("Opening Page: " + self.home_path+"/PageObjects/"+str(AccountNavItem)+"Page.py")
                BuiltIn().import_library(self.home_path+"/PageObjects/"+str(AccountNavItem)+"Page.py")
                break
        
'''
Created on 22-Oct-2016

@author: tarunjain
'''


from robot.utils.asserts import assert_true
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.events import AbstractEventListener
from robot.api import logger
from time import gmtime, strftime


class ScreenshotListener(AbstractEventListener):
    
    def __init__(self):
        logger.info("Screenshot Class Initializing")

    def on_exception(self, exception, driver):
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        screenshot_name = BuiltIn().get_variable_value("${TEST NAME}") + strftime("%Y-%m-%d%H:%M:%S", gmtime()) +".png"
        self.driver.get_screenshot_as_file(self.home_path + "/ScreenShots/" +screenshot_name)
        logger.info("Screenshot saved as '%s'" % screenshot_name)



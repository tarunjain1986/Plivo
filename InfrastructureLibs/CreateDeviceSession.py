
from appium import webdriver
from robot.libraries.BuiltIn import BuiltIn
import copy
from os.path import os
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from robot.api import logger
from time import gmtime, strftime


class CreateDeviceSession:
    '''
    classdocs
    Created on 22-Oct-2016
    Creates instance of driver depending upon the input provided.
    @author: tarunjain
    '''    
    def openBrowser(self,device):
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.reference = BuiltIn().get_variable_value("${references}")
        self.Browser = BuiltIn().get_variable_value("${globalTestBed}")["DesktopBrowser"]["BROWSER"]
        self.device = copy.deepcopy(self.reference)[device]
        self.desired_caps = {}
        logger.info("About to launch Browser")
        if(self.Browser == "Firefox"):
            self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,command_executor='http://'+self.device["SELENIUMSERVERIP"]+':4444/wd/hub')
        elif(self.Browser == "Chrome"):
            self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME,command_executor='http://'+self.device["SELENIUMSERVERIP"]+':4444/wd/hub')
        else:
            self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.SAFARI,command_executor='http://'+self.device["SELENIUMSERVERIP"]+':4444/wd/hub')
        logger.info("After launch Browser")
        self.driver.implicitly_wait(10)
        self.cur_session= {}
        self.cur_session["session"] = self.driver
        self.cur_session["properties"]= self.device
        self.cur_session["guest"] = 1
        self.driver = EventFiringWebDriver(self.driver, ScreenshotListener())
        logger.info("Opening Url:" + self.device["URL"])
        self.driver.get(self.device["URL"])
        BuiltIn().set_global_variable("${cur_session}",self.cur_session)
        BuiltIn().import_library(self.home_path+"/PageObjects/LoginPage.py")
        
        
    def closeSession(self):
        self.driver.quit() 
        
class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        screenshot_name = BuiltIn().get_variable_value("${TEST NAME}") + strftime("%Y-%m-%d%H:%M:%S", gmtime()) +".png"
        self.driver.get_screenshot_as_file(self.home_path + "/ScreenShots/" +screenshot_name)
        logger.info("Screenshot saved as '%s'" % screenshot_name)
        
    
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from robot.utils.asserts import assert_false
import time


class PaymentsPage(object):
    
    '''
    classdocs
    Created on Oct 23, 2016
    @author: tarun
    Provides element of the Payments page and the associated methods.
    '''
    errorText = "This coupon code is invalid."
    successText = "Coupon has been applied successfully. Your credits have been updated."
    
    def __init__(self):
        logger.info("Initializing Login Page's Element")
        self.home_path = BuiltIn().get_variable_value("${globalTestBed}")["AutomationServer"]["HOME_PATH"]
        self.driver = BuiltIn().get_variable_value("${cur_session}")["session"]
        self.inPaymentNav = self.driver.find_element_by_css_selector(".in-nav")
        self.cardInfo = self.driver.find_element_by_css_selector(".card-info")
        
    def clickReedeemCoupon(self, CouponCode, CouponType):
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.inPaymentNav))
        self.headerList = self.cardInfo.find_elements_by_tag_name("h4")
        try:
            self.headerList[0].find_element_by_tag_name("a").click()
            WebDriverWait(self.driver,20).until(EC.visibility_of(self.driver.find_element_by_css_selector("#coupon")))
            couponText = self.driver.find_element_by_css_selector("#coupon")
            couponText.send_keys(CouponCode)
            self.driver.find_element_by_css_selector("#modfooter >.btn").click()
            self.verifyPostCouponApplyMessage(CouponType)
        except Exception, e:
            logger.error("Reedeem Coupon option not available!!" + str(e))
            
    def verifyPostCouponApplyMessage(self, CouponType):
        if (str(CouponType) == "Incorrect"):
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element_by_css_selector("#modbody .alert.alert-error")))
                errorMessage = self.driver.find_element_by_css_selector("#modbody .alert.alert-error").text
                if (errorMessage == self.errorText):
                    logger.info("Invalid coupon message available! " + errorMessage)
                else:
                    assert_false(True, "Invalid coupon message not available!")
            except Exception, e:
                logger.info("Inside Incorrect Coupon If " + str(e))
        else :
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element_by_css_selector("#modbody .alert.alert-success")))
                successMessage = self.driver.find_element_by_css_selector("#modbody .alert.alert-success").text
                if (successMessage == self.successText):
                    logger.info("Correct coupon message available! " + successMessage)
                else:
                    assert_false(True, "Valid coupon message not available!")
            except:
                logger.info("Inside Correct Coupon If " + str(e))
                
        
import sys
import os
import time
from pathlib import Path

#from alphabin.common_functionality import WebDriver

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
path_c = str(Path(os.getcwd()).parent.parent)
#sys.path.append(os.path.join(str(path_c), "alphabin"))
sys.path.append(os.path.join(str(path_c), "alphabin\\map"))
sys.path.append(str(path_c+'\\alphabin'))
sys.path.append(str(path_c)+"alphabin\\common_utilities\\common_functionality.py")
from common_functionality import *
from map import Signup as map
from log import log_files

logger = log_files("Signup")


class Signup(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, driver):
        self.driver = driver
        self.email = None
        self.password = None

    def click_signup_for_free(self):
        try:
            sign_up = self.driver.get_element_by_xpath(map.signup_btn)
            sign_up.click()
            logger.info('sign_up clicked')
            #get_started = self.driver.get_element_by_xpath(map.free_account_btn)
            self.driver.scroll_by_pixel()
            logger.info("page scrolled")
        except Exception as ex:
            logger.error('click_signup_for_free failed')
            self.driver.capture_screenshot("click_signup")
            raise Exception(ex)

    def click_free_account(self):
        try:
            free_account = self.driver.get_element_by_xpath(map.free_account_btn)
            free_account.click()
            logger.info("click_free_account")
        except Exception as ex:
            logger.error('click_free_account failed')
            self.driver.capture_screenshot("click_free_account")
            raise Exception(ex)

    def fill_details(self, email, password):
        try:
            self.email = email
            self.password = password
            email_field = self.driver.get_element_by_id(map.email)
            email_field.clear()
            email_field.send_keys(email)
            logger.info(f'entered email: {email}')
            password_field = self.driver.get_element_by_id(map.password)
            password_field.send_keys(password)
            logger.info(f'entered password: {password}')
        except Exception as ex:
            logger.error('fill_details failed')
            self.driver.capture_screenshot("fill_details")
            raise Exception(ex)

    def click_continue(self):
        try:
            register = self.driver.get_element_by_id(map.register)
            register.click()
            logger.info('register clicked')
            time.sleep(20)
            print("hello")
        except Exception as ex:
            logger.error('click_continue failed')
            self.driver.capture_screenshot("click_continue")
            raise Exception(ex)

    def verify_signup(self):
        try:
            assert "Home - Evernote" == self.driver.get_page_title("Home - Evernote"), "registration verification failed"
            #time.sleep(30)
        except Exception as ex:
            logger.error('verify_signup failed')
            self.driver.capture_screenshot("verify_signup")
            raise Exception(ex)


#s = Signup()
#s.fill_details()
#print(str(Path(os.getcwd()).parent.parent))
#print(str(Path(os.getcwd()).parent.parent))
#print(str(Path(os.getcwd())))

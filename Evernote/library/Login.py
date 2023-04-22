import time

from map import Login as map
from log import log_files

logger = log_files("Login")


class Login:
    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        try:
            link = self.driver.get_element_by_xpath(map.login_link)
            link.click()
        except Exception as ex:
            logger.error("click_login_link failed")
            self.driver.capture_screenshot("click_login_link")
            raise Exception(ex)

    def enter_email(self, email):
        try:
            username = self.driver.get_element_by_id(map.email_id)
            username.clear()
            username.send_keys(email)
            logger.info(f"{email} entered")
        except Exception as ex:
            logger.error("enter_email failed")
            self.driver.capture_screenshot("enter_email")
            raise Exception(ex)

    def enter_password(self, password):
        try:
            password_field = self.driver.get_element_by_id(map.password_id)
            password_field.clear()
            password_field.send_keys(password)
            logger.info(f"{password} entered")
        except Exception as ex:
            logger.error("enter_password failed")
            self.driver.capture_screenshot("enter_password")
            raise Exception(ex)

    def click_continue(self):
        try:
            continue_btn = self.driver.get_element_by_id(map.continue_btn)
            continue_btn.click()
            logger.info("clicked_continue")
        except Exception as ex:
            logger.error("click_continue failed")
            self.driver.capture_screenshot("click_continue")
            raise Exception(ex)

    def click_signin(self):
        try:
            signin_btn = self.driver.get_element_by_id(map.continue_btn)
            signin_btn.click()
            logger.info("clicked_signin")
        except Exception as ex:
            logger.error("click_signin failed")
            self.driver.capture_screenshot("click_signin")
            raise Exception(ex)


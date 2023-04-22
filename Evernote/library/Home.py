import time

from map import Home as map
from log import log_files

logger = log_files("Home")


class Home:

    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        try:
            close = self.driver.get_element_by_id(map.close_popup)
            close.click()
            logger.info("closed_popup")
        except Exception as ex:
            logger.error("close_popup failed")
            self.driver.capture_screenshot("close_popup")
            raise Exception(ex)

    def verify_welcome_note(self):
        try:
            self.driver.get_element_by_presence(map.welcome_note)
            logger.error("welcome_note")
            return True
        except Exception as ex:
            return False
            logger.error("verify_welcome_note failed")
            self.driver.capture_screenshot("verify_welcome_note")
            raise Exception(ex)

    def click_get_started(self):
        try:
            get_started = self.driver.get_element_by_id(map.get_started)
            get_started.click()
            logger.info("clicked_get_started")
            return True
        except Exception as ex:
            return False
            #logger.error("click_get_started failed")
            #self.driver.capture_screenshot("click_get_started")
            #raise Exception(ex)

    def select_web_browser(self):
        try:
            web_browser = self.driver.get_element_by_presence(map.web_browser)
            get_started.click()
            logger.info("clicked_get_started")
            return True
        except Exception as ex:
            return False
    def choose_category(self):
        try:
            choose = self.driver.get_element_by_xpath(map.work)
            choose.click()
            logger.info("work clicked")
            self.click_next()
            meeting_template = self.driver.get_element_by_xpath(map.meeting_template)
            meeting_template.click()
            self.click_next()
            #time.sleep(30)
        except Exception as ex:
            logger.error("choose_category failed")
            self.driver.capture_screenshot("choose_category")
            raise Exception(ex)

    def click_next(self):
        try:
            next_btn = self.driver.get_element_by_xpath(map.next_btn)
            next_btn.click()
            logger.info("clicked_next")
        except Exception as ex:
            logger.error("click_next failed")
            self.driver.capture_screenshot("click_next")
            raise Exception(ex)

    def make_setup(self):
        try:
            self.close_popup()
            if self.click_get_started():
                pass
            #else:
            #time.sleep(5)
            #self.click_get_started()
            self.choose_category()
            self.close_setup()
            self.driver.get_element_by_xpath(map.close_btn).click()
            logger.info("popup closed")
        except Exception as ex:
            logger.error("make_setup failed")
            self.driver.capture_screenshot("make_setup")
            raise Exception(ex)

    def close_setup(self):
        try:
            close_btn = self.driver.get_element_by_id(map.close_setup)
            close_btn.click()
        except Exception as ex:
            logger.error("close_setup failed")
            self.driver.capture_screenshot("close_setup")
            raise Exception(ex)

    def verify_logged_user(self, username):
        try:
            logged_user = self.driver.get_element_by_presence(map.logged_in_user_text)
            logger.info(f"{logged_user.text} verified")
            assert username == logged_user.text
        except Exception as ex:
            logger.error("verify_logged_user failed")
            self.driver.capture_screenshot("verify_logged_user")
            raise Exception(ex)

    def sign_out(self):
        try:
            time.sleep(5)
            logged_user = self.driver.get_element_by_xpath("//div[@class='WgMHzCr34NNz6J10aqEP']") #qa-NAV_USER RIuSBaDpAUnBl7LN_Kjf  qa-USER_PORTRAIT
            logged_user.click()
            #self.driver.execute_script("arguments[0].click();", logged_user)
            logger.info("user clicked")
            sign_out = self.driver.get_element_by_xpath(map.sign_out)
            sign_out.click()
            logger.info("sign_out")
            assert "You have logged out of Evernote. | Evernote" == self.driver.get_page_title(
                "You have logged out of Evernote. | Evernote"), "signout failed"
        except Exception as ex:
            logger.error("sign_out failed")
            self.driver.capture_screenshot("sign_out")
            raise Exception(ex)


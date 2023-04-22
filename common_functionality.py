import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("https://evernote.com/")
        self.driver.maximize_window()

    def get_element_by_id(self, id_, timeout=40):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.ID, id_))
        )
        return element

    def get_element_by_xpath(self, xpath, timeout=30):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element

    def get_element_by_presence(self, xpath, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def scroll_by_pixel(self):
        scroll = self.driver.execute_script("window.scrollBy(0, 500)", "")
        return scroll

    def get_page_title(self, title, timeout=30):
        """
        return title of page focused
        :return:
        """
        WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        return self.driver.title

    def capture_screenshot(self, filename):
        directory = str(Path(os.getcwd()).parent) + "/Screenshots"
        print(directory)
        self.driver.save_screenshot("%s/%s" % (directory, filename + ".png"))

#w = WebDriver()
#w.capture_screenshot("vinray")



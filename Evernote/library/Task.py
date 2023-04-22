import os
import time
from pathlib import Path

from map import Task as map
from log import log_files
from selenium.webdriver import ActionChains

logger = log_files("Task")

class Task:
    def __init__(self, driver):
        self.driver = driver
        self.task_name = None

    def click_notes_tab(self):
        try:
            notes_tab = self.driver.get_element_by_xpath(map.notes_tab)
            notes_tab.click()
            logger.info("notes_tab clicked")
            #task_in_notes = self.driver.get_element_by_xpath(map.para)
            logger.info("open")
            #task_in_notes.click()
            logger.info("task_in_notes clicked")
        except Exception as ex:
            logger.error("click_notes_tab failed")
            self.driver.capture_screenshot("click_notes_tab")
            raise Exception(ex)

    def click_task(self):
        try:
            time.sleep(50)
            task = self.driver.get_element_by_id(map.task)
            task.click()
            logger.info("task clicked")
        except Exception as ex:
            logger.error("click_task failed")
            self.driver.capture_screenshot("click_task")
            raise Exception(ex)

    def create_task(self, task_name):
        try:
            self.task_name = task_name
            create_task = self.driver.get_element_by_id(map.new_task_btn)
            create_task.click()
            logger.info("new_task clicked")
            task = self.driver.get_element_by_id(map.task_name_id)
            task.send_keys(task_name)
            create_btn = self.driver.get_element_by_id(map.create_task_btn)
            create_btn.click()
            logger.info("create_task clicked")
        except Exception as ex:
            logger.error("create_task failed")
            self.driver.capture_screenshot("create_task")
            raise Exception(ex)

    def open_created_task(self):
        try:
            time.sleep(5)
            open_task = self.driver.get_element_by_xpath(map.created_task % self.task_name)
            open_task.click()
            logger.info("created_task clicked")
        except Exception as ex:
            logger.error("open_created_task failed")
            self.driver.capture_screenshot("open_created_task")
            raise Exception(ex)

    def open_notes(self):
        try:
            time.sleep(5)
            things_to_do = self.driver.get_element_by_id(map.things_to_do)
            things_to_do.click()
            logger.info("things_to_do clicked")
            go_to_note = self.driver.get_element_by_id(map.go_to_note)
            go_to_note.click()
            logger.info("go_to_note clicked")
        except Exception as ex:
            logger.error("open_notes failed")
            self.driver.capture_screenshot("open_notes")
            raise Exception(ex)

    def open_insert(self):
        try:
            insert = self.driver.get_element_by_id(map.insert)
            insert.click()
            logger.info("insert clicked")
        except Exception as ex:
            logger.error("insert failed")
            self.driver.capture_screenshot("insert")
            raise Exception(ex)

    def add_table(self):
        try:
            table = self.driver.get_element_by_id(map.table)
            table.click()
            logger.info("table clicked")
            hover_add_row = self.driver.get_element_by_id(map.hover_add_row)
            actions = ActionChains(self.driver)
            actions.double_click(hover_add_row).perform().click()
            logger.info("ook")
            time.sleep(10)
        except Exception as ex:
            logger.error("attachment failed")
            self.driver.capture_screenshot("attachment")
            raise Exception(ex)

    def add_image(self):
        try:
            attachment = self.driver.get_element_by_id(map.image)
            #attachment.click()
            dir = Path(os.getcwd())
            logger.info(dir)
            path = str(dir) + "\Screenshot (108).png"
            attachment.send_keys(path)
            logger.info("attachment clicked")
        except Exception as ex:
            logger.error("attachment failed")
            self.driver.capture_screenshot("attachment")
            raise Exception(ex)

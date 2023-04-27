import os
import time
from pathlib import Path

from map import Task as map
from log import log_files
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
logger = log_files("Task")

class Task:
    def __init__(self, driver):
        self.driver = driver
        self.task_name = None

    def click_task(self):
        try:
            #time.sleep(50)
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

    def click_notes_tab(self):
        try:
            time.sleep(5)
            notes_tab = self.driver.get_element_by_xpath(map.notes_tab)
            notes_tab.click()
            logger.info("notes_tab clicked")
            self.driver.switch_frame(map.editor_frame)
            self.driver.get_element_by_visible(map.en_note).click()
            logger.info("editor clicked")
            self.driver.switch_out_frame()
        except Exception as ex:
            logger.error("click_notes_tab failed")
            self.driver.capture_screenshot("click_notes_tab")
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

    def add_data(self, dummy_text):
        try:
            data_table = self.driver.get_element_by_tag('tbody')
            data_table_rows = data_table.find_elements(By.TAG_NAME, 'tr')
            logger.info(f"{len(data_table_rows)} rows found ")
            cells = self.driver.get_elements_by_xpath("//tbody/tr/td")
            logger.info(f"{len(cells)} cells found ")
            logger.info(f"{len(data_table_rows)}X{(len(cells)//len(data_table_rows))} table")
            for i in range(1, len(data_table_rows)+1):
                for j in range(1, (len(cells)//len(data_table_rows))+1):
                    cell = self.driver.get_element_by_xpath(f"//tbody/tr[{i}]/td[{j}]")
                    logger.info(f"//tbody/tr[{i}]/td[{j}]")
                    cell.click()
                    cell.send_keys(Keys.CONTROL + 'b')
                    cell.send_keys(dummy_text)
                    logger.info(f"text entered")
            #for row_no, web_element in enumerate(data_table_rows):
                #logger.info(f"{row_no+1}th row")
                #for column_no, column in enumerate(web_element.find_elements(By.TAG_NAME, 'td')):
                    #logger.info(f"{column_no+1} column")
                   # column.send_keys("vinay")
        except Exception as ex:
            logger.error("add_data failed")
            self.driver.capture_screenshot("add_data")
            raise Exception(ex)

    def add_table(self, dummy_text):
        try:
            table = self.driver.get_element_by_id(map.table)
            table.click()
            logger.info("table clicked")
            self.driver.switch_frame(map.editor_frame)
            logger.info(f" frame {map.editor_frame} switched")
            table = self.driver.get_element_by_tag(map.select_table)
            table.click()
            logger.info("table selected")
            #select_side_table = self.driver.get_elements_by_visible(map.side_table_select)
            select_side_table = self.driver.get_element_by_visible("//ui-table/div[@draggable='true']")
            select_side_table.click()
            logger.info("selected")
            hover_add_row = self.driver.get_element_by_presence(map.hover_add_row)
            hover_add_row.click()
            self.driver.get_element_by_visible(map.en_note).click()
            logger.info("editor clicked")
            time.sleep(10)
            table = self.driver.get_element_by_tag(map.select_table)
            table.click()
            logger.info("table selected")
            # select_side_table = self.driver.get_elements_by_visible(map.side_table_select)
            select_side_table = self.driver.get_element_by_visible("//ui-table/div[@draggable='true']")
            select_side_table.click()
            logger.info("selected")
            hover_add_row = self.driver.get_element_by_presence(map.hover_add_row)
            hover_add_row.click()
            logger.info("rows added")
            self.add_data(dummy_text)
            time.sleep(10)
        except Exception as ex:
            logger.error("add_table failed")
            self.driver.capture_screenshot("add_table")
            raise Exception(ex)


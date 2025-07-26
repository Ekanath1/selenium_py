import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests
import openpyxl
import xlsxwriter
import os
from openpyxl import Workbook


class Table:
    service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    url = "https://testautomationpractice.blogspot.com/"

    def web_table(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.maximize_window()
        no_of_rows = len(self.driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))

        no_of_cols = len(self.driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

        col_data = self.driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
        print(col_data)

        print("printing no of rows and cols data")
        data_list = []
        for r in range(2, no_of_rows + 1):
            d = []
            for c in range(1, no_of_cols + 1):
                data = self.driver.find_element(By.XPATH,
                    "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                d.append(data)
            data_list.append(d)

        with open("Employees.txt", "w") as file:

            for data in data_list:
                file.writelines(data)
                file.write("\n")

        print("Data is written into the file.")

    def web_table_data(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.maximize_window()
        no_of_rows = len(self.driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr"))

        no_of_cols = len(self.driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr/th"))

        print(no_of_rows)
        print(no_of_cols)
        data_list = []
        for i in range(1, no_of_rows):
            web_data = []
            for j in range(1, no_of_cols):
                data = self.driver.find_element(By.XPATH,
                        "//table[@id='taskTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
                web_data.append(data)
            data_list.append(web_data)
        print(data_list)

        file_path = "C:\\Users\\AKASH\\PycharmProjects\\sel\\Data\\Book1.xlsx"
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()

        # Write data row by row
        for row_num, row_data in enumerate(data_list):
            worksheet.write_row(row_num, 0, row_data)

        # Close the workbook after writing
        workbook.close()

    def page_data(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        rows = len(self.driver.find_elements(By.XPATH, "//table[@id='productTable']//tr"))

        cols = len(self.driver.find_elements(By.XPATH, "//table[@id='productTable']//tr/th"))
        print(rows, cols)
        i = 1

        while True:
            if i == 3:
                self.driver.find_element(By.XPATH, "//a[normalize-space()='3']").click()

                for r in range(1, rows):
                    page_data = []
                    for c in range(1, cols):
                        data = self.driver.find_element(By.XPATH,
                                "//table[@id='productTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                        page_data.append(data)

                    print(page_data)
                break

            i += 1

    def choose_file(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        db_click = self.driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
        act = ActionChains(self.driver)
        act.double_click(db_click).perform()
        time.sleep(5)

    def broken_links(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        links = self.driver.find_elements(By.CLASS_NAME,"link")
        for link in links:
            r = requests.head(link.get_attribute('href'))
            if r.status_code > 400:
                print(link.get_attribute('href'), r.status_code)
            else:
                print(str(link) + " isn't available.", r.status_code)

    def scrolling_dropdown(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        items = self.driver.find_elements(By.XPATH, "//div[@id='dropdown']//div")
        for item in items:
            if item.text.strip() == "Item 10":
                print(123)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
                time.sleep(3)
                item.click()
                print(item)
                break

        dropdown_element = self.driver.find_element(By.XPATH, "//input[@id='comboBox']")

        # option_to_scroll_to = dropdown_element.find_element(By.XPATH, "//div[text()='Item 10']")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", option_to_scroll_to)
        # time.sleep(5)
        # option_to_scroll_to.click()


web_tab = Table()
# web_tab.web_table()
web_tab.web_table_data()
# web_tab.page_data()
# web_tab.choose_file()
# web_tab.broken_links()
# web_tab.scrolling_dropdown()
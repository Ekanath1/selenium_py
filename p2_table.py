import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Table:
    service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    def web_table(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
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
        self.driver.get("https://testautomationpractice.blogspot.com/")
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

        with open("dynamic_data.txt", "w") as file:

            for data in data_list:
                file.writelines(data)
                file.write("\n")



    def page_data(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
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



web_tab = Table()
# web_tab.web_table()
web_tab.web_table_data()
# web_tab.page_data()
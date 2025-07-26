import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class  AssertEqual:
    service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    def assert_equal(self):

        expected_title = "GeeksforGeeks | A computer science portal for geeks"
        self.driver.get("https://www.geeksforgeeks.org/")
        # print(driver.title) "GeeksforGeeks | Your All-in-One Learning Portal"
        actual_title = self.driver.title
        assert actual_title == expected_title, "Title mismatch"

    def assert_not_equal(self):
        expected_title = "GeeksforGeeks | A computer science portal for geeks"
        self.driver.get("https://www.geeksforgeeks.org/")
        actual_title = self.driver.title

        assert actual_title != expected_title, "title match"

    def assert_true(self):
        expected_title = "GeeksforGeeks | A computer science portal for geeks"
        self.driver.get("https://www.geeksforgeeks.org/")
        actual_title = self.driver.title
        if actual_title == expected_title:
            assert True

    def assert_fasle(self):
        expected_title = "GeeksforGeeks | A computer science portal for geeks"
        self.driver.get("https://www.geeksforgeeks.org/")
        actual_title = self.driver.title
        if actual_title != expected_title:
            assert False

    def assert_in(self):
        title = "GeeksforGeeks | A computer science portal for geeks"
        self.driver.get("https://www.geeksforgeeks.org/")
        actual_title = self.driver.title
        assert "GeeksforGeeks" in actual_title


ass = AssertEqual()
# ass.assert_equal()
# ass.assert_not_equal()
ass.assert_in()
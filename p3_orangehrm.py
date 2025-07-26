import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Login:

    def orangehrm(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        time.sleep(4)
        driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("admin123")
        time.sleep(4)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)


log = Login()
log.orangehrm()
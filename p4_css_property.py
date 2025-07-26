import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CssProperty:

    def css_property(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        a = "//div[@id='tnb-login-btn']"
        element = wait.until(EC.presence_of_element_located((By.XPATH, a)))
        print(element.value_of_css_property("background"))
        print(element.value_of_css_property("style"))
        print(element.value_of_css_property("background-color"))
        print(element.value_of_css_property("color"))
        hrefs = driver.find_elements(By.TAG_NAME, 'a')
        print(len(hrefs))
        print(type(hrefs))
        for h in hrefs:
            print(h.get_attribute('href'))


pr = CssProperty()
pr.css_property()




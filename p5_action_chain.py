import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
class ActionChain:

    def action_cn(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        actions = ActionChains(driver)
        actions.send_keys(Keys.CTRL, Keys.SHIFT, "i")
        actions.perform()

act = ActionChain()
act.action_cn()




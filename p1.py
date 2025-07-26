import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class W3school:
    def search_by_id(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/")
        driver.maximize_window()
        driver.find_element(By.ID,"search2").send_keys("S")
        time.sleep(4)
        driver.find_element(By.XPATH, "//a[@class='search_item search_active']").click()
        time.sleep(5)


# search = W3school()
# search.search_by_id()

class Demo1:

    def find_element(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("http://demo.automationtesting.in/Windows.html")
        driver.maximize_window()
        time.sleep(5)
        # find xpath of button for child window page
        # this page no. 2
        driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
        time.sleep(5)
        # return all handles value of open browser window
        handles = driver.window_handles
        for i in handles:
            driver.switch_to.window(i)
            print(driver.title)
        driver.quit()

# demo = Demo1()
# demo.find_element()

class Demo2:

    def demo2(self):
        service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
        time.sleep(5)

        txt = driver.find_element(By.XPATH, "//tbody/tr[12]/td[1]")
        # txt1 = driver.find_element(By.XPATH, "//a[contains(text(),'Anant Raj Ltd.')]/self::a")

        print(txt.text)
        # print(txt1.text)

        # child = driver.find_elements(By.XPATH, "//a[contains(text(),'Anant Raj Ltd.')]/ancestor::tr/child::td")
        # for cld in child:
        #     print(cld.text)

        tt = driver.find_elements(By.XPATH, "//table[@id='allpage_links']//tr[2]//td")
        for data in tt:
            # print(data.text)
            dt = data.find_elements(By.XPATH, "//table[@id='allpage_links']//tr[2]//td//a")

            for d in dt:
                print(d.get_attribute('href'))
        driver.close()



d2 = Demo2()
d2.demo2()
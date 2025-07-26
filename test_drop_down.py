import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.common.exceptions import WebDriverException
import time

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_select_options(driver):
    driver.get('https://selenium.dev/selenium/web/formPage.html')

    select_element = driver.find_element(By.NAME, 'selectomatic')
    select = Select(select_element)

    two_element = driver.find_element(By.CSS_SELECTOR, "option[value='two']")
    print(two_element.text)
    four_element = driver.find_element(By.CSS_SELECTOR, "option[value='four']")
    count_element = driver.find_element(By.CSS_SELECTOR, "option[value='still learning how to count, apparently']")

    select.select_by_visible_text('Four')
    time.sleep(5)
    assert four_element.is_selected()

    select.select_by_value('two')
    time.sleep(5)
    assert two_element.is_selected()

    select.select_by_index(3)
    assert count_element.is_selected()


def test_select_multiple_options(driver):
    driver.get('https://selenium.dev/selenium/web/formPage.html')
    select_element = driver.find_element(By.NAME, 'multi')
    select = Select(select_element)

    ham_element = driver.find_element(By.CSS_SELECTOR, "option[value='ham']")
    gravy_element = driver.find_element(By.CSS_SELECTOR, "option[value='onion gravy']")
    egg_element = driver.find_element(By.CSS_SELECTOR, "option[value='eggs']")
    sausage_element = driver.find_element(By.CSS_SELECTOR, "option[value='sausages']")

    option_elements = select_element.find_elements(By.TAG_NAME, 'option')
    option_list = select.options
    assert option_elements == option_list

    selected_option_list = select.all_selected_options
    expected_selection = [egg_element, sausage_element]
    assert selected_option_list == expected_selection

    select.select_by_value('ham')
    select.select_by_value('onion gravy')
    assert ham_element.is_selected()
    assert gravy_element.is_selected()

    select.deselect_by_value('eggs')
    select.deselect_by_value('sausages')
    assert not egg_element.is_selected()
    assert not sausage_element.is_selected()


# def test_disabled_options1(driver):
#     driver.get('https://selenium.dev/selenium/web/formPage.html')
#
#     select_element = driver.find_element(By.NAME, 'single_disabled')
#     select = Select(select_element)
#
#     with pytest.raises(WebDriverException):
#         select.select_by_value('disabled')

def test_disabled_options(driver):
    driver.get('https://selenium.dev/selenium/web/formPage.html')

    select_element = driver.find_element(By.NAME, 'single_disabled')
    select = Select(select_element)

    disabled_option = driver.find_element(By.CSS_SELECTOR, "option[value='disabled']")
    assert not disabled_option.is_enabled()


def test_button_click(driver):
    driver.get('https://selenium.dev/selenium/web/formPage.html')
    driver.find_element(By.XPATH, "//input[@id='cheese']").click()
    cheese = driver.find_element(By.XPATH, "//input[@id='cheese']").is_selected()
    assert cheese

    button = driver.find_element(By.XPATH, "//input[@value='Click!']")
    button.click()
    time.sleep(5)

def test_key_down(driver):
    driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("abc")\
        .perform()

    assert driver.find_element(By.ID, "textInput").get_attribute('value') == "ABC"
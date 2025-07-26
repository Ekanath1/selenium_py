import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://selenium.dev/selenium/web/mouse_interaction.html"
@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=r"C:\Users\AKASH\Desktop\sel_path\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_click_and_hold(driver):
    driver.get(url)

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .click_and_hold(clickable) \
        .perform()

    time.sleep(3)
    assert driver.find_element(By.ID, "click-status").text == "focused"


def test_click_and_release(driver):
    driver.get(url)

    clickable = driver.find_element(By.ID, "click")
    ActionChains(driver) \
        .click(clickable) \
        .perform()
    time.sleep(3)

    assert "resultPage.html" in driver.current_url


def test_right_click(driver):
    driver.get(url)

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .context_click(clickable) \
        .perform()

    time.sleep(3)
    assert driver.find_element(By.ID, "click-status").text == "context-clicked"

@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_back_click_ab(driver):
    driver.get(url)
    driver.find_element(By.ID, "click").click()
    assert driver.title == "We Arrive Here"

    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.BACK)
    action.pointer_action.pointer_up(MouseButton.BACK)
    action.perform()
    time.sleep(4)

    assert driver.title == "BasicMouseInterfaceTest"

@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_forward_click_ab(driver):
    driver.get(url)
    driver.find_element(By.ID, "click").click()
    driver.back()
    assert driver.title == "BasicMouseInterfaceTest"

    action = ActionBuilder(driver)
    action.pointer_action.pointer_down(MouseButton.FORWARD)
    action.pointer_action.pointer_up(MouseButton.FORWARD)
    action.perform()

    assert driver.title == "We Arrive Here"


def test_double_click(driver):
    driver.get(url)

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver) \
        .double_click(clickable) \
        .perform()

    assert driver.find_element(By.ID, "click-status").text == "double-clicked"


def test_hover(driver):
    driver.get(url)

    hoverable = driver.find_element(By.ID, "hover")
    ActionChains(driver) \
        .move_to_element(hoverable) \
        .perform()

    assert driver.find_element(By.ID, "move-status").text == "hovered"


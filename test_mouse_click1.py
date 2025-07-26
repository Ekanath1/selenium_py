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


url = "https://selenium.dev/selenium/web/mouse_interaction.html"
def test_move_by_offset_from_element(driver):
    driver.get(url)

    mouse_tracker = driver.find_element(By.ID, "mouse-tracker")
    ActionChains(driver) \
        .move_to_element_with_offset(mouse_tracker, 8, 0) \
        .perform()

    coordinates = driver.find_element(By.ID, "relative-location").text.split(", ")
    assert abs(int(coordinates[0]) - 100 - 8) < 2

@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_move_by_offset_from_viewport_origin_ab(driver):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "absolute-location")))
    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(8, 0)
    action.perform()

    coordinates = driver.find_element(By.ID, "absolute-location").text.split(", ")

    assert abs(int(coordinates[0]) - 8) < 2


def test_move_by_offset_from_current_pointer_ab(driver):
    driver.get(url)

    action = ActionBuilder(driver)
    action.pointer_action.move_to_location(6, 3)
    action.perform()

    ActionChains(driver) \
        .move_by_offset(13, 15) \
        .perform()

    coordinates = driver.find_element(By.ID, "absolute-location").text.split(", ")

    assert abs(int(coordinates[0]) - 6 - 13) < 2
    assert abs(int(coordinates[1]) - 3 - 15) < 2


def test_drag_and_drop_onto_element(driver):
    driver.get(url)

    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    ActionChains(driver) \
        .drag_and_drop(draggable, droppable) \
        .perform()

    assert driver.find_element(By.ID, "drop-status").text == "dropped"


def test_drag_and_drop_by_offset(driver):
    driver.get(url)

    draggable = driver.find_element(By.ID, "draggable")
    start = draggable.location
    finish = driver.find_element(By.ID, "droppable").location
    ActionChains(driver) \
        .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
        .perform()

    assert driver.find_element(By.ID, "drop-status").text == "dropped"

@pytest.mark.order(1)
def test_copy_pest(driver):
    driver.get("https://text-compare.com/")
    input1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
    input2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

    input1.send_keys("Welcome to python")

    act = ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    act.send_keys(Keys.TAB).perform()

    act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


import time
import math 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.relative_locator import locate_with

def func(x: int):
    return math.log(abs(12*math.sin(x)))
    
try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    driver = webdriver.Chrome()
    
    driver.get(link)
    
    
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)
    answer = str(func(x))

    input_field = driver.find_element(By.ID, "answer")
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_radiobutton = driver.find_element(By.ID, "robotsRule")

    driver.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "robotsRule")))
    
    input_field.send_keys(answer)

    robot_checkbox.click()
    
    robot_radiobutton.click()
    
    submit_button.click()
    
    alert = WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    print(alert.text)
    alert.accept() 

finally:
    time.sleep(5)
    driver.quit
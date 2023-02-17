import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()

    link = "https://suninjuly.github.io/math.html"

    driver.get(link)
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    answer = calc(x)

    input_field = driver.find_element(By.ID, "answer")
    input_field.send_keys(answer)

    checkbox = driver.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    submit_button.click()
    
    wait = WebDriverWait(driver, timeout=10)
    alert = wait.until(expected_conditions.alert_is_present())
    print(alert.text)
    alert.accept()

finally:
    time.sleep(5)
    driver.quit()
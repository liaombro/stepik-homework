

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver = webdriver.Chrome()

    driver.get(link)

    go_button = driver.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    go_button.click()
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)


    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    answer = calc(x)

    input_field = driver.find_element(By.ID, "answer")
    input_field.send_keys(answer)


    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    submit_button.click()
    
    wait = WebDriverWait(driver, timeout=10)
    alert = wait.until(expected_conditions.alert_is_present())
    print(alert.text)
    alert.accept()

finally:
    time.sleep(5)
    driver.quit()
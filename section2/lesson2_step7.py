import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.NAME, "email")
    input3.send_keys("aaa@yandex.ru")
    input_file = driver.find_element(By.ID, "file")
    filepath = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(filepath, "2-7.txt")
    input_file.send_keys(filepath)
    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    wait = WebDriverWait(driver, timeout=10)
    alert = wait.until(expected_conditions.alert_is_present())
    print(alert.text)
    alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла

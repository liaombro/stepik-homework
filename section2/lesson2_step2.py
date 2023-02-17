import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

try:
    link = 'https://suninjuly.github.io/selects1.html'
    driver = webdriver.Chrome()
    
    driver.get(link)
    number1_element = driver.find_element(By.ID, "num1")
    number1 = int(number1_element.text)
    number2_element = driver.find_element(By.ID, "num2") 
    number2 = int(number2_element.text)
    
    sum =str(number1 + number2)
    
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(sum)

    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    submit_button.click()
    
    alert = WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
    print(alert.text)
    alert.accept()
    
finally:
    time.sleep(5)
    driver.quit()
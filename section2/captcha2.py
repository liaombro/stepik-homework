import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Captcha():
    def __init__(self, driver):
        self.driver = driver
    
    @staticmethod
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    def fill_input(self):
        x_element = self.driver.find_element(By.ID, "input_value")
        x = int(x_element.text)

        answer = self.calc(x)

        input_field = self.driver.find_element(By.ID, "answer")
        input_field.send_keys(answer)


        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
        submit_button.click()
        
        wait = WebDriverWait(self.driver, timeout=10)
        alert = wait.until(expected_conditions.alert_is_present())
        print(alert.text)
        alert.accept()

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from captcha2 import Captcha

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()

    driver.get(link)
    price_locator = (By.ID, "price")
    WebDriverWait(driver, timeout=10).until(expected_conditions.text_to_be_present_in_element(price_locator, "$100"))
    
    book_button = driver.find_element(By.ID, "book")
    book_button.click()
    
    capt = Captcha(driver)
    capt.fill_input()
    
finally:
    time.sleep(5)
    driver.quit()
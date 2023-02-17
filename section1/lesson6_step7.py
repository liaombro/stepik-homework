from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("ы")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = driver.switch_to_alert()
    print(alert.text)

finally:
    
    # успеваем скопировать код за 30 секунд
    #time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла

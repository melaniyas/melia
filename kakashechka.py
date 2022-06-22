from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 8).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button.click()

    button1 = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    x_element = browser.find_element(By.ID, "input_value")
    input1 = browser.find_element(By.ID, "answer")
    x = x_element.text
    y = calc(x)
    input1.send_keys(y)
    button1.click()

finally:
    time.sleep(30)
    browser.quit()
    
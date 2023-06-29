from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


brow = webdriver.Chrome()

brow.get("https://suninjuly.github.io/explicit_wait2.html")

button = brow.find_element(By.ID, "book")
WebDriverWait(brow, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
)
button.click()
x_num = brow.find_element(By.ID, "input_value")
x = x_num.text
y = calc(x)
brow.find_element(By.ID, "answer").send_keys(y)
brow.find_element(By.CSS_SELECTOR, "#solve").click()
time.sleep(5)
brow.quit()

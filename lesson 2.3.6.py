from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "https://suninjuly.github.io/redirect_accept.html"

brow = webdriver.Chrome()
brow.get(url)

brow.find_element(By.CSS_SELECTOR, '.btn').click()
window1 = brow.window_handles[1]
brow.switch_to.window(window1)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


x_num = brow.find_element(By.ID, "input_value")
x = x_num.text
y = calc(x)
brow.find_element(By.ID, "answer").send_keys(y)
brow.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(5)
brow.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

brow = webdriver.Chrome()
brow.get("https://suninjuly.github.io/wait1.html")

brow.find_element(By.ID, "button").click()
brow.quit()

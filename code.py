from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(r"C:\Users\Ash\Downloads\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target='"contact name"'
string="text to send"
x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(20):
    input_box.send_keys(string+Keys.ENTER)
    time.sleep(1)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

n = 0
urls = []
file = open('urls.txt', 'r')
lines = file.readlines()
for line in lines:
    n += 1
    urls.append(line)

browser = webdriver.Chrome(executable_path=r'C:\Users\Atharva\chromedriver.exe')
for i in range(0, n):
    browser.get('https://www.y2mate.com/en19')
    input_url = browser.find_element_by_id('txt-url')
    input_url.send_keys(urls[i])
    start_button = browser.find_element_by_id('btn-submit')
    start_button.click()
    time.sleep(5)

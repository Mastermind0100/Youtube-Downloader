from selenium import webdriver

# n = 0
# urls = []
# file = open('urls.txt', 'r')
# lines = file.readlines()
# for line in lines:
#     n += 1
#     urls.append(line)

n = 1
urls = ['https://www.youtube.com/watch?v=Ftexl9o4QX8&t=12s']

browser = webdriver.Chrome(executable_path=r'C:\Users\Atharva\chromedriver.exe')
for i in range(0, n):
    browser.get('https://www.y2mate.com/en19')
    input_url = browser.find_element_by_class_name('form-control input-lg')
    input_url.send_keys(urls[i])
    start_button = browser.find_element_by_id('btn-submit')
    start_button.click()

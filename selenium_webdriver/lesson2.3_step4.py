'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
'''
from selenium import webdriver
import time
import math

link = r"http://suninjuly.github.io/alert_accept.html"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    bro.find_element_by_css_selector("button.btn").click()
    bro.switch_to.alert.accept()
    x_val = bro.find_element_by_id("input_value")
    res = str(math.log(abs(12 * math.sin(int(x_val.text)))))
    bro.find_element_by_id("answer").send_keys(res)
    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()
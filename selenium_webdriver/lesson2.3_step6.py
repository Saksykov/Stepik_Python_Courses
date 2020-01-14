'''
Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''
import time
import math
from selenium import webdriver

link = r"http://suninjuly.github.io/redirect_accept.html"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    bro.find_element_by_css_selector("button.btn").click()
    new_window = bro.window_handles[1]
    bro.switch_to.window(new_window)
    x_val = bro.find_element_by_id("input_value")
    res = str(math.log(abs(12 * math.sin(int(x_val.text)))))
    bro.find_element_by_id("answer").send_keys(res)
    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()
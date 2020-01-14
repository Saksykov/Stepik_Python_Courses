'''
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''
import math
from selenium import webdriver
import time

link = r"http://SunInJuly.github.io/execute_script.html"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    x_val = bro.find_element_by_id("input_value")
    x = int(x_val.text)
    res = str(math.log(abs(12 * math.sin(x))))
    bro.find_element_by_id("answer").send_keys(res)
    bro.find_element_by_id("robotCheckbox").click()
    bro.execute_script("window.scrollBy(0, 200);")
    bro.find_element_by_id("robotsRule").click()
    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()

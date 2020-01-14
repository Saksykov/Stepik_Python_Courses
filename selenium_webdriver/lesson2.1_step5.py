'''
Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
'''
import time
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = r'http://suninjuly.github.io/math.html'
try:
    br = webdriver.Chrome()
    br.get(link)
    x_val = br.find_element_by_css_selector('span#input_value.nowrap')
    x = calc(x_val.text)
    ins_x = br.find_element_by_id('answer')
    ins_x.send_keys(x)
    check = br.find_element_by_id('robotCheckbox')
    check.click()
    radio = br.find_element_by_id('robotsRule')
    radio.click()
    button = br.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(15)
    br.quit()
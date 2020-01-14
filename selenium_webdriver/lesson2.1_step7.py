'''
Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
'''
import math
import time
from selenium import webdriver

link = r'http://suninjuly.github.io/get_attribute.html'
try:
    br = webdriver.Chrome()
    br.get(link)
    atr = br.find_element_by_tag_name('img')
    x_val = atr.get_attribute('valuex')
    x = str(math.log(abs(12*math.sin(int(x_val)))))
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
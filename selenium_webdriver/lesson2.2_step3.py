'''
Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
'''
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

link = r"http://suninjuly.github.io/selects2.html"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    el1_val = bro.find_element_by_css_selector("span#num1.nowrap")
    el1 = int(el1_val.text)
    el2_val = bro.find_element_by_css_selector("span#num2.nowrap")
    el2 = int(el2_val.text)
    res = el1 + el2
    select = Select(bro.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(res))
    but = bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()
'''
На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
Добавьте в самый верх своего кода import math
Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
str(math.ceil(math.pow(math.pi, math.e)*10000))(можно вставить данное выражение в свой код,
а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)
Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
Заполните скриптом форму так же как вы делали в предыдущем шаге урока
После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
'''
import time
from selenium import webdriver
import math

link = r'http://suninjuly.github.io/find_link_text'
find_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
value1 = 'input'
value2 = 'last_name'
value3 = 'city'
value4 = 'country'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    f_el = browser.find_element_by_link_text(find_link)
    f_el.click()
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
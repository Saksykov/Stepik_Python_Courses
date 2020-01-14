'''
На этот раз воспользуемся возможностью искать элементы по XPath.

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации,
как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки.
Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.
'''
import time
from selenium import webdriver

link = r'http://suninjuly.github.io/find_xpath_form'
value1 = 'input'
value2 = 'last_name'
value3 = 'city'
value4 = 'country'
but_value = '//button[@type=\'submit\']'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Andzha")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Saksykov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Elista")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath(but_value)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
'''
Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
'''
import time
from selenium import webdriver

link = r"http://suninjuly.github.io/file_input.html"
name = "An"
last_name = "Saks"
mail = "saks_an@mail.ru"
file_path = r"D:\\read.txt"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    bro.find_element_by_css_selector("input[name=\"firstname\"]").send_keys(name)
    bro.find_element_by_css_selector("input[name=\"lastname\"]").send_keys(last_name)
    bro.find_element_by_css_selector("input[name=\"email\"]").send_keys(mail)
    bro.find_element_by_id("file").send_keys(file_path)
    bro.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    bro.quit()

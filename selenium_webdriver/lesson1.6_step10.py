'''
Попробуем реализовать один из автотестов из предыдущего шага. Вам дана страница с формой регистрации.
Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля,
отмеченные символом *: First name, last name, email. Текст для полей может быть любым.
Успешность регистрации проверяется сравнением ожидаемого текста "Congratulations! You have successfully registered!"
с текстом на странице, которая открывается после регистрации.
Для сравнения воспользуемся стандартной конструкцией assert из языка Python.
'''
import time
from selenium import webdriver

link = r'http://suninjuly.github.io/registration2.html'
name = 'Andzha'
last_name = 'Saksykov'
email = 'saks_an@mail.ru'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    insert_name = browser.find_element_by_css_selector('div.first_block div.first_class .first')
    insert_name.send_keys(name)
    insert_last_name = browser.find_element_by_css_selector('div.first_block div.second_class input.second')
    insert_last_name.send_keys(last_name)
    insert_email = browser.find_element_by_css_selector('div.first_block div.third_class input.third')
    insert_email.send_keys(email)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(2)

    text_el = browser.find_element_by_tag_name('h1')
    text = text_el.text

    assert 'Congratulations! You have successfully registered!' == text

finally:
    time.sleep(3)
    browser.quit()
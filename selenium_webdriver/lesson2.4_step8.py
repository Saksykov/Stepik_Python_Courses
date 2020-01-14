'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = r"http://suninjuly.github.io/explicit_wait2.html"
try:
    bro = webdriver.Chrome()
    bro.get(link)
    # easy method to wait - browser.implicitly_wait(5)
    price = WebDriverWait(bro, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    bro.find_element_by_css_selector("button#book").click()
    x_val = bro.find_element_by_id("input_value")
    res = str(math.log(abs(12 * math.sin(int(x_val.text)))))
    bro.find_element_by_id("answer").send_keys(res)
    bro.find_element_by_id("solve").click()
    al = bro.switch_to.alert
    print(al.text)  # find answer for task
    al.accept()

finally:
    bro.quit()
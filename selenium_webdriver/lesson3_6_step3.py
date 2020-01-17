'''
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача - реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
'''
import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('link_part', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_find_answer_in_failed_tests(browser, link_part):
    link = f"https://stepik.org/lesson/236{link_part}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    insert = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.textarea")))
    insert.send_keys(answer)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()
    result = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint")))
    assert result.text == "Correct!", "Failed link - {}, Answer part - {}".format(link, result.text)

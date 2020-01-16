'''
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага - https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
'''

import unittest
from selenium import webdriver


class TestRegistrationForm(unittest.TestCase):
    link1 = r'http://suninjuly.github.io/registration1.html'
    link2 = r'http://suninjuly.github.io/registration2.html'
    name = 'An'
    last_name = 'Saks'
    email = 'saks_an@mail.ru'

    def registration(self, link):
        self.bro = webdriver.Chrome()
        self.bro.get(link)
        self.bro.implicitly_wait(5)
        insert_name = self.bro.find_element_by_css_selector('div.first_block div.first_class .first')
        insert_name.send_keys(self.name)
        insert_last_name = self.bro.find_element_by_css_selector('div.first_block div.second_class input.second')
        insert_last_name.send_keys(self.last_name)
        insert_email = self.bro.find_element_by_css_selector('div.first_block div.third_class input.third')
        insert_email.send_keys(self.email)
        self.bro.find_element_by_css_selector('button.btn').click()
        self.result = self.bro.find_element_by_tag_name('h1').text
        self.bro.quit()
        return self.result

    def test_registration_link_1(self):
        self.assertEqual(self.registration(self.link1),
                         "Congratulations! You have successfully registered!",
                         "failed registration")

    def test_registration_link_2(self):
        self.assertEqual(self.registration(self.link2),
                         "Congratulations! You have successfully registered!",
                         "failed registration")


if __name__ == "__main__":
    unittest.main()

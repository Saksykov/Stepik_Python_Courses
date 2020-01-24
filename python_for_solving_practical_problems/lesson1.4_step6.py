"""
В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица.
Просуммируйте все числа в ней. Теперь мы не только добавили разных тегов для изменения стиля отображения,
но и сделали невалидный HTML-код (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

resp = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html")
html = resp.read().decode("utf8")
soup = BeautifulSoup(html, "html.parser")
tab = soup.find_all("td")
res = 0
for i in tab:
    res += int(i.text)

print(res)

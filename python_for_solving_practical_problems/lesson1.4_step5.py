"""
В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения.
Для доступа к ячейкам используйте возможности BeautifulSoup.
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

resp = urlopen("https://stepik.org/media/attachments/lesson/209723/4.html")
html = resp.read().decode("utf8")
soup = BeautifulSoup(html, "html.parser")
tab = soup.find_all("td")
res = 0
for i in tab:
    res += int(i.text)

print(res)

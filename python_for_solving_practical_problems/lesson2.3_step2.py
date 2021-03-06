"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и
разделял целую и дробную часть чисел запятой. Таблица доступа по ссылке
https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx

Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты. Помогите ему и упорядочите
продукты по убыванию калорийности. В случае, если продукты имеют одинаковую калорийность - упорядочите их по названию.
В качестве ответа необходимо сдать названия продуктов, по одному в строке.
"""
import xlrd

workbook = xlrd.open_workbook("trekking1.xlsx")
sheet_names = workbook.sheet_names()
work_sheet = workbook.sheet_by_name(sheet_names[0])
prod_dic = {}

for i in range(1, 38):
    if work_sheet.cell_value(i, 1) not in prod_dic:
        prod_dic[work_sheet.cell_value(i, 1)] = []
    prod_dic[work_sheet.cell_value(i, 1)].append(work_sheet.cell_value(i, 0))

while len(prod_dic) > 0:
    max_cal = max(prod_dic)
    prod_dic[max_cal].sort()
    for o in prod_dic[max_cal]:
        print(o)
    prod_dic.pop(max_cal)

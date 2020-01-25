"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и
дробную часть чисел запятой.
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx

Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его
количества в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов.
Числа округлите до целых вниз и введите через пробел.
"""
import xlrd

workbook = xlrd.open_workbook("trekking2.xlsx")
workbook_names = workbook.sheet_names()
work_sheet_spr = workbook.sheet_by_name(workbook_names[0])
work_sheet_ras = workbook.sheet_by_name(workbook_names[1])

spr_dic = {}
for i in range(1, 38):
    spr_dic[work_sheet_spr.cell_value(i, 0)] = []
    for j in range(1, 5):
        spr_dic[work_sheet_spr.cell_value(i, 0)].append(work_sheet_spr.cell_value(i, j))

res = [0, 0, 0, 0]
for i in range(1, 13):
    pr = work_sheet_ras.cell_value(i, 0)
    gr = work_sheet_ras.cell_value(i, 1)
    for j in range(4):
        if spr_dic[pr][j] == "":
            spr_dic[pr][j] = 0
        res[j] += spr_dic[pr][j] / 100 * gr

for i in res:
    print(int(i), end=" ")

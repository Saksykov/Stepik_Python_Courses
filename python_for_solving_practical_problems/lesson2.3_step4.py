"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение
равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня,
названия продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и
граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел.
Информация о каждом дне должна выводиться в отдельной строке.
"""
import xlrd

wb = xlrd.open_workbook("trekking3.xlsx")
sheets = wb.sheet_names()
work_sheet_spr = wb.sheet_by_name(sheets[0])
work_sheet_ras = wb.sheet_by_name(sheets[1])

days = []
dict_spr = {}
for i in range(1, 38):
    dict_spr[work_sheet_spr.cell_value(i, 0)] = []
    for j in range(1, 5):
        if work_sheet_spr.cell_value(i, j) != "":
            dict_spr[work_sheet_spr.cell_value(i, 0)].append(work_sheet_spr.cell_value(i, j))
        else:
            dict_spr[work_sheet_spr.cell_value(i, 0)].append(0)

row = 1
for i in range(1, 10):
    kkal = [0, 0, 0, 0]
    try:
        while work_sheet_ras.cell_value(row, 0) == i:
            prod = work_sheet_ras.cell_value(row, 1)
            gr = work_sheet_ras.cell_value(row, 2)
            for j in range(4):
                kkal[j] += dict_spr[prod][j] / 100 * gr
            row += 1
        days.append(kkal)
    except IndexError:
        days.append(kkal)

for i in days:
    for j in i:
        print(int(j), end=" ")
    print()

"""
Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для разных
интересных ему профессий. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx.
Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент,
стоящий в середине массива после его упорядочивания) и, через пробел,
название профессии с самой высокой средней зарплатой по всем регионам.
"""
import xlrd

workbook = xlrd.open_workbook("salaries.xlsx")  # create workbook
sheet_names = workbook.sheet_names()  # return array - sheet names
work_sheet_by_name = workbook.sheet_by_name(sheet_names[0])  # return sheet by name
work_sheet_by_index = workbook.sheet_by_index(0)  # return sheet by index
cell_value = work_sheet_by_name.cell(1, 1).value  # return cell value in (строка, колонка)

reg_dic = {}
prof_dic = {}
for i in range(1, 9):
    reg_dic[work_sheet_by_index.cell_value(i, 0)] = []
for j in range(1, 8):
    prof_dic[work_sheet_by_name.cell_value(0, j)] = []

for i in range(1, 9):
    for j in range(1, 8):
        reg_dic[work_sheet_by_index.cell_value(i, 0)].append(work_sheet_by_index.cell_value(i, j))
        prof_dic[work_sheet_by_name.cell_value(0, j)].append(work_sheet_by_name.cell_value(i, j))

for reg in reg_dic:
    reg_dic[reg].sort()
    if len(reg_dic[reg]) % 2 == 0:
        reg_dic[reg] = reg_dic[reg][len(reg_dic[reg]) // 2]
    else:
        reg_dic[reg] = reg_dic[reg][len(reg_dic[reg]) // 2 + 1]
max_med = max(reg_dic.values())
for region in reg_dic:
    if reg_dic[region] == max_med:
        print(region, end=" ")

for pro in prof_dic:
    res = 0
    for zp in prof_dic[pro]:
        res += zp
    prof_dic[pro] = res / len(prof_dic[pro])
max_zp = max(prof_dic.values())
for prof in prof_dic:
    if prof_dic[prof] == max_zp:
        print(prof)

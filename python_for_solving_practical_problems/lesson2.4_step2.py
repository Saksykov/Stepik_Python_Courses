"""
Главный бухгалтер компании "Рога и копыта" случайно удалил ведомость с начисленной зарплатой.
К счастью, у него сохранились расчётные листки всех сотрудников. Помогите по этим расчётным листкам восстановить
 зарплатную ведомость. Архив с расчётными листками доступен по ссылке
 https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip (вы можете скачать и распаковать его вручную
 или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, в каждой строке должно быть указано ФИО сотрудника и,
через пробел, его зарплата. Сотрудники должны быть упорядочены по алфавиту.
"""
import xlrd
import zipfile

zip_file_path = r"C:/users/пк/downloads/rogaikopyta.zip"
rogaikopyta_zip = zipfile.ZipFile(zip_file_path)
zip_extract_path = r"D:/main"
rogaikopyta_zip.extractall(zip_extract_path)
rogaikopyta_zip.close()

res = []
res_dic = {}
for i in range(1, 1001):
    xlsx_book_path = f"d:/main/{str(i)}.xlsx"
    workbook = xlrd.open_workbook(xlsx_book_path)
    work_sheet = workbook.sheet_by_index(0)
    res_dic[work_sheet.cell_value(1, 1)] = int(work_sheet.cell_value(1, 3))
    res.append(work_sheet.cell_value(1, 1))

res.sort()
write_file_path = r"d:/main/res.txt"
with open(write_file_path, "w") as f:
    for fio in res:
        f.write(fio + " " + str(res_dic[fio]) + "\n")

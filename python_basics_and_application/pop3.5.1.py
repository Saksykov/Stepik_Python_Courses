'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз.
'''
import csv

res = {}
with open(r'D:\Crimes.csv', 'r') as rf:
    reader = csv.DictReader(rf)
    for i in reader:
        if i['Primary Type'] not in res:
            res[i['Primary Type']] = 1
        else:
            res[i['Primary Type']] += 1
m = 0
n = ''
for i in res:
    if res[i] > m:
        m = res[i]
        n = i
print(n)
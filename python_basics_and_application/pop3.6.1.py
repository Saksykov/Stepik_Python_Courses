'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный
математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
'''
import requests
import sys

api_url = 'http://numbersapi.com/'
p = '/math?json=true'
for num in sys.stdin:
    num = num.strip()
    res = requests.get(api_url + num + p)
    js = res.json()
    if js['found']:
        print('Interesting')
    else:
        print('Boring')

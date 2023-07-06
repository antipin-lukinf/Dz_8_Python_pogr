"""
Задание №3
📌 Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
Погружение в Python
"""
import csv
import random


def user_input():
    user_list = []
    while True:
        name = input('Name: ')
        if not name:
            return user_list
        while True:
            user_id = random.randint(10_000, 100_000)
            if user_id not in [uid[2] for uid in user_list]:
                break

        while True:
            lvl = input('Lvl: ')
            if lvl.isdigit() and 0 < int(lvl) < 8:
                user_list.append((name, lvl, user_id))
                break


def csv_write():
    user_list = user_input()
    result_dict = {}
    for user in user_list:
        if user[1] in result_dict:
            result_dict[user[1]].update({user[2]:user[0]})
        else:
            result_dict[user[1]] = {user[2]:user[0]}
    with open('result.csv', 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', quoting=csv.QUOTE_ALL) #fieldnames=['name', 'acsess level', 'id'],
        csv_write.writerow(('name', 'acsess level', 'id'))

        for user in user_list:
            csv_write.writerow(user)



csv_write()
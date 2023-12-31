"""
Задание №6
📌 Напишите функцию, которая преобразует pickle файл,
хранящий список словарей, в табличный csv файл.
📌 Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
📌 Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import os
import pickle

nes_extension = 'pickle'


def pickle_to_csv(path):
    for file in (os.listdir()):
        if os.path.isfile(file):
            initial_name, initial_ext = os.path.join(file).split('.')
            if initial_ext == nes_extension:
                with open(file, 'rb') as f:
                    new_dict = pickle.load(f)
                    # print(f'{new_dict = }')
                    initial_name = initial_name + '.csv'
                    with open(initial_name, 'w') as f:
                        csv_write = csv.DictWriter(f, fieldnames=[value for value in new_dict], quoting=csv.QUOTE_ALL)
                        csv_write.writeheader()
                        all_data = []
                        # for i, dict_row in enumerate(new_dict.values()):
                        #     if i != 0:
                        all_data.append(new_dict)
                        csv_write.writerow(new_dict)



pickle_to_csv(os.path.join(os.getcwd()))
"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
  Результаты обхода сохраните в файлы json, csv и pickle.
[]
○Для дочерних объектов указывайте родительскую директорию.
○Для каждого объекта укажите файл это или директория.
○Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import json
import os
import csv
import pickle


def recursive_traversal(directory):
    tree = os.walk(os.getcwd(), directory)
    res = {}
    for path, name_dir, file_name in tree:

        with os.scandir(path) as sp:
            file_size = []
            dir_size = []
            for entry in sp:
                if entry.is_file():
                    file_size.append(entry.stat().st_size)
                if entry.is_dir():
                    dir_size.append(entry.path)

        name_dir = str(name_dir) + '(directory)'
        file_name = str(file_name) + '(file)'
        parent_dir = os.path.abspath(os.path.join(str(name_dir), os.pardir))

        res[path] = [name_dir, file_name, parent_dir, dir_size, file_size]
    return res


res = recursive_traversal('stat_1')


def json_save(res):
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=4, ensure_ascii=False)


json_save(res)


def save_to_csv(res):
    with open('result.csv', 'w') as f:
        csv_write = csv.DictWriter(f, fieldnames=[value for value in res], quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        all_data = []
        # for i, dict_row in enumerate(new_dict.values()):
        #     if i != 0:
        all_data.append(res)
        csv_write.writerow(res)

save_to_csv(res)


def save_pickle(res):
    with open('result.pickle', 'wb') as file:
        pickle.dump(res, 'result.pickle')
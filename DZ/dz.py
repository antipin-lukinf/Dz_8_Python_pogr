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




def recursive_traversal(directory):
    tree = os.walk(os.getcwd(), directory)
    res = []
    for dir_path, dir_name, file_name in tree:

        res.append((dir_path, dir_name, file_name))
    return res


res = recursive_traversal('DZ')

def json_save(res):

    print(res)
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=4, ensure_ascii=False)


json_save(res)






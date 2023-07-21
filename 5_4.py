# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.
import json
import os
import csv
import pickle


def my_dirs(curr_dir: str) -> dict[int:{str: str}]:

    my_dict = {}
    types = ['file', 'dir']
    for i, file in enumerate(os.listdir(curr_dir), 1):
        path = os.path.join(curr_dir, file)
        item_dict = {'name': path.split('\\')[-1], 'parent': path.split('\\')[-2], 'type': None, 'size': None}
        my_dict[i] = item_dict
        if os.path.isfile(path):
            item_dict['size'] = f'{os.path.getsize(path)} b'
            item_dict['type'] = types[False]
        elif os.path.isdir(path):
            item_dict['type'] = types[True]
            my_dict.update(my_dirs(path))
    print(my_dict)

    with open('my_json.json5', 'w', encoding='utf-8') as j:
        json.dump(my_dict, j, ensure_ascii=True, indent=2)

    with open('my_csv.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter='|')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for key, value in my_dict.items():
            writer.writerow((key, value['name'], value['parent'], value['type'], value['size']))
    with open('my_pickle', 'wb') as t:
        pickle.dump(my_dict, t)


if __name__ == '__main__':
    my_dirs('777')


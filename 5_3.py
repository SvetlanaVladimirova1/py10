# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
import json
import os


def my_dirs(curr_dir: str) -> dict[int:{str: str}]:

    for dir_path, dir_name, file_name in os.walk(curr_dir):
        print(f'{dir_path =  }\n{dir_name =  }\n{file_name =  }\n')
        for i, file in enumerate(os.listdir(curr_dir), 1):
            my_dict = {}
            path = os.path.join(dir_path, file)
            item_dict = {'file_name': file_name, 'dir_name': dir_name, 'parent': path.split('\\')[:-1]}
            my_dict[i] = item_dict
            if os.path.isfile(path):
                item_dict['size'] = f'{os.path.getsize(path)} b'
                print(f'{os.path.getsize(path)} b')
                my_dict.update(my_dirs(path))
            with open('my_json.json', 'w', encoding='utf-8') as j:
                json.dump(my_dict, j, ensure_ascii=True, indent=2)
            print(my_dict)


if __name__ == '__main__':
    my_dirs('777')



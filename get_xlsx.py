import openpyxl
import datetime

from os.path import join, abspath
from typing import Dict, List

def handle_request(vmc, hb, rc, st, cd):
    """Обработка файлов с путями."""
    # Создаем словарь с путями
    files_dict = {
        "vmc": {
            "path": vmc.split('; ') if vmc else [],
            "check": ["визуальн"]
        },
        "hb": {
            "path": hb.split('; ') if hb else [],
            "check": ["твердост", "твёрдост"]
        },
        "rc": {
            "path": rc.split('; ') if rc else [],
            "check": ["радиограф", "ультразвук"]
        },
        "st": {
            "path": st.split('; ') if st else [],
            "check": ["флуоресцент"]
        },
        "cd": {
            "path": cd.split('; ') if cd else [],
            "check": ["капилляр"]
        },
    }

    # Удаляем ключи, у которых значения пустые массивы
    files_dict = {key: value for key, value in files_dict.items() if value['path']}

    # Проверка файлов, правильно ли они раскиданы по путям
    for file_info in files_dict.values():
        check_files(file_info['path'], file_info['check'])

    # Получение данных и запихивание их в словари

    # Объединение словарей

    # Сравнение словарей

    # Сотавление итоговой таблицы

    # Здесь будет логика обработки файлов
    print("Обработка файлов...")
    for key, value in files_dict.items():
        print(f"{key}: {value}")

def check_files(paths, check_keys):
    """Проверяет каждый файл в paths на наличие check_keys в первых 10 
       строках. Это необходимо, чтобы понять, в том ли текстовом поле 
       загружен файл. Это важно для последующей обработки файлов."""
    for path in paths:
        filename = path.split('/')[-1]
        try:
            # Открываем файл
            wb = openpyxl.load_workbook(path)
            sheet = wb.active  # Получаем первую страницу

            # Флаг, чтобы определить, найдено ли совпадение
            found = False

            # Проверяем первые 10 строк первого столбца
            for row in range(1, 11):  # Строки 1-10
                cell_value = sheet.cell(row=row, column=1).value
                # Проверяем, если ячейка не пустая и содержит одно из check_keys
                if cell_value and any(key in str(cell_value) for key in check_keys):
                    found = True
                    break  # Выходим из цикла, если найдено совпадение

            # Если совпадений не найдено, выбрасываем исключение
            if not found:
                raise ValueError(f"Файл {filename} не содержит нужные ключи в первых 10 строках.")

        except Exception as e:
            print(f"Ошибка при проверке файла {path}: {e}")


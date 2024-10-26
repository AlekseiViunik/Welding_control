"""
Этот файл принимает пути файлов, которые были указаны на главном окне
интерфейса пользователя. И выполняет с файлами по указанным путям 
следующие действия:
1. Используя ключевые слова проходит по файлам и проверяет, привальный ли файл
   лежит в указанном пути. Например путь к файлу ВИК должен указывать на
   файл протоколов визуально-измерительного контроля, а не, например, на
   протокол замеров твердости.
2. Использует собственный парсер, который прописан в parser.py, чтобы 
   прочесать все страницы всех файлов эксель и найти в них номера швов и 
   даты контроля этих швов. Парсер создает временное хранилище в виде 
   python словаря, в котором хранится вся информация о типе контроля и его
   дате для каждого шва.
3. Создает итоговую таблицу с номерами швов и разными датами контроля для них.
   Процесс создания таблицы прописан в create_summary. Для создания таблицы
   используются данные, полученные в п.2.   
"""
import openpyxl

import create_summary
import parser

from gui.messagebox import show_error
from default_settings.gui_settings import PATH_DIVIDER


# TODO убрать принт. Добавить аннотации.
def handle_request(vmc='', hb='', rc='', st='', cd=''):
    """Обработка файлов с путями."""
    # Создаем словарь с путями
    # TODO создать файл с константами и запихать все значения туда
    files_dict = {
        "vmc": {
            "path": vmc.split(PATH_DIVIDER) if vmc else [],
            "check": ["визуальн"]
        },
        "hb": {
            "path": hb.split(PATH_DIVIDER) if hb else [],
            "check": ["твердост", "твёрдост"]
        },
        "rc": {
            "path": rc.split(PATH_DIVIDER) if rc else [],
            "check": ["радиограф", "ультразвук"]
        },
        "st": {
            "path": st.split(PATH_DIVIDER) if st else [],
            "check": ["флуоресцент"]
        },
        "cd": {
            "path": cd.split(PATH_DIVIDER) if cd else [],
            "check": ["капилляр"]
        },
    }

    # Удаляем ключи, у которых значения пустые массивы
    files_dict = {
        key: value for key, value in files_dict.items() if value['path']
    }

    # Проверка файлов, правильно ли они раскиданы по путям
    # TODO разкомментить проверку после отладки
    for file_info in files_dict.values():
        check_files(file_info['path'], file_info['check'])
        #pass

    # Получение данных и запихивание их в словарь
    for key, value in files_dict.items():
        parser.parse_weld_data(value['path'], key)

    # Составление итоговой таблицы
    create_summary.create_summary_excel(parser.welds_data)

def check_files(paths, check_keys):
    """Проверяет каждый файл в paths на наличие check_keys в первых 10 
       строках. Это необходимо, чтобы понять, в том ли текстовом поле 
       загружен файл. Это важно для последующей обработки файлов."""
    for path in paths:
        filename = path.split('/')[-1]
        file_extension = path.split('.')[-1]
        if file_extension not in ['xlsx', 'xls', 'csv']:
            show_error(f"Какой-то непонятный файл тут: {path}")
            break
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
                show_error(f"Я не верю, что {filename} находится в нужном поле.")
                break

        except Exception as e:
            show_error(f"Ошибка при проверке файла {path}: {e}")
            break

if __name__ == '__main__':
    vmc = 'C:/Users/vjuni/Documents/Dev/Welding_control/files/A4993_VMC1.xlsx'
    hb = 'C:/Users/vjuni/Documents/Dev/Welding_control/files/A4993_HB.xlsx'
    rc = 'C:/Users/vjuni/Documents/Dev/Welding_control/files/A4993_RC.xlsx'
    st = 'C:/Users/vjuni/Documents/Dev/Welding_control/files/A4993_ST.xlsx'
    cd = 'C:/Users/vjuni/Documents/Dev/Welding_control/files/A4993_CD.xlsx'
    handle_request(vmc, hb, rc, st, cd)


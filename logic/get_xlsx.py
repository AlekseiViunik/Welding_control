"""
Этот файл принимает пути файлов, которые были указаны на главном окне
интерфейса пользователя. И выполняет с файлами по указанным путям
следующие действия:
1. Используя ключевые слова проходит по файлам и проверяет, правильный ли файл
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
import logging
import openpyxl

from . import create_summary
from . import parser

from gui.messagebox import show_error
from settings import (
    logic_settings as ls,
    gui_settings as gs,
    logging_settings as log
)


# TODO Добавить аннотации.
def handle_request(vmc='', hb='', rc='', st='', cd='', save_path=''):
    """Обработка файлов с путями."""
    # Создаем словарь с путями
    files_dict = {
        ls.VMC: {
            "path": vmc.split(gs.PATH_DIVIDER) if vmc else [],
            "check": ls.VMC_CHECK_KEYS
        },
        ls.HB: {
            "path": hb.split(gs.PATH_DIVIDER) if hb else [],
            "check": ls.HB_CHECK_KEYS
        },
        ls.RC: {
            "path": rc.split(gs.PATH_DIVIDER) if rc else [],
            "check": ls.RC_CHECK_KEYS
        },
        ls.ST: {
            "path": st.split(gs.PATH_DIVIDER) if st else [],
            "check": ls.ST_CHECK_KEYS
        },
        ls.CD: {
            "path": cd.split(gs.PATH_DIVIDER) if cd else [],
            "check": ls.CD_CHECK_KEYS
        },
    }

    # Удаляем ключи, у которых значения пустые массивы
    files_dict = {
        key: value for key, value in files_dict.items() if value['path']
    }

    logging.info(log.LOG_CHECK_FILES_START)
    logging.info(log.LOG_CHECK_FILES_CALL)
    for field, file_info in files_dict.items():
        if not check_files(file_info['path'], file_info['check'], field):
            return False
    logging.info(log.LOG_CHECK_FILES_DONE)

    logging.info(log.LOG_PARSE_START)
    logging.info(log.LOG_PARSE_CALL)
    # Получение данных и запихивание их в словарь
    for key, value in files_dict.items():
        parser.parse_weld_data(value['path'], key)
    logging.info(
        f"Парсинг выполнен. Количесвто элементов: {len(parser.welds_data)}"
    )

    logging.info(log.LOG_TABLE_START)
    logging.info(log.LOG_TABLE_METHOD_CALL)
    # Составление итоговой таблицы
    create_summary.create_summary_excel(parser.welds_data, save_path)
    logging.info(log.LOG_TABLE_DONE)
    return True


def check_files(paths, check_keys, field):
    """Проверяет каждый файл в paths на наличие check_keys в первых 10
       строках. Это необходимо, чтобы понять, в том ли текстовом поле
       загружен файл. Это важно для последующей обработки файлов."""
    for path in paths:
        filename = path.split(ls.FILEPATH_DIVIDER)[-1]
        file_extension = filename.split(ls.EXTENSION_DIVIDER)[-1]
        if file_extension not in ls.EXTENSIONS:
            show_error(
                (
                    f"Какой-то непонятный файл тут: {path}\n"
                    "Приложение закроется!"
                )
            )
            logging.error(f"Файл с недопустимым разрешением: {path}")
            return False
        try:
            wb = openpyxl.load_workbook(path)
            sheet = wb.active  # Получаем первую страницу

            # Флаг, чтобы определить, найдено ли совпадение
            found = False

            # Проверяем первые N строк первого столбца
            for row in range(ls.MIN_ROW_RANGE_VALUE, ls.MAX_ROW_RANGE_VALUE):
                cell_value = sheet.cell(row=row, column=1).value
                if cell_value and any(
                    key in str(cell_value) for key in check_keys
                ):
                    found = True
                    break

            if not found:
                show_error(
                    (
                        f"Я не верю, что {filename} находится в нужном поле.\n"
                        "Приложение закроется!"
                    )
                )
                logging.error(
                    f"Файл не на своем месте: {path} загружен для поля {field}"
                )
                return False

        except Exception as e:
            show_error(f"Ошибка при проверке файла {path}: {e}")
            logging.error(f"Ошибка при проверке файла {path}: {e}")
            return False
    return True

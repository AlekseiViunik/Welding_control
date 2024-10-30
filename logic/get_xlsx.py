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
import openpyxl

from . import create_summary
from . import parser

from gui.messagebox import show_error
from settings.gui_settings import PATH_DIVIDER
from settings import logic_settings as ls


# TODO Добавить аннотации.
def handle_request(vmc='', hb='', rc='', st='', cd='', save_path=''):
    """Обработка файлов с путями."""
    # Создаем словарь с путями
    files_dict = {
        ls.VMC: {
            "path": vmc.split(PATH_DIVIDER) if vmc else [],
            "check": ls.VMC_CHECK_KEYS
        },
        ls.HB: {
            "path": hb.split(PATH_DIVIDER) if hb else [],
            "check": ls.HB_CHECK_KEYS
        },
        ls.RC: {
            "path": rc.split(PATH_DIVIDER) if rc else [],
            "check": ls.RC_CHECK_KEYS
        },
        ls.ST: {
            "path": st.split(PATH_DIVIDER) if st else [],
            "check": ls.ST_CHECK_KEYS
        },
        ls.CD: {
            "path": cd.split(PATH_DIVIDER) if cd else [],
            "check": ls.CD_CHECK_KEYS
        },
    }

    # Удаляем ключи, у которых значения пустые массивы
    files_dict = {
        key: value for key, value in files_dict.items() if value['path']
    }

    # Проверка файлов, правильно ли они раскиданы по путям
    # TODO раскомментить после отладки
    for file_info in files_dict.values():
        # check_files(file_info['path'], file_info['check'])
        pass

    # Получение данных и запихивание их в словарь
    for key, value in files_dict.items():
        parser.parse_weld_data(value['path'], key)

    # Составление итоговой таблицы
    create_summary.create_summary_excel(parser.welds_data, save_path)


def check_files(paths, check_keys):
    """Проверяет каждый файл в paths на наличие check_keys в первых 10
       строках. Это необходимо, чтобы понять, в том ли текстовом поле
       загружен файл. Это важно для последующей обработки файлов."""
    for path in paths:
        filename = path.split(ls.FILEPATH_DIVIDER)[-1]
        file_extension = filename.split(ls.EXTENSION_DIVIDER)[-1]
        if file_extension not in ls.EXTENSIONS:
            show_error(f"Какой-то непонятный файл тут: {path}")
            break
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
                    f"Я не верю, что {filename} находится в нужном поле."
                )
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

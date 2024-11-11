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

from gui.messagebox import MessageBox
from settings import settings as set
from .create_summary import CreateSummary
from .parser import Parser


class GetXlsx:
    def __init__(self, vmc, hb, rc, st, cd, save_path, lang_code):
        self.vmc = vmc
        self.hb = hb
        self.rc = rc
        self.st = st
        self.cd = cd
        self.save_path = save_path
        self.lang_code = lang_code
        self.message_box = MessageBox()
        self.files_dict = {
            set.VMC: {
                "path": vmc.split(set.PATH_DIVIDER) if vmc else [],
                "check": set.VMC_CHECK_KEYS
            },
            set.HB: {
                "path": hb.split(set.PATH_DIVIDER) if hb else [],
                "check": set.HB_CHECK_KEYS
            },
            set.RC: {
                "path": rc.split(set.PATH_DIVIDER) if rc else [],
                "check": set.RC_CHECK_KEYS
            },
            set.ST: {
                "path": st.split(set.PATH_DIVIDER) if st else [],
                "check": set.ST_CHECK_KEYS
            },
            set.CD: {
                "path": cd.split(set.PATH_DIVIDER) if cd else [],
                "check": set.CD_CHECK_KEYS
            },
        }

    # TODO Добавить аннотации.
    def handle_request(self):
        """Обработка файлов с путями."""

        # Удаляем ключи, у которых значения пустые массивы
        self.files_dict = {
            key: value for key, value in self.files_dict.items() if value[
                'path'
            ]
        }

        # Проверка переданных файлов
        logging.info(set.log_check_files_start[self.lang_code])
        logging.info(set.log_check_files_call[self.lang_code])
        for field, file_info in self.files_dict.items():
            if not self.check_files(
                file_info['path'],
                file_info['check'],
                field
            ):
                return False
        logging.info(set.log_check_files_done[self.lang_code])

        # Получение данных и запихивание их в словарь
        logging.info(set.log_parse_start[self.lang_code])
        logging.info(set.log_parse_call[self.lang_code])
        parser = Parser(self.lang_code)
        for key, value in self.files_dict.items():
            parser.parse_weld_data(value['path'], key)
        logging.info(
            f"Парсинг выполнен. Количесвто элементов: {len(parser.welds_data)}"
        )

        # Составление итоговой таблицы
        logging.info(set.log_table_start[self.lang_code])
        logging.info(set.log_table_method_call[self.lang_code])
        create_summary = CreateSummary(self.lang_code)
        create_summary.create_summary_excel(parser.welds_data, self.save_path)
        logging.info(set.log_table_done[self.lang_code])
        return True

    def check_files(self, paths, check_keys, field):
        """Проверяет каждый файл в paths на наличие check_keys в первых 10
           строках. Это необходимо, чтобы понять, в том ли текстовом поле
           загружен файл. Это важно для последующей обработки файлов."""
        for path in paths:
            filename = path.split(set.FILEPATH_DIVIDER)[-1]
            file_extension = filename.split(set.EXTENSION_DIVIDER)[-1]
            if file_extension not in set.EXTENSIONS:
                message = (
                    f"Какой-то непонятный файл тут: {path}\n"
                    "Приложение закроется!"
                )
                self.message_box.show_error(
                    message,
                    self.lang_code
                )
                logging.error(f"Файл с недопустимым разрешением: {path}")
                return False
            try:
                wb = openpyxl.load_workbook(path)
                sheet = wb.active  # Получаем первую страницу

                # Флаг, чтобы определить, найдено ли совпадение
                found = False

                # Проверяем первые N строк первого столбца
                for row in range(
                    set.MIN_ROW_RANGE_VALUE,
                    set.MAX_ROW_RANGE_VALUE
                ):
                    cell_value = sheet.cell(row=row, column=1).value
                    if cell_value and any(
                        key in str(cell_value) for key in check_keys
                    ):
                        found = True
                        break

                if not found:
                    message = (
                        f"Я не верю, что {filename} находится в нужном "
                        "поле.\nПриложение закроется!"
                    )
                    self.message_box.show_error(
                        message,
                        self.lang_code
                    )
                    log_message = (
                        f"Файл не на своем месте: {path} загружен для "
                        f"поля {field}"
                    )
                    logging.error(log_message)
                    return False

            except Exception as e:
                message = f"Ошибка при проверке файла {path}: {e}"
                self.message_box.show_error(
                    message,
                    self.lang_code
                )
                logging.error(f"Ошибка при проверке файла {path}: {e}")
                return False
        return True

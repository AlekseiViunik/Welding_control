"""
Парсер. Парсит каждую страницу каждого переданного эксель файла и выписывает
все найденные швы и даты их контроля. Принцип такой:
0. Готовим стартовый пустой словарь welds_data для хранения итоговых
   результатов.
1. В parse_weld_data передаем массив путей с файлами одного типа контроля.
   Файлов может быть несколько. Пробегаемся циклом по каждому файлу
2. Открываем файл и пробегаемся циклом по каждой странице файла.
3. На каждой странице пробегаемя циклом по каждой строке и проверяем ее на
   соответствие регулярному выражению, записанному в weld_number_pattern.
   Регулярки соответствуют все строки типа <Одна_из_CYTNHСНТУ_букв> +
   любое количество цифр и дефисов в любой последовательности.
   ВАЖНО: номер шва должен быть в столбце A. Столбцы могут быть объединены,
   но в объединенных столбцах тогда должен быть столбец A.
4. Как только нашли номер шва, заменяем первую букву на кириллицу.
5. Идем по строке вправо в поисках даты. Дата у нас либо объект Datetime,
   либо цифры, разделенные разделителем "точка", "слеш", или "дефис".
6. Как только нашли дату, проверяем, есть ли в нашем итоговом словаре ключ
   для этого номера шва. Если нет, создаем его. Для каждого номера шва
   в словаре значением будет еще один словарь типа {тип_контроля: дата}.
   Если ключ с таким номером шва есть - добавляем в его значения тип контроля
   (передан как key в метод) и его дату.
"""
import re
from datetime import datetime

import openpyxl

from settings import logic_settings as ls


class Parser:
    def __init__(self):
        # TODO подключить Redis(?) для хранения данных вместо словаря
        self.welds_data = {}
        self.weld_number_pattern = re.compile(ls.WELD_ID_REGEXP)

    def parse_weld_data(self, paths, key):
        """Парсим все страницы переданных файлов в поисках номеров швов и дат
           контроля. Поскольку файлов много, как и страниц в каждом файле,
           как и самих швов на страницах, то операция будет проходить довольно
           долго."""

        for path in paths:
            wb = openpyxl.load_workbook(path, read_only=True)
            for sheet in wb.worksheets:
                for row in sheet.iter_rows(min_row=1):
                    weld_number = str(row[0].value)
                    if (
                        weld_number and
                        self.weld_number_pattern.match(weld_number)
                    ):
                        date_found = False
                        weld_number_ru = (
                            (ls.REPLACEMENT_DICT[weld_number[0]] +
                             weld_number[1:])
                            if weld_number[0] in ls.REPLACEMENT_DICT
                            else weld_number
                        )
                        if weld_number_ru not in self.welds_data.keys():
                            self.welds_data[weld_number_ru] = {}
                        for cell in row[1:]:
                            cell_value = cell.value
                            if isinstance(cell_value, datetime):
                                self.welds_data[weld_number_ru][key] = (
                                    cell_value.strftime(ls.DATE_FORMAT)
                                )
                                date_found = True
                                break
                            elif (
                                isinstance(cell_value, str) and
                                re.search(
                                    ls.DATE_REGEXP,
                                    cell_value
                                )
                            ):
                                try:
                                    # Пытаемся разобрать строку как дату
                                    date_found = True
                                    date = datetime.strptime(
                                        cell_value,
                                        ls.DATE_FORMAT
                                    )
                                    self.welds_data[weld_number_ru] = {
                                        key: date.strftime(ls.DATE_FORMAT)
                                    }
                                    break
                                except ValueError:
                                    continue
                            if date_found:
                                break

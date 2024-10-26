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
import openpyxl
from datetime import datetime

# TODO подключить Redis(?) для хранения данных вместо словаря
welds_data = {}
weld_number_pattern = re.compile(r'^[CYTNHСНТУ][-\d]*$')

# TODO создать файл с константами и запихать все значения туда
replacement_dict = {
    'C': 'С',  # Английская C на русскую С
    'H': 'Н',  # Английская H на русскую Н
    'T': 'Т',  # Английская T на русскую Т
    'Y': 'У'   # Английская Y на русскую У
}

def parse_weld_data(paths, key):
    """Парсим все страницы переданных файлов в поисках номеров швов и дат
       контроля. Поскольку файлов много, как и страниц в каждом файле,
       как и самих швов на страницах, то операция будет проходить довольно
       долго."""

    for path in paths:
        wb = openpyxl.load_workbook(path, read_only=True)
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(min_row=1):
                weld_number = str(row[0].value)
                if (weld_number and 
                    weld_number_pattern.match(weld_number)):
                    date_found = False
                    weld_number_ru = (
                        replacement_dict[weld_number[0]] + weld_number[1:]
                        if weld_number[0] in replacement_dict
                        else weld_number
                    )
                    if weld_number_ru not in welds_data.keys():
                        welds_data[weld_number_ru] = {}
                    for cell in row[1:]:
                        cell_value = cell.value
                        if isinstance(cell_value, datetime):
                            welds_data[weld_number_ru][key] = cell_value.strftime("%m/%d/%Y")  # Форматируем дату
                            date_found = True
                            break
                        elif (isinstance(cell_value, str) and 
                              re.search(
                                  r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}',
                                  cell_value
                              )):
                            try:
                                # Пытаемся разобрать строку как дату
                                date_found = True
                                date = datetime.strptime(
                                    cell_value, "%m/%d/%Y"
                                )
                                welds_data[weld_number_ru] = {
                                    key: date.strftime("%m/%d/%Y")
                                }
                                break
                            except ValueError:
                                continue
                        if date_found:
                            break

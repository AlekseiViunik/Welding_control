import re
import openpyxl
from datetime import datetime

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
    
    # TODO убрать return
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
    return welds_data

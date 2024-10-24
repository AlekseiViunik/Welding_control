import openpyxl

def create_summary_excel(welds_data, output_file='summary.xlsx'):
    # Создаем новый Workbook
    wb = openpyxl.Workbook()
    ws = wb.active

    # Устанавливаем заголовки столбцов
    # TODO перенести заголовки в константы
    headers = [
        "Номер шва",
        "Дата замера твёрдости",
        "Дата визуального контроля",
        "Дата стилоскопирования",
        "Дата РК или УЗК",
        "Дата цветной дефектоскопии"
    ]
    
    ws.append(headers)  # Добавляем заголовки в первую строку

    # Заполняем таблицу данными
    for weld_number, controls in welds_data.items():
        row = [
            weld_number,
            controls.get('hb', ''),  # Получаем дату контроля по типу
            controls.get('vmc', ''),
            controls.get('st', ''),
            controls.get('rc', ''),
            controls.get('cd', '')
        ]
        ws.append(row)  # Добавляем строку с данными

    # Сохраняем файл
    wb.save(output_file)
    print(f"Итоговая таблица сохранена в {output_file}")
import openpyxl

# TODO убрать принт
def create_summary_excel(welds_data, output_file='summary.xlsx'):
    """Создает итоговую таблицу в формате Excel на основе данных о швах."""
    wb = openpyxl.Workbook()
    ws = wb.active
    headers = [
        "Номер шва",
        "ВИК",
        "Твёрдость",
        "Стилоскопирование",
        "РК или УЗК",
        "ЦД",
        "Примечания"  # Новая колонка для примечаний
    ]

    # Записываем заголовки в таблицу
    ws.append(headers)

    for weld_number, control_dates in welds_data.items():
        # Получаем даты контроля по ключам
        hb = control_dates.get("hb", "")
        vmc = control_dates.get("vmc", "")
        st = control_dates.get("st", "")
        rc = control_dates.get("rc", "")
        cd = control_dates.get("cd", "")

        # Примечание по умолчанию
        note = ""

        # Сравнение дат
        if vmc:
            if hb and hb < vmc:
                note += "Замер твердости проведен раньше ВИК; "
            if st:
                if st < vmc:
                    note += "Стилоскопирование проведено раньше ВИК; "
                elif st < hb:
                    note += "Стилоскопирование проведено раньше замеров твердости; "
            if rc:
                if rc < vmc:
                    note += "РК или УЗК проведено раньше ВИК; "
                elif rc < hb:
                    note += "РК или УЗК проведено раньше замеров твердости; "
                elif rc < st:
                    note += "РК или УЗК проведено раньше стилоскопирования; "
            if cd:
                if cd < vmc:
                    note += "ЦД проведена раньше ВИК; "
                elif cd < hb:
                    note += "ЦД проведена раньше замеров твердости; "
                elif cd < st:
                    note += "ЦД проведена раньше замеров стилоскопирования; "
                elif cd < rc:
                    note += "ЦД проведена раньше замеров РК или УЗК; "    
        else:
            note += "Дата ВИК не указана; "

        # Записываем данные в строку таблицы
        row = [
            weld_number,
            vmc,
            hb,
            st,
            rc,
            cd,
            note.strip()  # Убираем лишние пробелы
        ]
        ws.append(row)

    wb.save(output_file)
    print(f"Итоговая таблица сохранена в {output_file}")
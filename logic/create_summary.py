import openpyxl

from datetime import datetime
from openpyxl.styles import NamedStyle
from tkinter import messagebox

from settings.logic_settings import (
    HEADERS, VMC, HB, RC, ST, CD, NOTE, NOTE_VMC_DOES_NOT_EXIST,
    NOTE_HB_LT_VMC, NOTE_ST_LT_HB, NOTE_ST_LT_VMC, NOTE_RC_LT_VMC,
    NOTE_RC_LT_HB, NOTE_RC_LT_ST, NOTE_CD_LT_VMC, NOTE_CD_LT_HB,
    NOTE_CD_LT_ST, NOTE_CD_LT_RC
)
from settings.user_settings import DEFAULT_SAVE_PATH

date_style = NamedStyle(name='datetime', number_format='DD/MM/YYYY')


# TODO убрать принт
def create_summary_excel(welds_data, output_file='summary.xlsx'):
    """Создает итоговую таблицу в формате Excel на основе данных о швах."""
    wb = openpyxl.Workbook()
    ws = wb.active

    # Записываем заголовки в таблицу
    ws.append(HEADERS)

    for weld_number, control_dates in welds_data.items():
        # Получаем даты контроля по ключам
        hb = datetime.strptime(
            control_dates.get(HB, ""), "%d/%m/%Y"
        ) if control_dates.get(HB, "") else None
        vmc = datetime.strptime(
            control_dates.get(VMC, ""), "%d/%m/%Y"
        ) if control_dates.get(VMC, "") else None
        st = datetime.strptime(
            control_dates.get(ST, ""), "%d/%m/%Y"
        ) if control_dates.get(ST, "") else None
        rc = datetime.strptime(
            control_dates.get(RC, ""), "%d/%m/%Y"
        ) if control_dates.get(RC, "") else None
        cd = datetime.strptime(
            control_dates.get(CD, ""), "%d/%m/%Y"
        ) if control_dates.get(CD, "") else None

        # Примечание по умолчанию
        note = NOTE

        # Сравнение дат
        if vmc:
            if hb and hb < vmc:
                note += NOTE_HB_LT_VMC
            if st:
                if st < vmc:
                    note += NOTE_ST_LT_VMC
                elif hb and st < hb:
                    note += NOTE_ST_LT_HB
            if rc:
                if rc < vmc:
                    note += NOTE_RC_LT_VMC
                elif hb and rc < hb:
                    note += NOTE_RC_LT_HB
                elif st and rc < st:
                    note += NOTE_RC_LT_ST
            if cd:
                if cd < vmc:
                    note += NOTE_CD_LT_VMC
                elif hb and cd < hb:
                    note += NOTE_CD_LT_HB
                elif st and cd < st:
                    note += NOTE_CD_LT_ST
                elif rc and cd < rc:
                    note += NOTE_CD_LT_RC
        else:
            note = NOTE_VMC_DOES_NOT_EXIST

        # Записываем данные в строку таблицы
        # используем символ " ' ", чтобы дата не записалась как число
        row = [
            weld_number,
            "'" + vmc.strftime("%d/%m/%Y") if vmc else "",
            "'" + hb.strftime("%d/%m/%Y") if hb else "",
            "'" + st.strftime("%d/%m/%Y") if st else "",
            "'" + rc.strftime("%d/%m/%Y") if rc else "",
            "'" + cd.strftime("%d/%m/%Y") if cd else "",
            note.strip()
        ]
        ws.append(row)

    wb.save(DEFAULT_SAVE_PATH)

    messagebox.showinfo(
        "Успех",
        f"Итоговая таблица сохранена в {DEFAULT_SAVE_PATH}"
    )

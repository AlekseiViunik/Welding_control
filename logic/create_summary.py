import openpyxl

from datetime import datetime
from openpyxl.styles import NamedStyle

from gui.messagebox import show_message
from settings import (
    logic_settings as ls,
    user_settings as us,
    gui_settings as gs
)

date_style = NamedStyle(name='datetime', number_format='DD/MM/YYYY')


# TODO убрать принт
def create_summary_excel(welds_data, output_file='summary.xlsx'):
    """Создает итоговую таблицу в формате Excel на основе данных о швах."""
    wb = openpyxl.Workbook()
    ws = wb.active

    # Записываем заголовки в таблицу
    ws.append(ls.HEADERS)

    for weld_number, control_dates in welds_data.items():
        # Получаем даты контроля по ключам
        hb = datetime.strptime(
            control_dates.get(ls.HB, ""), ls.DATE_FORMAT
        ) if control_dates.get(ls.HB, "") else None
        vmc = datetime.strptime(
            control_dates.get(ls.VMC, ""), ls.DATE_FORMAT
        ) if control_dates.get(ls.VMC, "") else None
        st = datetime.strptime(
            control_dates.get(ls.ST, ""), ls.DATE_FORMAT
        ) if control_dates.get(ls.ST, "") else None
        rc = datetime.strptime(
            control_dates.get(ls.RC, ""), ls.DATE_FORMAT
        ) if control_dates.get(ls.RC, "") else None
        cd = datetime.strptime(
            control_dates.get(ls.CD, ""), ls.DATE_FORMAT
        ) if control_dates.get(ls.CD, "") else None

        # Примечание по умолчанию
        note = ls.NOTE

        # Сравнение дат
        if vmc:
            if hb and hb < vmc:
                note += ls.NOTE_HB_LT_VMC
            if st:
                if st < vmc:
                    note += ls.NOTE_ST_LT_VMC
                elif hb and st < hb:
                    note += ls.NOTE_ST_LT_HB
            if rc:
                if rc < vmc:
                    note += ls.NOTE_RC_LT_VMC
                elif hb and rc < hb:
                    note += ls.NOTE_RC_LT_HB
                elif st and rc < st:
                    note += ls.NOTE_RC_LT_ST
            if cd:
                if cd < vmc:
                    note += ls.NOTE_CD_LT_VMC
                elif hb and cd < hb:
                    note += ls.NOTE_CD_LT_HB
                elif st and cd < st:
                    note += ls.NOTE_CD_LT_ST
                elif rc and cd < rc:
                    note += ls.NOTE_CD_LT_RC
        else:
            note = ls.NOTE_VMC_DOES_NOT_EXIST

        # Записываем данные в строку таблицы
        # используем символ " ' ", чтобы дата не записалась как число
        row = [
            weld_number,
            (ls.EXCEL_ESCAPING_SYMBOL +
             vmc.strftime(ls.DATE_FORMAT)) if vmc else "",
            (ls.EXCEL_ESCAPING_SYMBOL +
             hb.strftime(ls.DATE_FORMAT)) if hb else "",
            (ls.EXCEL_ESCAPING_SYMBOL +
             st.strftime(ls.DATE_FORMAT)) if st else "",
            (ls.EXCEL_ESCAPING_SYMBOL +
             rc.strftime(ls.DATE_FORMAT)) if rc else "",
            (ls.EXCEL_ESCAPING_SYMBOL +
             cd.strftime(ls.DATE_FORMAT)) if cd else "",
            note.strip()
        ]
        ws.append(row)

    wb.save(us.DEFAULT_SAVE_PATH)

    show_message(
        gs.SUCCESS_TITLE,
        gs.SAVED_FILE_SUCCESS_MESSAGE + us.DEFAULT_SAVE_PATH
    )

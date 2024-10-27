import openpyxl

from settings.logic_settings import (
    HEADERS, VMC, HB, RC, ST, CD, NOTE, NOTE_VMC_DOES_NOT_EXIST,
    NOTE_HB_LT_VMC, NOTE_ST_LT_HB, NOTE_ST_LT_VMC, NOTE_RC_LT_VMC,
    NOTE_RC_LT_HB, NOTE_RC_LT_ST, NOTE_CD_LT_VMC, NOTE_CD_LT_HB,
    NOTE_CD_LT_ST, NOTE_CD_LT_RC
)
from settings.user_settings import DEFAULT_SAVE_PATH


# TODO убрать принт
def create_summary_excel(welds_data, output_file='summary.xlsx'):
    """Создает итоговую таблицу в формате Excel на основе данных о швах."""
    wb = openpyxl.Workbook()
    ws = wb.active

    # Записываем заголовки в таблицу
    ws.append(HEADERS)

    for weld_number, control_dates in welds_data.items():
        # Получаем даты контроля по ключам
        hb = control_dates.get(HB, "")
        vmc = control_dates.get(VMC, "")
        st = control_dates.get(ST, "")
        rc = control_dates.get(RC, "")
        cd = control_dates.get(CD, "")

        # Примечание по умолчанию
        note = NOTE

        # Сравнение дат
        if vmc:
            if hb and hb < vmc:
                note += NOTE_HB_LT_VMC
            if st:
                if st < vmc:
                    note += NOTE_ST_LT_VMC
                elif st < hb:
                    note += NOTE_ST_LT_HB
            if rc:
                if rc < vmc:
                    note += NOTE_RC_LT_VMC
                elif rc < hb:
                    note += NOTE_RC_LT_HB
                elif rc < st:
                    note += NOTE_RC_LT_ST
            if cd:
                if cd < vmc:
                    note += NOTE_CD_LT_VMC
                elif cd < hb:
                    note += NOTE_CD_LT_HB
                elif cd < st:
                    note += NOTE_CD_LT_ST
                elif cd < rc:
                    note += NOTE_CD_LT_RC
        else:
            note = NOTE_VMC_DOES_NOT_EXIST

        # Записываем данные в строку таблицы
        row = [
            weld_number,
            vmc,
            hb,
            st,
            rc,
            cd,
            note.strip()
        ]
        ws.append(row)
    wb.save(DEFAULT_SAVE_PATH)

    # TODO заменить принт на всплывающее информационное окно
    print(f"Итоговая таблица сохранена в {DEFAULT_SAVE_PATH}")

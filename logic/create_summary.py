import logging
from datetime import datetime

import openpyxl
from openpyxl.styles import NamedStyle

from gui.messagebox import MessageBox
from settings import logging_settings as log
from settings import logic_settings as ls
from settings import user_settings as us
from settings.gui.windows import info_windows as info

date_style = NamedStyle(name='datetime', number_format='DD/MM/YYYY')


class CreateSummary:
    def __init__(self):
        self.message_box = MessageBox()

    def create_summary_excel(
            self,
            welds_data,
            save_path,
            output_file=us.SAVE_FILE_NAME
            ):
        """Создает итоговую таблицу в формате Excel на основе данных о швах."""
        logging.info(log.LOG_TABLE_CREATING)
        wb = openpyxl.Workbook()
        ws = wb.active

        # Записываем заголовки в таблицу
        logging.info(log.LOG_ADD_HEADERS)
        ws.append(ls.HEADERS)

        logging.info(log.LOG_ADD_DATA)
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
        logging.info(log.LOG_DATA_ADDED)
        file_direction = save_path + "/" + output_file
        logging.info(f"Сохраняем таблицу в {file_direction}")
        wb.save(file_direction)
        logging.info(log.LOG_TABLE_SAVED)

        self.message_box.show_message(
            info.SUCCESS_TITLE,
            info.SAVED_FILE_SUCCESS_MESSAGE + save_path
        )

import logging
from datetime import datetime

import openpyxl
from openpyxl.styles import NamedStyle

from gui.messagebox import MessageBox
from settings import settings as set

date_style = NamedStyle(name='datetime', number_format='DD/MM/YYYY')


class CreateSummary:
    def __init__(self, lang_code):
        self.message_box = MessageBox()
        self.lang_code = lang_code

    def create_summary_excel(
            self,
            welds_data,
            save_path,
            output_file=set.SAVE_FILE_NAME
            ):
        """Создает итоговую таблицу в формате Excel на основе данных о швах."""
        logging.info(set.log_table_creating[self.lang_code])
        wb = openpyxl.Workbook()
        ws = wb.active

        # Записываем заголовки в таблицу
        logging.info(set.log_add_headers[self.lang_code])
        ws.append(set.headers[self.lang_code])

        logging.info(set.log_add_data[self.lang_code])
        for weld_number, control_dates in welds_data.items():
            # Получаем даты контроля по ключам
            hb = datetime.strptime(
                control_dates.get(set.HB, ""), set.DATE_FORMAT
            ) if control_dates.get(set.HB, "") else None
            vmc = datetime.strptime(
                control_dates.get(set.VMC, ""), set.DATE_FORMAT
            ) if control_dates.get(set.VMC, "") else None
            st = datetime.strptime(
                control_dates.get(set.ST, ""), set.DATE_FORMAT
            ) if control_dates.get(set.ST, "") else None
            rc = datetime.strptime(
                control_dates.get(set.RC, ""), set.DATE_FORMAT
            ) if control_dates.get(set.RC, "") else None
            cd = datetime.strptime(
                control_dates.get(set.CD, ""), set.DATE_FORMAT
            ) if control_dates.get(set.CD, "") else None

            # Примечание по умолчанию
            note = set.NOTE

            # Сравнение дат
            if vmc:
                if hb and hb < vmc:
                    note += set.note_hb_lt_vmc[self.lang_code]
                if st:
                    if st < vmc:
                        note += set.note_st_lt_vmc[self.lang_code]
                    elif hb and st < hb:
                        note += set.note_st_lt_hb[self.lang_code]
                if rc:
                    if rc < vmc:
                        note += set.note_rc_lt_vmc[self.lang_code]
                    elif hb and rc < hb:
                        note += set.note_rc_lt_hb[self.lang_code]
                    elif st and rc < st:
                        note += set.note_rc_lt_st[self.lang_code]
                if cd:
                    if cd < vmc:
                        note += set.note_cd_lt_vmc[self.lang_code]
                    elif hb and cd < hb:
                        note += set.note_cd_lt_hb[self.lang_code]
                    elif st and cd < st:
                        note += set.note_cd_lt_st[self.lang_code]
                    elif rc and cd < rc:
                        note += set.note_cd_lt_rc[self.lang_code]
            else:
                note = set.note_vmc_does_not_exist[self.lang_code]

            # Записываем данные в строку таблицы
            # используем символ " ' ", чтобы дата не записалась как число
            row = [
                weld_number,
                (set.EXCEL_ESCAPING_SYMBOL +
                 vmc.strftime(set.DATE_FORMAT)) if vmc else "",
                (set.EXCEL_ESCAPING_SYMBOL +
                 hb.strftime(set.DATE_FORMAT)) if hb else "",
                (set.EXCEL_ESCAPING_SYMBOL +
                 st.strftime(set.DATE_FORMAT)) if st else "",
                (set.EXCEL_ESCAPING_SYMBOL +
                 rc.strftime(set.DATE_FORMAT)) if rc else "",
                (set.EXCEL_ESCAPING_SYMBOL +
                 cd.strftime(set.DATE_FORMAT)) if cd else "",
                note.strip()
            ]
            ws.append(row)
        logging.info(set.log_data_added[self.lang_code])
        file_direction = save_path + "/" + output_file
        logging.info(f"Сохраняем таблицу в {file_direction}")
        wb.save(file_direction)
        logging.info(set.log_table_saved[self.lang_code])

        self.message_box.show_message(
            set.success_title[self.lang_code],
            set.saved_file_success_message[self.lang_code] + save_path
        )

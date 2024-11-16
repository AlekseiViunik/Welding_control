import re
from datetime import datetime

import openpyxl

from settings import settings as set


class Parser:
    def __init__(self, lang_code):
        self.lang_code = lang_code
        self.welds_data = {}
        self.weld_number_pattern = (
            re.compile(set.joint_id_regexp[self.lang_code])
        )

    def parse_weld_data(self, paths, key):
        """
        Parse all pages of the provided files in search of joint ids and their
        control dates.
        """
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
                            # Change first symbol on the cyrillic one
                            (set.REPLACEMENT_DICT[weld_number[0]] +
                             weld_number[1:])
                            if weld_number[0] in set.REPLACEMENT_DICT
                            else weld_number
                        )
                        if weld_number_ru not in self.welds_data.keys():
                            self.welds_data[weld_number_ru] = {}
                        for cell in row[1:]:
                            cell_value = cell.value
                            if isinstance(cell_value, datetime):
                                self.welds_data[weld_number_ru][key] = (
                                    cell_value.strftime(set.DATE_FORMAT)
                                )
                                date_found = True
                                break
                            elif (
                                isinstance(cell_value, str) and
                                re.search(
                                    set.DATE_REGEXP,
                                    cell_value
                                )
                            ):
                                try:
                                    # trying to convert String to date
                                    date_found = True
                                    date = datetime.strptime(
                                        cell_value,
                                        set.DATE_FORMAT
                                    )
                                    self.welds_data[weld_number_ru] = {
                                        key: date.strftime(set.DATE_FORMAT)
                                    }
                                    break
                                except ValueError:
                                    continue
                            if date_found:
                                break

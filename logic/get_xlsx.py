import logging
import openpyxl

from logic.settings_handler import SettingsHandler
from gui.messagebox import MessageBox
from settings import settings as set
from .create_summary import CreateSummary
from .parser import Parser


class GetXlsx:
    def __init__(self, vmc, hb, rc, st, cd, lang_code):
        self.vmc = vmc
        self.hb = hb
        self.rc = rc
        self.st = st
        self.cd = cd
        self.lang_code = lang_code
        self.message_box = MessageBox()
        self.settings_handler = SettingsHandler()
        self.save_path = ''
        self.files_dict = {
            set.VMC: {
                set.FILES_DICT_PATH_KEY:
                    vmc.split(set.PATH_DIVIDER) if vmc else [],
                set.FILES_DICT_CHECK_KEY: set.VMC_CHECK_KEYS
            },
            set.HB: {
                set.FILES_DICT_PATH_KEY:
                    hb.split(set.PATH_DIVIDER) if hb else [],
                set.FILES_DICT_CHECK_KEY: set.HB_CHECK_KEYS
            },
            set.RC: {
                set.FILES_DICT_PATH_KEY:
                    rc.split(set.PATH_DIVIDER) if rc else [],
                set.FILES_DICT_CHECK_KEY: set.RC_CHECK_KEYS
            },
            set.ST: {
                set.FILES_DICT_PATH_KEY:
                    st.split(set.PATH_DIVIDER) if st else [],
                set.FILES_DICT_CHECK_KEY: set.ST_CHECK_KEYS
            },
            set.CD: {
                set.FILES_DICT_PATH_KEY:
                    cd.split(set.PATH_DIVIDER) if cd else [],
                set.FILES_DICT_CHECK_KEY: set.CD_CHECK_KEYS
            },
        }

    def handle_request(self):
        """Handling files provided."""
        self.save_path = self.settings_handler.file_read(
            set.DEFAULT_SAVE_PATH_KEY
        )
        # Remove the keys for the control types which paths are still empty
        self.files_dict = {
            key: value for key, value in self.files_dict.items() if value[
                set.FILES_DICT_PATH_KEY
            ]
        }

        # Provided files checking
        logging.info(set.log_check_files_start[self.lang_code])
        logging.info(set.log_check_files_call[self.lang_code])
        for field, file_info in self.files_dict.items():
            if not self.check_files(
                file_info[set.FILES_DICT_PATH_KEY],
                file_info[set.FILES_DICT_CHECK_KEY],
                field
            ):
                return False
        logging.info(set.log_check_files_done[self.lang_code])

        # Parse data and put it in the dict
        logging.info(set.log_parse_start[self.lang_code])
        logging.info(set.log_parse_call[self.lang_code])
        parser = Parser(self.lang_code)
        for key, value in self.files_dict.items():
            parser.parse_weld_data(value[set.FILES_DICT_PATH_KEY], key)
        logging.info(
            f"{set.log_parse_done_el_amount[self.lang_code]}"
            f"{len(parser.welds_data)}"
        )

        # Summary table creation
        logging.info(set.log_table_start[self.lang_code])
        logging.info(set.log_table_method_call[self.lang_code])
        create_summary = CreateSummary(self.lang_code)
        create_summary.create_summary_excel(parser.welds_data, self.save_path)
        logging.info(set.log_table_done[self.lang_code])
        return True

    def check_files(self, paths, check_keys, field):
        """
        Checks each file in paths for check_keys in the first 10
        lines. This is necessary to understand if the text field is in the
        right place the file has been uploaded. This is important for
        subsequent file processing.
        """
        for path in paths:
            filename = path.split(set.FILEPATH_DIVIDER)[-1]
            file_extension = filename.split(set.EXTENSION_DIVIDER)[-1]
            if file_extension not in set.EXTENSIONS:
                message = (
                    f"{set.unnknown_file_error[self.lang_code]}{path}\n"
                    f"{set.close_app_error[self.lang_code]}"
                )
                self.message_box.show_error(
                    message,
                    self.lang_code
                )
                logging.error(
                    f"{set.log_unacceptable_extension[self.lang_code]}{path}"
                )
                return False
            try:
                wb = openpyxl.load_workbook(path)
                sheet = wb.active

                found = False

                for row in range(
                    set.MIN_ROW_RANGE_VALUE,
                    set.MAX_ROW_RANGE_VALUE
                ):
                    cell_value = sheet.cell(row=row, column=1).value
                    if cell_value and any(
                        key in str(cell_value) for key in check_keys
                    ):
                        found = True
                        break

                if not found:
                    message = (
                        set.check_failed_error[self.lang_code].
                        format(filename, set.close_app_error[self.lang_code])
                    )
                    self.message_box.show_error(
                        message,
                        self.lang_code
                    )

                    log_message = (
                        set.log_check_failed_error[self.lang_code].
                        format(path, field)
                    )

                    logging.error(log_message)
                    return False

            except Exception as e:
                message = (
                    set.file_check_error[self.lang_code].format(path, e)
                )
                self.message_box.show_error(
                    message,
                    self.lang_code
                )
                logging.error(message)
                return False
        return True

import openpyxl
import datetime

from os.path import join, abspath
from typing import Dict, List


FOLDER_PATH: str = join('.', 'files')

VMC_FILE_NAME: str = 'A4993_VMC.xlsx'  # Visual Measuring Control. Goes first, true by default.
HB_FILE_NAME: str = 'A4993_HB.xlsx'  # Hardness control
ST_FILE_NAME: str = 'A4993_ST.xlsx'  # Styloscopy
RC_FILE_NAME: str = 'A4993_RC.xlsx'  # Radiografic control
CD_FILE_NAME: str = 'A4993_CD.xlsx'  # Color defectoscopy

VMC_FILE_PATH: str = abspath(join(FOLDER_PATH, VMC_FILE_NAME))
HB_FILE_PATH: str = abspath(join(FOLDER_PATH, HB_FILE_NAME))
ST_FILE_PATH: str = abspath(join(FOLDER_PATH, ST_FILE_NAME))
RC_FILE_PATH: str = abspath(join(FOLDER_PATH, RC_FILE_NAME))
CD_FILE_PATH: str = abspath(join(FOLDER_PATH, CD_FILE_NAME))

welds: Dict[str, Dict[str, str]] = {}  # {weld_number: {control_type: date}}

wb = openpyxl.reader.excel.load_workbook(
    filename=VMC_FILE_PATH, read_only=True
)

sheets: List[str] = wb.sheetnames

for i in range(len(sheets)):
    wb.active = i
    sheet = wb.active
    j = 1
    while True:
        weld_number = sheet['A' + str(j)].value
        control_date = sheet['C' + str(j)].value
        if isinstance(control_date, datetime.datetime):
            print(weld_number, control_date)

        if weld_number is not None or j > 100000:
            if weld_number.strip().lower()[:10] == 'заключение':
                break
        j += 1




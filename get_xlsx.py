import openpyxl
import datetime

from os.path import join, abspath
from typing import Dict, List

def handle_request(vmc, hb, rc, st, cd):
    """Обработка файлов с путями."""
    # Создаем словарь с путями
    files_dict = {
        "vmc": vmc,
        "hb": hb,
        "rc": rc,
        "st": st,
        "cd": cd.split(';')  # Если несколько путей, разделяем их
    }

    # Здесь будет логика обработки файлов
    print("Обработка файлов...")
    for key, value in files_dict.items():
        print(f"{key}: {value}")




import os

# Указываем путь сохранения итогового файла по умолчанию на рабочий стол
# Default:
# os.path.join(
#     os.path.expanduser("~"),
#     "Desktop",
#     "summary.xlsx"
# )
DEFAULT_SAVE_PATH = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "summary.xlsx"
)

# Указываем имя файла, под которым будут сохраняться пользовательские
# настройки
SETTINGS_FILE_NAME = "settings.json"  # Default: "settings.json"

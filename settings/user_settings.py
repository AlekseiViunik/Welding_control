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

# Здесь указан ключ файла json, значением которого является путь к сохранению
# итогового файла
SAVE_PATH_KEY = "DEFAULT_SAVE_PATH"  # Default: "DEFAULT_SAVE_PATH"

# Путь из корня проекта к папке с логикой
LOGIC_PATH = 'logic'  # Default: 'logic'

# Путь из корня проекта к папке с интерфейсом
GUI_PATH = 'gui'  # Default: 'gui'

# Отступ в пробелах для записи в json файл
JSON_INDENT = 4  # Default: 4

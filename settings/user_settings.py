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

# Здесь указан ключ файла json, значением которого является путь к сохранению
# итогового файла
DEFAULT_SAVE_PATH_KEY = "DEFAULT_SAVE_PATH"  # Default: "DEFAULT_SAVE_PATH"

# Здесь указан ключ файла json, значением которого является словарь с
# языковыми настройками
DEFAULT_LANG_KEY = "lang"  # Default "lang"

# Здесь указан ключ файла json, значением которого является код страны
# выбранного языка
DEFAULT_LANG_CODE_KEY = "code"  # Default: "code"

# Здесь указан код страны по умолчанию
DEFAULT_LANG_CODE = "ru"  # Default: "ru"

# Здесь указан ключ файла json, значением которого является путь к файлу с
# иконкой страны выбранного языка
DEFAULT_LANG_ICON_PATH_KEY = "icon_path"  # Default: "icon_path"

# Здесь указан путь к файлу с иконкой страны выбранного языка по умолчанию
# Default: "files/icons/ru.png"
DEFAULT_LANG_ICON_PATH = "files/icons/ru.png"

# Указываем имя файла, под которым будут сохраняться пользовательские
# настройки
SETTINGS_FILE_NAME = "settings.json"  # Default: "settings.json"

# Путь из корня проекта к папке с логикой
LOGIC_PATH = 'logic'  # Default: 'logic'

# Путь из корня проекта к папке с интерфейсом
GUI_PATH = 'gui'  # Default: 'gui'

# Отступ в пробелах для записи в json файл
JSON_INDENT = 4  # Default: 4

SAVE_FILE_NAME = "summary.xlsx"

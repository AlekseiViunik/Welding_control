"""
Здесь находятся настройки инструментов логирования.
"""

# Устанавливает максимальное количество строк файла логирования.
# Если при очередном запуске программы файл будет переполнен,
# он очистится.
MAX_LOG_LINES = 50000  # Default: 50000

# Кодировка файла логирования. Необходима для кириллицы. Лучше не трогать.
ENCODING = 'utf-8'  # Default: 'utf-8'

# Папка для хранения логов
LOG_FOLDER = 'logging_files'  # Default: 'logging_files'

# Имя файла логов
LOG_FILENAME = 'app.log'  # Default: 'app.log'

# Формат записи логов
# Default: '%(asctime)s - %(levelname)s - %(message)s'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# ==================Статические сообщения для логов==================

# Разделитель между логами разных процессов
# Default: "******************************************************"
LOG_DIVIDER = "******************************************************"

# Информирует о начале выполнения логики.
LOG_START = "Начало выполнения логики"  # Default: "Начало выполнения логики"

# Информирует о вызове метода WeldControlWindow.calculate_dates
# Default: "Вызов метода WeldControlWindow.calculate_dates"
LOG_CALCULATE_DATES_CALL = "Вызов метода WeldControlWindow.calculate_dates"

# Информирует о вызове метода WeldControlWindow.handle_request
# Default: "Вызов метода WeldControlWindow.handle_request"
LOG_HANDLE_REQUEST_CALL = "Вызов метода WeldControlWindow.handle_request"

# Информирует об ошибке в программе без конкретизации
# Default: "Обработка завершилась с ошибкой."
LOG_ERROR_MSG = "Обработка завершилась с ошибкой."

# Информирует о начале проверки файлов
# Default: "Начало проверки файлов, правильно ли они раскиданы по путям"
LOG_CHECK_FILES_START = (
    "Начало проверки файлов, правильно ли они раскиданы по путям"
)

# Информирует о вызове метода check_files
# Default: "Вызов метода check_files"
LOG_CHECK_FILES_CALL = "Вызов метода check_files"

# Информирует об окончании проверки check_files
# Default: "Проверка выполнена"
LOG_CHECK_FILES_DONE = "Проверка выполнена"

# Информирует начале парсинга
# Default: "Начало парсинга предоставленных файлов"
LOG_PARSE_START = "Начало парсинга предоставленных файлов"

# Информирует вызове метода parser.parse_weld_data
# Default: "Вызов метода parser.parse_weld_data"
LOG_PARSE_CALL = "Вызов метода parser.parse_weld_data"

# Информирование о начале создания итоговой таблицы
# Default: "Начало составления итоговой таблицы"
LOG_TABLE_START = "Начало составления итоговой таблицы"

# Информирует о вызове метода create_summary.create_summary_excel
# Default: "Вызов метода create_summary.create_summary_excel"
LOG_TABLE_METHOD_CALL = "Вызов метода create_summary.create_summary_excel"

# Информирует о создании итоговой таблицы
# Default: "Таблица составлена"
LOG_TABLE_DONE = "Таблица составлена"

# Информирует о запуске процесса создания итоговой таблицы
# Default: "Создаем таблицу"
LOG_TABLE_CREATING = "Создаем таблицу"

# Информирует о добавлении заголовков в итоговую таблицу
# Default: "Создаем заголовки"
LOG_ADD_HEADERS = "Создаем заголовки"

# Информирует о добавлении данных в итоговую таблицу
# Default: "Записываем данные..."
LOG_ADD_DATA = "Записываем данные..."

# Информирует о добавлении данных в итоговую таблицу
# Default: "Данные записаны"
LOG_DATA_ADDED = "Данные записаны"

# Информирует о сохранении итоговой таблицы
# Default: "Таблица сохранена"
LOG_TABLE_SAVED = "Таблица сохранена"

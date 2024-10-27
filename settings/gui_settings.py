"""
По сути это конфигурация главного окна.
"""

# Имя приложения
TITLE = "Dates Control - v1.0.0"  # Default: "Dates Control - v1.0.0"

# Размеры стартового окна
MAIN_WINDOW_WIDTH = 600  # Default: 600
MAIN_WINDOW_HEIGHT = 400  # Default: 400

# =====================Настройки для лейблов=========================

# Тексты для лейблов (описание, какой файл необходимо выбрать)
# Будут расположены в том же порядке, в котором перечислены в списке
# Порядок лучше не менять, иначе все по пизде пойдет.
# Это будет исправлено в будущем.
# Default: [
#            "Выбери файлы Визуального контроля",
#            "Выбери файлы Радиографического контроля",
#            "Выбери файлы Стилоскопирования",
#            "Выбери файлы Цветной дефектоскопии",
#            "Выбери файлы Твердости"
#          ]
LABELS = [
            "Выбери файлы Визуального контроля",
            "Выбери файлы Радиографического контроля",
            "Выбери файлы Стилоскопирования",
            "Выбери файлы Цветной дефектоскопии",
            "Выбери файлы Твердости"
        ]

# Определяем, к какой стороне окна будет привязка лейбла с текстом
# Доступные варианты:
# n: Север (верхний центр)
# s: Юг (нижний центр)
# e: Восток (правый центр)
# w: Запад (левый центр)
# ne: Северо-восток (верхний правый угол)
# nw: Северо-запад (верхний левый угол)
# se: Юго-восток (нижний правый угол)
# sw: Юго-запад (нижний левый угол)
# center: Центр (по умолчанию, если не задано значение anchor)
LABEL_ANCHOR = 'w'  # Default: 'w'

# =====================Настройки для фрейма==========================
# Содержат поле для ввода и кнопку

# Выбор оси, по которой будет растягивание фрейма (лучше не менять
# этот параметр)
FRAME_FILL_AXIS = 'x'  # Default: 'x'

# Отступы от краев по горизонтали
# Поскольку заполнение по умолчанию будет на весь размер окна по ширине,
# то отступы будут с обеих сторон
FRAME_PADX = 20  # Default: 20

# =================Настройки для текстовых полей=====================

# Ширина поля (в количестве символов)
ENTRY_WIDTH = 50  # Default: 50

# Размещение поля внутри фрейма
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
ENTRY_FRAME_SIDE = 'left'  # Default: 'left'

# Выбор оси, по которой будет растягивание поля (лучше не менять этот параметр)
ENTRY_FILL_AXIS = 'x'  # Default: 'x'

# Растяжение поля при изменении размеров главного окна
ENTRY_EXPAND = True  # Default: True

# ==================Настройки для кнопки фрейма======================

# Текст кнопки возле текстового поля
FRAME_BUTTON_TEXT = 'Обзор'  # Default: 'Обзор'

# Размещение кнопки внутри фрейма
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
FRAME_BUTTON_SIDE = 'right'  # Default: 'right'

# Отступ слева от кнопки
FRAME_BUTTON_LEFT_PADX = 10  # Default: 10

# Отступ справа от кнопки
FRAME_BUTTON_RIGHT_PADX = 0  # Default: 0

# ==============Настройки для разделительной строки==================
# Строка идет после каждого фрейма и нужна для отделения фреймов
# друг от друга, чтобы они не сливались

# Высота разделительной строки
DIVIDER_HEIGHT = 5  # Default: 5

# Выбор оси, по которой будет растягивание разделителя
# (лучше не менять этот параметр)

DIVIDER_FILL_AXIS = 'x'  # Default 'x'

# ================Настройки для фрейма и кнопок======================
# Фрейм, который используется для расположения 3х кнопок внизу

# Отступы для фрейма по вертикали в пикселях
BUTTONS_FRAME_PADY = 10  # Default: 10

# Ширина кнопок фрейма (в количестве вмещаемых символов)
BUTTONS_WIDTH = 15  # Default: 15

# Текст, отображаемый на кнопках в порядке указания элементов в массиве
# И процесс, запускаемый для каждой кнопки
# Default: BUTTON_TEXTS = {
#    "Погнали": "start_process",
#    "Забить": "clear_entries",
#    "Настройки": "open_settings",
#    }
BUTTON_TEXTS = {
    "Погнали": "start_process",
    "Забить": "clear_entries",
    "Настройки": "open_settings",
    }

# Отступы по горизонтали слева и справа для кнопок внутри фрейма
FRAME_BUTTONS_PADX = 5  # Default: 5

# Размещение кнопок внутри фрейма с учетом других кнопок
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# Возможные варианты:
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
FRAME_BUTTONS_SIDE = 'left'  # Default: 'left'

# ===============Настройки для метода browse_file====================

# Стартовый элемент очистки текстового поля и вставки в него
# рекомендуется не менять
FIRST_ELEMENT = 0  # Default: 0

# Разделитель пути файлов, если выбрано несколько файлов в одном тестовом поле
PATH_DIVIDER = '; '  # Default: '; '

# ===================Настройки для MessageBox========================

# Заголовок окна об ошибке
ERROR_MESSAGE_TITLE = 'Ошибка'  # Default: 'Ошибка'

# ===================Настройки для InfoWindow========================
# Это окно вылезает, когда начинается процесс обработки файлов и предупреждает
# юзера, что работа пошла, чтобы юзер не подумал, что приложение зависло.

# Ширина инфобокса
INFO_WINDOW_WIDTH = 200  # Default: 200

# Высота инфобокса
INFO_WINDOW_HEIGHT = 100  # Default: 100

# Заголовок инфобокса
INFO_WINDOW_TITLE = 'Для справки'  # Default: 'Для справки'

# Текст информационного сообщения
# Default: "Работа пошла.\nПодожди немного!"
INFO_LABEL_TEXT = "Работа пошла.\nПодожди немного!"

# Отступ по краям окна по горизонтали
INFO_LABEL_PADX = 20  # Default: 20

# Отступ по краям окна по вертикали
INFO_LABEL_PADY = 20  # Default: 20

# ===================Настройки для Авторства========================

# Текст лейбла
AUTHOR_LABEL_TEXT = "Created by Viunik"  # Default: "Created by Viunik"

# Привязка лейбла к краю экрана
# Доступные варианты:
# n: Север (верхний центр)
# s: Юг (нижний центр)
# e: Восток (правый центр)
# w: Запад (левый центр)
# ne: Северо-восток (верхний правый угол)
# nw: Северо-запад (верхний левый угол)
# se: Юго-восток (нижний правый угол)
# sw: Юго-запад (нижний левый угол)
# center: Центр (по умолчанию, если не задано значение anchor)
AUTHOR_ANCHOR = 's'  # Default: 's'

# Отступы по вертикали
AUTHOR_PADY = 5  # Default: 5

# Устанавливаем горизонтальную позицию от левого края окна (центр).
# Тут 0 - левый край, 1.0 - правый край, 0.5 - середина
AUTHOR_RELX = 0.5

# Устанавливаем вертикальную позицию от верхнего края окна (центр).
# Тут 0 - верхний край, 1.0 - нижний край, 0.5 - середина
AUTHOR_RELY = 1.0

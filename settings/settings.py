"""
Здесь все настройки приложения.
"""
import os

"""
================Константы и переменные графического интерфейса================
"""
# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================     Основные окна      ==========================
# ============================================================================

# Код языка РФ
RU_CODE = 'ru'

# Код языка Великобритании
GB_CODE = 'gb'

# Код языка Италии
IT_CODE = 'it'

# Список доступных кодов
# Сюда добавлять все константы кодов выше
LANG_CODES = [RU_CODE, GB_CODE, IT_CODE]

# Имя Главного окна
# Default: "Dates Control - v1.0.0"
START_WINDOW_TITLE = "Dates Control - v1.0.0"

# Имя окна настроек
# Default:
# {
#     RU_ICON_CODE: "Настройки",
#     GB_ICON_CODE: "Settings",
#     IT_ICON_CODE: "Impostazioni"
# }
settings_window_title = {
    RU_CODE: "Настройки",
    GB_CODE: "Settings",
    IT_CODE: "Impostazioni"
}

# Размеры стартового окна
WINDOW_WIDTH = 600  # Default: 600
WINDOW_HEIGHT = 400  # Default: 400

# ========================Настройки работы с иконками=========================

# Имя папки, в которой хранятся иконки.
ICONS_FOLDER_NAME = "files/icons"  # Default: icons

# Имя файла иконки приложения, которая будет отображаться в углу приложения
PNG_ICON_FILENAME = "mark32x32.png"

# Имя файла иконки приложения, которая будет отображаться в панели задач
ICO_ICON_FILENAME = "mark32x32.ico"

# Путь к .png иконке приложеня
PNG_ICON_FILEPATH = "files/icons/mark32x32.png"

# Путь к .ico иконке приложеня
ICO_ICON_FILEPATH = "files/icons/mark32x32.ico"

# Путь к .png иконке флага РФ
RU_ICON_PATH = 'files/icons/ru40x30.png'

# Путь к .png иконке флага Великобритании
GB_ICON_PATH = 'files/icons/gb40x30.png'

# Путь к .png иконке флага Италии
IT_ICON_PATH = 'files/icons/it40x30.png'

# ======================Настройки для метода browse_file======================

# Стартовый элемент очистки текстового поля и вставки в него
# рекомендуется не менять
FIRST_ELEMENT = 0  # Default: 0

# Разделитель пути файлов, если выбрано несколько файлов в одном тестовом поле
PATH_DIVIDER = '; '  # Default: '; '

# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================  Второстепенные окна   ==========================
# ============================================================================


# =========================Настройки для MessageBox===========================

# Заголовок окна об ошибке
# Default:
# {
#     RU_ICON_CODE: "Ошибка",
#     GB_ICON_CODE: "Error",
#     IT_ICON_CODE: "Errore"
# }
error_message_title = {
    RU_CODE: "Ошибка",
    GB_CODE: "Error",
    IT_CODE: "Errore"
}

# =========================Настройки для InfoWindow===========================
# Это окно вылезает, когда начинается процесс обработки файлов и предупреждает
# юзера, что работа пошла, чтобы юзер не подумал, что приложение зависло.

# Ширина инфобокса
INFO_WINDOW_WIDTH = 400  # Default: 200

# Высота инфобокса
INFO_WINDOW_HEIGHT = 100  # Default: 100

# Заголовок инфобокса
# Default:
# {
#     RU_ICON_CODE: "Для справки!",
#     GB_ICON_CODE: "For your information!",
#     IT_ICON_CODE: "Per l'informazione"
# }
info_window_title = {
    RU_CODE: "Для справки!",
    GB_CODE: "For your information!",
    IT_CODE: "Per l'informazione"
}

# =============Настройки информационных окон об успехе===============

# Заголовок окна об успехе
# Default:
# {
#     RU_ICON_CODE: "Успех!",
#     GB_ICON_CODE: "Success!",
#     IT_ICON_CODE: "Successo!"
# }
success_title = {
    RU_CODE: "Успех!",
    GB_CODE: "Success!",
    IT_CODE: "Successo!"
}

# Сообщение окна об успехе сохранения файла настроек
# Default:
# {
#     RU_ICON_CODE: "Настройки сохранены!",
#     GB_ICON_CODE: "The settings are saved!",
#     IT_ICON_CODE: "Impostazioni salvate!"
# }
saved_settings_success_message = {
    RU_CODE: "Настройки сохранены!",
    GB_CODE: "The settings are saved!",
    IT_CODE: "Le impostazioni sono salvate!"
}

# Сообщение окна об успехе сохранения настроек
# Это сообщение составляется из 2х частей: этой и
# пути из настроек в settings.json
# Default:
# {
#     RU_ICON_CODE: "Итоговая таблица сохранена в ",
#     GB_ICON_CODE: "The final table is saved in",
#     IT_ICON_CODE: "La tabella finale è salvata in"
# }
saved_file_success_message = {
    RU_CODE: "Итоговая таблица сохранена в ",
    GB_CODE: "The final table is saved in ",
    IT_CODE: "La tabella finale è salvata in "
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Фреймы         ==========================
# ============================================================================

# ==================Настройки для фрейма ввода пути==================
# Содержат лейбл, поле для ввода и кнопку

# Выбор оси, по которой будет растягивание фрейма (лучше не менять
# этот параметр)
FRAME_FILL_AXIS = 'x'  # Default: 'x'

# Отступы от краев по горизонтали
# Поскольку заполнение по умолчанию будет на весь размер окна по ширине,
# то отступы будут с обеих сторон
FRAME_PADX = 20  # Default: 20

# =============Настройки для фрейма разделительной строки============
# Строка идет после каждого фрейма и нужна для отделения фреймов
# друг от друга, чтобы они не сливались

# Высота разделительной строки
DIVIDER_HEIGHT = 10  # Default: 5

# Выбор оси, по которой будет растягивание разделителя
# (лучше не менять этот параметр)

DIVIDER_FILL_AXIS = 'x'  # Default 'x'

# ==================Настройки для фрейма и кнопок====================
# Фрейм, который используется для расположения кнопок внизу

# Отступы для фрейма по вертикали в пикселях
BUTTONS_FRAME_PADY = 10  # Default: 10

# ===============Настройки для фрейма основных кнопок================

# Отступ от края по вертикали сверху и снизу
SETTINGS_BUTTONS_FRAME_PADY = 20

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Кнопки         ==========================
# ============================================================================

# ==========================Общие настройки==========================
# Ширина кнопок фрейма по умолчанию (в количестве вмещаемых символов)
BUTTONS_WIDTH = 15  # Default: 15

# ====================Настройки для кнопки "Обзор"===================

# Текст кнопки
# Default:
# {
#     RU_ICON_CODE: "Обзор",
#     GB_ICON_CODE: "Browse",
#     IT_ICON_CODE: "Navigazione"
# }
browse_button_text = {
    RU_CODE: "Обзор",
    GB_CODE: "Browse",
    IT_CODE: "Navigazione"
}

# Размещение кнопки внутри фрейма
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
BROWSE_BUTTON_SIDE = 'right'  # Default: 'right'

# Отступ слева от кнопки
BROWSE_BUTTON_LEFT_PADX = 10  # Default: 10

# Отступ справа от кнопки
BROWSE_BUTTON_RIGHT_PADX = 0  # Default: 0

# ============Настройки для кнопок фрейма окна настроек==============

# Имя кнопки для сохранения
# Default:
# {
#     RU_ICON_CODE: "Сохранить",
#     GB_ICON_CODE: "Save",
#     IT_ICON_CODE: "Salvare"
# }
save_button_name = {
    RU_CODE: "Сохранить",
    GB_CODE: "Save",
    IT_CODE: "Salvare"
}

# Имя кнопки для отмены
# Default:
# {
#     RU_ICON_CODE: "Отмена",
#     GB_ICON_CODE: "Cancel",
#     IT_ICON_CODE: "Annullare"
# }
cancel_button_name = {
    RU_CODE: "Отмена",
    GB_CODE: "Cancel",
    IT_CODE: "Annullare"
}

# Размещение кнопок внутри фрейма с учетом других кнопок
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# Возможные варианты:
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
SETTINGS_BUTTONS_PACK_SIDE = "left"  # Default: "left"

# Отступы от края и друг от друга по горизонтали
SETTINGS_BUTTONS_PADX = 5  # Default: 5

# Текст, отображаемый на кнопках окна настроек.
# И процесс, запускаемый для каждой кнопки
# Default:
# {
#     code: {
#         save_button_name[code]: "save_settings",
#         cancel_button_name[code]: "destroy",
#     }
#     for code in LANG_CODES
# }
settings_buttons_name_to_process = {
    code: {
        save_button_name[code]: "save_settings",
        cancel_button_name[code]: "destroy",
    }
    for code in LANG_CODES
}

# ==============Настройки фрейма кнопок стартового окна==============

# Имя кнопки для запуска процесса обработки файлов
# Default:
# {
#     RU_CODE: "Погнали",
#     GB_CODE: "Run",
#     IT_CODE: "Vai"
# }
go_button_name = {
    RU_CODE: "Погнали",
    GB_CODE: "Run",
    IT_CODE: "Vai"
}

# Имя кнопки для очистки всех текстовых полей
# {
#     RU_CODE: "Забить",
#     GB_CODE: "Clear",
#     IT_CODE: "Cancellare"
# }
clean_button_name = {
    RU_CODE: "Забить",
    GB_CODE: "Clear",
    IT_CODE: "Cancellare"
}

# Имя кнопки для открытия окна настроек
# Default:
# {
#     RU_CODE: "Настройки",
#     GB_CODE: "Settings",
#     IT_CODE: "Impostazioni"
# }
settings_button_name = {
    RU_CODE: "Настройки",
    GB_CODE: "Settings",
    IT_CODE: "Impostazioni"
}

# Текст, отображаемый на кнопках в порядке указания элементов в массиве
# И процесс, запускаемый для каждой кнопки
# Default: BUTTON_TEXTS = {
#    "Погнали": "start_process",
#    "Забить": "clear_entries",
#    "Настройки": "open_settings",
#    }
start_buttons_name_to_process = {
    code: {
        go_button_name[code]: "start_process",
        clean_button_name[code]: "clear_entries",
        settings_button_name[code]: "open_settings"
    }
    for code in LANG_CODES
}

# =================Расположение кнопок внутри фрейма=================

# Отступы по горизонтали слева и справа для кнопок внутри фрейма
FRAME_BUTTONS_PADX = 5  # Default: 5

# Отступы по вертикали сверху и снизу для кнопок внутри фрейма
FRAME_BUTTONS_PADY = 5  # Default: 5

# Размещение кнопок внутри фрейма с учетом других кнопок
# При указании одной и той же стороны, элементы будут прижаты друг к другу
# с учетом отступов.
# Возможные варианты:
# 'left' - слева
# 'right' - справа
# 'top' - сверху
# 'botton' - снизу
FRAME_BUTTONS_SIDE = 'left'  # Default: 'left'

# =====================Найстройки языковых кнопок====================
lang = {
    RU_CODE: RU_ICON_PATH,
    GB_CODE: GB_ICON_PATH,
    IT_CODE: IT_ICON_PATH
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Лейблы         ==========================
# ============================================================================

# =====================Настройки для Лейбла Авторства======================

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
AUTHOR_PADY = -5  # Default: 5

# Устанавливаем горизонтальную позицию от левого края окна (центр).
# Тут 0 - левый край, 1.0 - правый край, 0.5 - середина
AUTHOR_RELX = 0.5

# Устанавливаем вертикальную позицию от верхнего края окна (центр).
# Тут 0 - верхний край, 1.0 - нижний край, 0.5 - середина
AUTHOR_RELY = 1.0

# =============Настройки для Лейбла информационного окна=============
# Текст информационного сообщения
# Default:
# {
#     RU_CODE: "Работа пошла.\nПодожди немного!",
#     GB_CODE: "The work has started.\nWait a bit!",
#     IT_CODE: "Il lavoro è iniziato.\nAspetta un attimo!"
# }
info_label_text = {
    RU_CODE: "Работа пошла.\nПодожди немного!",
    GB_CODE: "The work has started.\nWait a bit!",
    IT_CODE: "Il lavoro è iniziato.\nAspetta un attimo!"
}

# Отступ по краям окна по горизонтали
INFO_LABEL_PADX = 20  # Default: 20

# Отступ по краям окна по вертикали
INFO_LABEL_PADY = 20  # Default: 20

# ================Настройки лейбла для окна настроек=================

# Текст для лейбла окна настроек
# Default:
# {
#     RU_CODE: "Куда сохранять итоговый файл?",
#     GB_CODE: "Where should I save the final file?",
#     IT_CODE: "Dove salvare il file finale?"
# }
where_to_save = {
    RU_CODE: "Куда сохранять итоговый файл?",
    GB_CODE: "Where should I save the final file?",
    IT_CODE: "Dove salvare il file finale?"
}

# ==============Настройки для лейблов стартового окна================

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

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================     Текстовые поля     ==========================
# ============================================================================

# ===============Настройки для текстовых полей фрейма================

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

"""
==============================================================================
"""

"""
========================Константы и переменные логики=========================
"""
# =====================Настройки для get_xlsx.py=====================
# =====================Ключи для проверки файлов=====================
# По этим текстовым ключам проверяется каждый файл. Если указанного
# куска текста нет в указанном файле, значит файл был выбран в
# неправильном текстовом поле.
# Принцип: ищем в первых строках файла текст, который соответствует ключам.
# если текст найден, то файл выбран правильно. Если нет, райзим ошибку.
# Например: файл ВИК был выбран в поле для файлов Стилоскопирования.

# Ключ для проверки протоколов визуального и измерительного контроля (ВИК)
VMC_CHECK_KEYS = ["визуальн"]  # Default ["визуальн"]

# Ключ для проверки протоколов замеров твердости
HB_CHECK_KEYS = ["твердост", "твёрдост"]  # Default ["твердост", "твёрдост"]

# Ключ для проверки протоколов радиографического контроля (РК или УЗК)
# Default ["радиограф", "ультразвук"]
RC_CHECK_KEYS = ["радиограф", "ультразвук"]

# Ключ для проверки протоколов стилоскопирования (СТ)
ST_CHECK_KEYS = ["флуоресцент"]  # Default ["флуоресцент"]

# Ключ для проверки протоколов цветной дефектоскопии (ЦД)
CD_CHECK_KEYS = ["капилляр"]  # Default ["капилляр"]

# Ключи у словаря files_dict у нас тоже настраиваемые и могут быть любыми,
# поэтому перенесем имена ключей в константы.
# Кстати, итоговый словарь, в котором хранятся типы контроля и даты контроля
# каждого типа для каждого шва у нас пока хранится в файле parser.py и
# структура такая:
# {<номер_шва>: {<тип_контроля>: <дата_контроля>}}
# В create_summary нам нужно будет вытащить даты контроля для каждого шва по
# типу контроля, где мы будем использовать эти же константы

# Ключ для визуального и измерительного контроля
VMC = 'vmc'  # Default: 'vmc'
# Ключ для контроля твердости
HB = 'hb'  # Default: 'hb'
# Ключ для радиографического или ультразвукового контроля
RC = 'rc'  # Default: 'rc'
# Ключ для ренгенофуоресцентного контроля или стилоскопирования
ST = 'st'  # Default: 'st'
# Ключ для цветной дефектоскопии
CD = 'cd'  # Default: 'cd'

# ========================Остальные настройки========================

# Разделитель, который используется для строки, содержащей путь к файлу.
# Необходим для получения имени файла из пути к нему.
FILEPATH_DIVIDER = '/'  # Default: '/'

# Разделитель, который используется для строки, содержащей имя файла.
# Необходим для получения разрешения файла из его имени.
# рекомендуется не трогать
EXTENSION_DIVIDER = '.'  # Default: '.'

# Разрешения, которые допустимы для файлов
EXTENSIONS = ['xlsx']

# Значения, которые определяют, с какой по какую строку мы будем искать
# совпадения по ключам для проверки файлов.
MIN_ROW_RANGE_VALUE = 1  # Default: 1
MAX_ROW_RANGE_VALUE = 11  # Default: 10

# ======================Настройки для parser.py======================

# Регулярное выражение для поиска номера шва. Обычно название шва состоит из
# одной буквы кириллицы, означающей тип шва и случайного набора чисел,
# чередующихся с дефисами.
# Варианты букв могут быть только определенные:
# С криллица или латиница - стыковой шов
# Н криллица или латиница - нахлесточный шов
# Т криллица или латиница - тавровый шов
# У или Y (редко) - угловой шов
# N - нестандартный шов
# Примеры наименования швов, подходящих под регулярное выражение:
# C-1
# T12-1-1
# N3-3
# Номера швов, которые не встречаются, но тоже подходят:
# C---1
# H11-1-
# T-
# Номера швов, которые не подойдут:
# A1-1
# Это_номер_шва
# TT-1-1-1
WELD_ID_REGEXP = r'^[CYTNHСНТУ][-\d]*$'  # Default: r'^[CYTNHСНТУ][-\d]*$'

# Поскольку в номерах швов у нас должны быть только кириллические буквы,
# но имеются также и похожие буквы латиницы, то благодаря человеческому
# фактору, один и тот же номер шва в разных протоколах может быть написан
# в разной раскладке. Особенно это касается буквы С, которая находится на
# одной и той же клавише, независимо от раскладки и это самый ебланский
# косяк чувака, который придумал раскладку ЙЦУКЕН. Отдельно можно было бы
# еще сказать про то, что чтобы запятую написать, я должен шифт зажимать,
# но это уже совсем другая история.
# В связи с чем, нужно для каждого номера шва менять букву латиницы на
# букву кириллицы. Этот словарь нужен для такого сопоставления букв.
# Default:
# {
#     'C': 'С',  # Английская C на русскую С
#     'H': 'Н',  # Английская H на русскую Н
#     'T': 'Т',  # Английская T на русскую Т
#     'Y': 'У'   # Английская Y на русскую У
# }
REPLACEMENT_DICT = {
    'C': 'С',  # Английская C на русскую С
    'H': 'Н',  # Английская H на русскую Н
    'T': 'Т',  # Английская T на русскую Т
    'Y': 'У'   # Английская Y на русскую У
}

# Обычно, дата в экселе отображается как объект datetime, но если, по
# каким-то причинам, дата преобразована в строку, то не мешало бы проверить
# и это.
# Эта регулярка нужна для проверки значения текущей ячейки на соответсвие его
# одному из форматов даты.
# А форматы могут быть такие:
# 1. С одной или двумя цифрами для номера дня и месяца.
# 2. С двумя или четырьмя цифрами для номера года.
# 3. С разделителем в виде точки, слеша или дефиса.
# Default: r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}'
DATE_REGEXP = r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}'

# В конце концов, какой бы не была дата, мы преобразуем ее в полюбившийся
# почти всем формат типа дд/мм/гггг. Ебанем универсалочку, так сказать. В
# таком формате дата будет отображена в итоговом сгенерированном файле.
DATE_FORMAT = "%d/%m/%Y"  # Default: "%d/%m/%Y"

# ==================Настройки для create_summary.py==================

# Имена колонок для генерируемой таблицы. Идут слева направо по порядку
# их перечисления в списке.
# Лучше ничего не добавлять и не удалять, а то все по пизде пойдет.
# Но переименовывать можно. В будущем исправлю.
# Default:
# [
#    "Номер шва",
#    "ВИК",
#    "Твёрдость",
#    "Стилоскопирование",
#    "РК или УЗК",
#    "ЦД",
#    "Примечания"
# ]
HEADERS = [
    "Номер шва",
    "ВИК",
    "Твёрдость",
    "Стилоскопирование",
    "РК или УЗК",
    "ЦД",
    "Примечания"
]

# Тут должны были быть константы для ключей типа VMC, CD, RC, HB и ST,
# но я их перенес выше, так как они используются сразу в двух файлах.
# Ищи их там

# Дефолтное значение ячейки в столбце с примечаниями:
NOTE = ""  # Default: ""

# Ниже значения, которые мы будем дописывать в note, когда какая-то из дат
# прописана неверно. Название констант будет составляться так:
# NOTE_<тип_контроля>_LT(less_than)_<другой_тип_контроля>, что означает,
# что контроль <тип_контроля> проведен раньше, чем <другой_тип_контроля>,
# что является ошибкой и такого быть не должно.

# Default: "Замер твердости проведен раньше ВИК; "
NOTE_HB_LT_VMC = "Замер твердости проведен раньше ВИК; "
# Default: "Стилоскопирование проведено раньше ВИК; "
NOTE_ST_LT_VMC = "Стилоскопирование проведено раньше ВИК; "
# Default: "Стилоскопирование проведено раньше замеров твердости; "
NOTE_ST_LT_HB = "Стилоскопирование проведено раньше замеров твердости; "
# Default: "РК или УЗК проведено раньше ВИК; "
NOTE_RC_LT_VMC = "РК или УЗК проведено раньше ВИК; "
# Default: "РК или УЗК проведено раньше замеров твердости; "
NOTE_RC_LT_HB = "РК или УЗК проведено раньше замеров твердости; "
# Default: "РК или УЗК проведено раньше стилоскопирования; "
NOTE_RC_LT_ST = "РК или УЗК проведено раньше стилоскопирования; "
# Default: "ЦД проведена раньше ВИК; "
NOTE_CD_LT_VMC = "ЦД проведена раньше ВИК; "
# Default: "ЦД проведена раньше замеров твердости; "
NOTE_CD_LT_HB = "ЦД проведена раньше замеров твердости; "
# Default: "ЦД проведена раньше замеров стилоскопирования; "
NOTE_CD_LT_ST = "ЦД проведена раньше замеров стилоскопирования; "
# Default: "ЦД проведена раньше замеров РК или УЗК; "
NOTE_CD_LT_RC = "ЦД проведена раньше замеров РК или УЗК; "
# Default: "Дата ВИК не указана!"
NOTE_VMC_DOES_NOT_EXIST = "Дата ВИК не указана!"

# Формат даты по умолчанию для записи в итоговый файл
DATE_FORMAT = "%d/%m/%Y"  # Default: "%d/%m/%Y"

# Символ экранирования для даты в эксель
EXCEL_ESCAPING_SYMBOL = "'"
"""
==============================================================================
"""

"""
=====================Константы и переменные логирования=======================
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

# Информирует о вызове метода App.calculate_dates
# Default: "Вызов метода App.calculate_dates"
LOG_CALCULATE_DATES_CALL = "Вызов метода App.calculate_dates"

# Информирует о вызове метода App.handle_request
# Default: "Вызов метода App.handle_request"
LOG_HANDLE_REQUEST_CALL = "Вызов метода App.handle_request"

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
"""
==============================================================================
"""

"""
===============Константы и переменные пользовательских настроек===============
"""
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

# Здесь указан ключ файла json, значением которого является путь к файлу с
# иконкой страны выбранного языка
DEFAULT_LANG_ICON_PATH_KEY = "icon_path"  # Default: "icon_path"

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

"""
==============================================================================
"""

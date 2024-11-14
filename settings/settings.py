"""
Здесь все настройки приложения.
"""
import os

# Код языка РФ
RU_CODE = 'ru'

# Код языка Великобритании
GB_CODE = 'gb'

# Код языка Италии
IT_CODE = 'it'

# Список доступных кодов
# Сюда добавлять все константы кодов выше
LANG_CODES = [RU_CODE, GB_CODE, IT_CODE]

"""
##############################################################################
##############################################################################
##############################################################################
####################                                     #####################
####################      Настройки на разных языках     #####################
####################   Settings on different languages   #####################
####################   Impostazioni in diverse lingue    #####################
####################                                     #####################
##############################################################################
##############################################################################
##############################################################################
"""
"""
================Константы и переменные графического интерфейса================
"""
# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================     Основные окна      ==========================
# ============================================================================

# Имя окна настроек
# Default:
# {
#     RU_CODE: "Настройки",
#     GB_CODE: "Settings",
#     IT_CODE: "Impostazioni"
# }
settings_window_title = {
    RU_CODE: "Настройки",
    GB_CODE: "Settings",
    IT_CODE: "Impostazioni"
}

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
# ==========================         Кнопки         ==========================
# ============================================================================

# ====================Настройки для кнопки "Обзор"===================

# Текст кнопки
# Default:
# {
#     RU_ICON_CODE: "Обзор",
#     GB_ICON_CODE: "Browse",
#     IT_ICON_CODE: "Navigazione"
# }
browse_button_name = {
    RU_CODE: "Обзор",
    GB_CODE: "Browse",
    IT_CODE: "Navigazione"
}

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
clear_button_name = {
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
        clear_button_name[code]: "clear_entries",
        settings_button_name[code]: "open_settings"
    }
    for code in LANG_CODES
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Лейблы         ==========================
# ============================================================================

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
# Default:
# {
#     RU_CODE: [
#         "Выбери файлы Визуального контроля",
#         "Выбери файлы Радиографического контроля",
#         "Выбери файлы Стилоскопирования",
#         "Выбери файлы Цветной дефектоскопии",
#         "Выбери файлы Твердости"
#     ],
#     GB_CODE: [
#         "Select Visual Inspection files",
#         "Select Radiographic Inspection files",
#         "Select Styloscopy files",
#         "Select the Color Flaw detection files",
#         "Select the Hardness measurement files"
#     ],
#     IT_CODE: [
#         "Scegli i file di controllo visivo",
#         "Scegli i file di controllo radiografico",
#         "Scegli i file di Styloscoping",
#         "Scegli i file di rilevamento dei difetti A Colori",
#         "Scegli i file di misurazione della durezza"
#     ],
# }
labels = {
    RU_CODE: [
        "Выбери файлы Визуального контроля",
        "Выбери файлы Радиографического контроля",
        "Выбери файлы Стилоскопирования",
        "Выбери файлы Цветной дефектоскопии",
        "Выбери файлы Твердости"
    ],
    GB_CODE: [
        "Select Visual Inspection files",
        "Select Radiographic Inspection files",
        "Select Styloscopy files",
        "Select the Color Flaw detection files",
        "Select the Hardness measurement files"
    ],
    IT_CODE: [
        "Scegli i file di controllo visivo",
        "Scegli i file di controllo radiografico",
        "Scegli i file di Styloscoping",
        "Scegli i file di rilevamento dei difetti A Colori",
        "Scegli i file di misurazione della durezza"
    ],
}

"""
==============================================================================
"""

"""
========================Константы и переменные логики=========================
"""
# =========================Настройки для get_xlsx.py==========================

# Сообщение о том, что приложение закроется.
# Default:
# {
#     RU_CODE: "Приложение закроется!",
#     GB_CODE: "The App will close!",
#     IT_CODE: "L'app chiude!",
# }
close_app_error = {
    RU_CODE: "Приложение закроется!",
    GB_CODE: "The App will close!",
    IT_CODE: "L'app chiude!",
}

# Сообщение о том, что загружен файл с непонятным разрешением
# Default:
# {
#     RU_CODE: "Какой-то непонятный файл тут: ",
#     GB_CODE: "Unnknown file here: ",
#     IT_CODE: "Il file sconosciuto qui: ",
# }
unnknown_file_error = {
    RU_CODE: "Какой-то непонятный файл тут: ",
    GB_CODE: "Unnknown file here: ",
    IT_CODE: "Il file sconosciuto qui: ",
}

# Сообщает, что файл находится не в нужном поле
# Default:
# {
#     RU_CODE: "Я не верю, что {} находится в нужном поле.\n{}",
#     GB_CODE: "I don't believe that {} is in the right place.\n{}",
#     IT_CODE: "Non credo che {} si trovi al posto giusto.\n{}",
# }
check_failed_error = {
    RU_CODE: "Я не верю, что {} находится в нужном поле.\n{}",
    GB_CODE: "I don't believe that {} is in the right place.\n{}",
    IT_CODE: "Non credo che {} si trovi al posto giusto.\n{}",
}

file_check_error = {
    RU_CODE: "Ошибка при проверке файла {}: {}",
    GB_CODE: "File check error {}: {}",
    IT_CODE: "Errore durante la convalida del file {}: {}",
}

# ==========================Настройки для parser.py===========================

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
# Default:
# {
#     RU_CODE: r'^[CYTNHСНТУ][-\d]*$',
#     GB_CODE: r'^[a-zA-Z][-\d]*$',
#     IT_CODE: r'^[a-zA-Z][-\d]*$',
# }
joint_id_regexp = {
    RU_CODE: r'^[CYTNHСНТУ][-\d]*$',
    GB_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
    IT_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
}

# =======================Настройки для create_summary.py======================

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
headers = {
    RU_CODE: [
        "Номер шва",
        "ВИК",
        "Твёрдость",
        "Стилоскопирование",
        "РК или УЗК",
        "ЦД",
        "Примечания"
    ],
    GB_CODE: [
        "Joint id",
        "Visual",
        "Hardness",
        "Styloscopy",
        "Radioghraph or Ultrasonic",
        "Color",
        "Notes"
    ],
    IT_CODE: [
        "Id saldatura",
        "Visivo",
        "Durezza",
        "Stiloscopia",
        "Radiografia o ultrasuoni",
        "Colore",
        "Nota"
    ],
}

# Ниже значения, которые мы будем дописывать в note, когда какая-то из дат
# прописана неверно. Название констант будет составляться так:
# NOTE_<тип_контроля>_LT(less_than)_<другой_тип_контроля>, что означает,
# что контроль <тип_контроля> проведен раньше, чем <другой_тип_контроля>,
# что является ошибкой и такого быть не должно.
# Default:
# {
#     RU_CODE: "Замер твердости проведен раньше ВИК; ",
#     GB_CODE: "Hardness measurement is carried out before visual control",
#     IT_CODE: "Misurazione della durezza eseguita prima del controllo visivo",
# }
note_hb_lt_vmc = {
    RU_CODE: "Замер твердости проведен раньше ВИК; ",
    GB_CODE: "Hardness measurement is carried out before visual control",
    IT_CODE: "Misurazione della durezza eseguita prima del controllo visivo",
}
# Default:
# {
#     RU_CODE: "Стилоскопирование проведено раньше ВИК; ",
#     GB_CODE: "Styloscopy is performed before visual control",
#     IT_CODE: "Stiloscopia eseguita prima del controllo visivo",
# }
note_st_lt_vmc = {
    RU_CODE: "Стилоскопирование проведено раньше ВИК; ",
    GB_CODE: "Styloscopy is performed before visual control",
    IT_CODE: "Stiloscopia eseguita prima del controllo visivo",
}
# Default:
# {
#     RU_CODE: "Стилоскопирование проведено раньше замеров твердости; ",
#     GB_CODE: "Styloscopy is performed before hardness measurements",
#     IT_CODE: "Stiloscopia eseguita prima delle misure di durezza",
# }
note_st_lt_hb = {
    RU_CODE: "Стилоскопирование проведено раньше замеров твердости; ",
    GB_CODE: "Styloscopy is performed before hardness measurements",
    IT_CODE: "Stiloscopia eseguita prima delle misure di durezza",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше ВИК; ",
#     GB_CODE:
#         "Radiography or Ultrasonic are performed before visual control",
#     IT_CODE: "Radiografia o Ultrasuoni eseguiti prima del controllo visivo",
# }
note_rc_lt_vmc = {
    RU_CODE: "РК или УЗК проведено раньше ВИК; ",
    GB_CODE:
        "Radiography or Ultrasonic are performed before visual control",
    IT_CODE: "Radiografia o Ultrasuoni eseguiti prima del controllo visivo",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше замеров твердости; ",
#     GB_CODE: "Radiography or Ultrasonic are performed before Hardness",
#     IT_CODE:
#         "Radiografia o Ultrasuoni eseguiti prima delle misure di durezza",
# }
note_rc_lt_hb = {
    RU_CODE: "РК или УЗК проведено раньше замеров твердости; ",
    GB_CODE: "Radiography or Ultrasonic are performed before Hardness",
    IT_CODE:
        "Radiografia o Ultrasuoni eseguiti prima delle misure di durezza",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше стилоскопирования; ",
#     GB_CODE: "Radiography or Ultrasound are performed before Styloscopy",
#     IT_CODE: "Radiografia o Ultrasuoni eseguiti prima della Stiloscopia",
# }
note_rc_lt_st = {
    RU_CODE: "РК или УЗК проведено раньше стилоскопирования; ",
    GB_CODE: "Radiography or Ultrasound are performed before Styloscopy",
    IT_CODE: "Radiografia o Ultrasuoni eseguiti prima della Stiloscopia",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше ВИК; ",
#     GB_CODE: "Color flaw detection is performed before visual control",
#     IT_CODE: "Difetti di colore eseguiti prima del controllo visivo",
# }
note_cd_lt_vmc = {
    RU_CODE: "ЦД проведена раньше ВИК; ",
    GB_CODE: "Color flaw detection is performed before visual control",
    IT_CODE: "Difetti di colore eseguiti prima del controllo visivo",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров твердости; ",
#     GB_CODE: "Color flaw detection is performed before hardness",
#     IT_CODE: "Difetti di colore eseguiti prima delle misure di durezza",
# }
note_cd_lt_hb = {
    RU_CODE: "ЦД проведена раньше замеров твердости; ",
    GB_CODE: "Color flaw detection is performed before hardness",
    IT_CODE: "Difetti di colore eseguiti prima delle misure di durezza",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров стилоскопирования; ",
#     GB_CODE: "Color flaw detection is performed before Styloscopy",
#     IT_CODE: "Difetti di colore eseguiti prima della Stiloscopia",
# }
note_cd_lt_st = {
    RU_CODE: "ЦД проведена раньше замеров стилоскопирования; ",
    GB_CODE: "Color flaw detection is performed before Styloscopy",
    IT_CODE: "Difetti di colore eseguiti prima della Stiloscopia",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров РК или УЗК; ",
#     GB_CODE:
#         "Color flaw detection is performed before Radiography or Ultrasound",
#     IT_CODE: "Difetti di colore eseguiti prima dei Radiografia e Ultrasuoni",
# }
note_cd_lt_rc = {
    RU_CODE: "ЦД проведена раньше замеров РК или УЗК; ",
    GB_CODE:
        "Color flaw detection is performed before Radiography or Ultrasound",
    IT_CODE: "Difetti di colore eseguiti prima dei Radiografia e Ultrasuoni",
}
# Default:
# {
#     RU_CODE: "Дата ВИК не указана!",
#     GB_CODE: "The date of visual control is not specified!",
#     IT_CODE: "Nessuna data di controllo visivo specificata!",
# }
note_vmc_does_not_exist = {
    RU_CODE: "Дата ВИК не указана!",
    GB_CODE: "The date of visual control is not specified!",
    IT_CODE: "Nessuna data di controllo visivo specificata!",
}

"""
==============================================================================
"""

"""
=====================Константы и переменные логирования=======================
"""

# =====================Статические сообщения для логов========================

# Информирует о начале выполнения логики.
# Default:
# {
#     RU_CODE: "Начало выполнения логики",
#     GB_CODE: "The beginning of logic execution",
#     IT_CODE: "Inizio dell'esecuzione della logica",
# }
log_start = {
    RU_CODE: "Начало выполнения логики",
    GB_CODE: "The beginning of logic execution",
    IT_CODE: "Inizio dell'esecuzione della logica",
}

# Информирует о вызове метода App.calculate_dates
# Default:
# {
#     RU_CODE: "Вызов метода App.calculate_dates",
#     GB_CODE: "Calling the App.calculate_dates method",
#     IT_CODE: "Chiamare il metodo App.calculate_dates",
# }
log_calculate_dates_call = {
    RU_CODE: "Вызов метода App.calculate_dates",
    GB_CODE: "Calling the App.calculate_dates method",
    IT_CODE: "Chiamare il metodo App.calculate_dates",
}

# Информирует о вызове метода App.handle_request
# Default:
# {
#     RU_CODE: "Вызов метода App.handle_request",
#     GB_CODE: "Calling the App.handle_request method",
#     IT_CODE: "Chiamare il metodo App.handle_request",
# }
log_handle_request_call = {
    RU_CODE: "Вызов метода App.handle_request",
    GB_CODE: "Calling the App.handle_request method",
    IT_CODE: "Chiamare il metodo App.handle_request",
}

# Информирует об ошибке в программе без конкретизации
# Default:
# {
#     RU_CODE: "Обработка завершилась с ошибкой",
#     GB_CODE: "Processing failed with an error",
#     IT_CODE: "L'elaborazione non è riuscita con un errore",
# }
log_error_msg = {
    RU_CODE: "Обработка завершилась с ошибкой",
    GB_CODE: "Processing failed with an error",
    IT_CODE: "L'elaborazione non è riuscita con un errore",
}

# Информирует о начале проверки файлов
# Default:
# {
#     RU_CODE: "Начало проверки файлов",
#     GB_CODE: "Start files check",
#     IT_CODE: "Inizio del controllo dei file",
# }
log_check_files_start = {
    RU_CODE: "Начало проверки файлов",
    GB_CODE: "Start files check",
    IT_CODE: "Inizio del controllo dei file",
}

# Информирует о вызове метода check_files
# Default:
# {
#     RU_CODE: "Вызов метода check_files",
#     GB_CODE: "Calling check_files method",
#     IT_CODE: "Chiamare il metodo check_files",
# }
log_check_files_call = {
    RU_CODE: "Вызов метода check_files",
    GB_CODE: "Calling check_files method",
    IT_CODE: "Chiamare il metodo check_files",
}

# Информирует об окончании проверки check_files
# Default:
# {
#     RU_CODE: "Проверка выполнена",
#     GB_CODE: "Checking is completed",
#     IT_CODE: "Verifica eseguita",
# }
log_check_files_done = {
    RU_CODE: "Проверка выполнена",
    GB_CODE: "Checking is completed",
    IT_CODE: "Verifica eseguita",
}

# Информирует начале парсинга
# Default:
# {
#     RU_CODE: "Начало парсинга предоставленных файлов",
#     GB_CODE: "Start parsing",
#     IT_CODE: "Inizio del parsing",
# }
log_parse_start = {
    RU_CODE: "Начало парсинга предоставленных файлов",
    GB_CODE: "Start parsing",
    IT_CODE: "Inizio del parsing",
}

# Информирует вызове метода parser.parse_weld_data
# Default:
# {
#     RU_CODE: "Вызов метода parser.parse_weld_data",
#     GB_CODE: "Calling parser.parse_weld_data method",
#     IT_CODE: "Chiamare il metodo parser.parse_weld_data",
# }
log_parse_call = {
    RU_CODE: "Вызов метода parser.parse_weld_data",
    GB_CODE: "Calling parser.parse_weld_data method",
    IT_CODE: "Chiamare il metodo parser.parse_weld_data",
}

# Информирование о начале создания итоговой таблицы
# Default:
# {
#     RU_CODE: "Начало составления итоговой таблицы",
#     GB_CODE: "Starting summary table creation",
#     IT_CODE: "Avvio della creazione della tabella riassuntiva",
# }
log_table_start = {
    RU_CODE: "Начало составления итоговой таблицы",
    GB_CODE: "Starting summary table creation",
    IT_CODE: "Avvio della creazione della tabella riassuntiva",
}

# Информирует о вызове метода create_summary.create_summary_excel
# Default:
# {
#     RU_CODE: "Вызов метода create_summary.create_summary_excel",
#     GB_CODE: "Calling CreateSummary.create_summary_excel method",
#     IT_CODE: "Chiamare il metodo CreateSummary.create_summary_excel",
# }
log_table_method_call = {
    RU_CODE: "Вызов метода create_summary.create_summary_excel",
    GB_CODE: "Calling CreateSummary.create_summary_excel method",
    IT_CODE: "Chiamare il metodo CreateSummary.create_summary_excel",
}

# Информирует о создании итоговой таблицы
# Default:
# {
#     RU_CODE: "Таблица составлена",
#     GB_CODE: "The table is done",
#     IT_CODE: "La tabella è fatta",
# }
log_table_done = {
    RU_CODE: "Таблица составлена",
    GB_CODE: "The table is done",
    IT_CODE: "La tabella è fatta",
}

# Информирует о запуске процесса создания итоговой таблицы
# Default:
# {
#     RU_CODE: "Создаем основу",
#     GB_CODE: "Create the base",
#     IT_CODE: "Crea una base",
# }
log_table_creating = {
    RU_CODE: "Создаем основу",
    GB_CODE: "Create the base",
    IT_CODE: "Creare una base",
}

# Информирует о добавлении заголовков в итоговую таблицу
# Default:
# {
#     RU_CODE: "Создаем заголовки",
#     GB_CODE: "Create headers",
#     IT_CODE: "Creare titoli",
# }
log_add_headers = {
    RU_CODE: "Создаем заголовки",
    GB_CODE: "Create headers",
    IT_CODE: "Creare titoli",
}

# Информирует о добавлении данных в итоговую таблицу
# Default:
# {
#     RU_CODE: "Записываем данные...",
#     GB_CODE: "Recording the data...",
#     IT_CODE: "Registriamo i dati...",
# }
log_add_data = {
    RU_CODE: "Записываем данные...",
    GB_CODE: "Recording the data...",
    IT_CODE: "Registriamo i dati...",
}

# Информирует о добавлении данных в итоговую таблицу
# Default:
# {
#     RU_CODE: "Данные записаны",
#     GB_CODE: "The data is recorded",
#     IT_CODE: "I dati sono registrati",
# }
log_data_added = {
    RU_CODE: "Данные записаны",
    GB_CODE: "The data is recorded",
    IT_CODE: "I dati sono registrati",
}

# Информирует о сохранении итоговой таблицы
# Default:
# {
#     RU_CODE: "Таблица сохранена",
#     GB_CODE: "The table is saved",
#     IT_CODE: "La tabella è salvata",
# }
log_table_saved = {
    RU_CODE: "Таблица сохранена",
    GB_CODE: "The table is saved",
    IT_CODE: "La tabella è salvata",
}

# Информирует о том, куда будет сохранен итоговый файл
# Default:
# {
#     RU_CODE: "Путь для сохранения итогового файла: ",
#     GB_CODE: "Final table save path is: ",
#     IT_CODE: "Percorso per salvare il file finale: ",
# }
log_save_path_is = {
    RU_CODE: "Путь для сохранения итогового файла: ",
    GB_CODE: "Final table save path is: ",
    IT_CODE: "Percorso per salvare il file finale: ",
}

# Информирует, что парсинг выполнен и указывает количество элементов.
# {
#     RU_CODE: "Парсинг выполнен. Количесвто элементов: ",
#     GB_CODE: "Parsing is done. Elements amount is : ",
#     IT_CODE: "Parsing è fatta. Numero di elementi: ",
# }
log_parse_done_el_amount = {
    RU_CODE: "Парсинг выполнен. Количесвто элементов: ",
    GB_CODE: "Parsing is done. Elements amount is : ",
    IT_CODE: "Parsing è fatta. Numero di elementi: ",
}

# Информирует о том, что файл не на своем месте и показывает, что это
# за файл и куда был загружен.
# {
#     RU_CODE: "Файл не на своем месте: {} загружен для поля {}",
#     GB_CODE: "The file isn't at his place: {} is loaded for the field {}",
#     IT_CODE: "Il file non è al suo posto: {} è caricato per il campo {}"
# }
log_check_failed_error = {
    RU_CODE: "Файл не на своем месте: {} загружен для поля {}",
    GB_CODE: "The file isn't at his place: {} is loaded for the field {}",
    IT_CODE: "Il file non è al suo posto: {} è caricato per il campo {}"
}

# Информирует о том, что у загруженного файла недопустимое расширение.
# {
#     RU_CODE: "Файл с недопустимым расширением: ",
#     GB_CODE: "File with unacceptable extension: ",
#     IT_CODE: "File con estensione non valida: ",
# }
log_unacceptable_extension = {
    RU_CODE: "Файл с недопустимым расширением: ",
    GB_CODE: "File with unacceptable extension: ",
    IT_CODE: "File con estensione non valida: ",
}

# Информирует о выбранных файлах:
# Default:
# {
#     RU_CODE: "Выбранные файлы: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
#     GB_CODE: "Chosen files: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
#     IT_CODE: "I file scelti: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
# }
log_chosen_files = {
    RU_CODE: "Выбранные файлы: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
    GB_CODE: "Chosen files: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
    IT_CODE: "I file scelti: VMC: {}, RC: {}, ST: {}, CD: {}, HB: {}",
}

# Информирует о том, куда сохраняем таблицу
# Default:
# {
#     RU_CODE: "Сохраняем таблицу в {}",
#     GB_CODE: "Save table to {}",
#     IT_CODE: "Salvare la tabella in {}",
# }
log_save_table_to = {
    RU_CODE: "Сохраняем таблицу в {}",
    GB_CODE: "Save table to {}",
    IT_CODE: "Salvare la tabella in {}",
}

"""
==============================================================================
"""

"""
##############################################################################
##############################################################################
##############################################################################
####################                                     #####################
####################         Остальные настройки         #####################
####################          The other settings         #####################
####################        Le altre impostazioni        #####################
####################                                     #####################
##############################################################################
##############################################################################
##############################################################################
"""


"""
================Константы и переменные графического интерфейса================
"""
# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================     Основные окна      ==========================
# ============================================================================

# Имя Главного окна
# Default: "Dates Control - v1.0.0"
START_WINDOW_TITLE = "Dates Control - v1.0.0"

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

# =========================Настройки для InfoWindow===========================
# Это окно вылезает, когда начинается процесс обработки файлов и предупреждает
# юзера, что работа пошла, чтобы юзер не подумал, что приложение зависло.

# Ширина инфобокса
INFO_WINDOW_WIDTH = 300  # Default: 200

# Высота инфобокса
INFO_WINDOW_HEIGHT = 100  # Default: 100

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Фреймы         ==========================
# ============================================================================

# =======================Настройки для фрейма ввода пути======================
# Содержат лейбл, поле для ввода и кнопку

# Выбор оси, по которой будет растягивание фрейма (лучше не менять
# этот параметр)
FRAME_FILL_AXIS = 'x'  # Default: 'x'

# Отступы от краев по горизонтали
# Поскольку заполнение по умолчанию будет на весь размер окна по ширине,
# то отступы будут с обеих сторон
FRAME_PADX = 20  # Default: 20

# ==================Настройки для фрейма разделительной строки================
# Строка идет после каждого фрейма и нужна для отделения фреймов
# друг от друга, чтобы они не сливались

# Высота разделительной строки
DIVIDER_HEIGHT = 10  # Default: 5

# Выбор оси, по которой будет растягивание разделителя
# (лучше не менять этот параметр)

DIVIDER_FILL_AXIS = 'x'  # Default 'x'

# =======================Настройки для фрейма и кнопок========================
# Фрейм, который используется для расположения кнопок внизу

# Отступы для фрейма по вертикали в пикселях
BUTTONS_FRAME_PADY = 10  # Default: 10

# ====================Настройки для фрейма основных кнопок====================

# Отступ от края по вертикали сверху и снизу
SETTINGS_BUTTONS_FRAME_PADY = 20

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Кнопки         ==========================
# ============================================================================

# ===============================Общие настройки==============================
# Ширина кнопок фрейма по умолчанию (в количестве вмещаемых символов)
BUTTONS_WIDTH = 15  # Default: 15

# =========================Настройки для кнопки "Обзор"=======================

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

# =================Настройки для кнопок фрейма окна настроек==================

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

# =====================Расположение кнопок внутри фрейма======================

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

# =========================Найстройки языковых кнопок=========================
lang = {
    RU_CODE: RU_ICON_PATH,
    GB_CODE: GB_ICON_PATH,
    IT_CODE: IT_ICON_PATH
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Лейблы         ==========================
# ============================================================================

# =======================Настройки для Лейбла Авторства=======================

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

# ==================Настройки для Лейбла информационного окна=================

# Отступ по краям окна по горизонтали
INFO_LABEL_PADX = 20  # Default: 20

# Отступ по краям окна по вертикали
INFO_LABEL_PADY = 20  # Default: 20

# ===================Настройки для лейблов стартового окна====================

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
# Default: ["визуальн", "visual", "visiv"]
VMC_CHECK_KEYS = ["визуальн", "visual", "visiv"]

# Ключ для проверки протоколов замеров твердости
# Default: ["твердост", "твёрдост", "hardness", "durezz"]
HB_CHECK_KEYS = ["твердост", "твёрдост", "hardness", "durezz"]

# Ключ для проверки протоколов радиографического контроля (РК или УЗК)
# Default:
# [
#     "радиограф",
#     "ультразвук",
#     "radiograph",
#     "radiograf",
#     "ultrason",
#     "ultrasuon"
# ]
RC_CHECK_KEYS = [
    "радиограф",
    "ультразвук",
    "radiograph",
    "radiograf",
    "ultrason",
    "ultrasuon"
]

# Ключ для проверки протоколов стилоскопирования (СТ)
# Default: ["флуоресцент", "styloscop"]
ST_CHECK_KEYS = ["флуоресцент", "styloscop"]

# Ключ для проверки протоколов цветной дефектоскопии (ЦД)
CD_CHECK_KEYS = ["капилляр", "color"]  # Default: ["капилляр", "color"]

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

# Ключ для словаря files_dict значением которого является путь к файлу контроля
FILES_DICT_PATH_KEY = 'path'  # Default: 'path'

# Ключ для словаря files_dict значением которого являются ключи для проверки
# файлов контроля
FILES_DICT_CHECK_KEY = 'check'  # Default: 'check'

# =============================Остальные настройки============================

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

# ===========================Настройки для parser.py==========================

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

# =======================Настройки для create_summary.py======================

# Дефолтное значение ячейки в столбце с примечаниями:
NOTE = ""  # Default: ""

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

# =======================Статические сообщения для логов======================

# Разделитель между логами разных процессов
# Default: "******************************************************"
LOG_DIVIDER = "******************************************************"

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

"""
Здесь все настройки приложения.
Here are all the application settings.
Qui tutte le impostazioni dell'applicazione.
"""
import os

# Код языка РФ.
# ****************************************************************************
# RF language code.
# ****************************************************************************
# Codice della lingua della Federazione Russa.
# ****************************************************************************
RU_CODE = 'ru'  # Default: 'ru'

# Код языка Великобритании.
# ****************************************************************************
# Great Britain language code.
# ****************************************************************************
# Codice della lingua del Regno Unito.
# ****************************************************************************
GB_CODE = 'gb'  # Default: 'gb'

# Код языка Италии.
# ****************************************************************************
# Italy language code.
# ****************************************************************************
# Codice della lingua dell'Italia.
# ****************************************************************************
IT_CODE = 'it'  # Default: 'it'

# Список доступных кодов.
# Сюда добавлять все константы кодов выше.
# ****************************************************************************
# Available codes list.
# Here to put all the code constants from above.
# ****************************************************************************
# Elenco dei codici disponibili.
# Aggiungere qui tutte le costanti dei codici sopra.
# ****************************************************************************
#
# Default: [RU_CODE, GB_CODE, IT_CODE]
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
================Constants & variables of the graphic interface================
================Costanti e variabili dell'interfaccia grafica=================
"""
# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================     Основные окна      ==========================
# ==========================        WINDOWS         ==========================
# ==========================    Primary windows     ==========================
# ==========================        FINESTRE        ==========================
# ==========================    Finestre primarie   ==========================
# ============================================================================

# Имя окна настроек.
# ****************************************************************************
# Settings window title.
# ****************************************************************************
# Titolo della finestra delle impostazioni.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Настройки",
#     GB_CODE: "Settings",
#     IT_CODE: "Impostazioni",
# }
settings_window_title = {
    RU_CODE: "Настройки",
    GB_CODE: "Settings",
    IT_CODE: "Impostazioni",
}

# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================  Второстепенные окна   ==========================
# ==========================        WINDOWS         ==========================
# ==========================   Secondary windows    ==========================
# ==========================        FINESTRE        ==========================
# ==========================  Finestre secondarie   ==========================
# ============================================================================

# =====================Настройки для окна выбора языка========================
# ===========================Lang window settings=============================
# =================Impostazioni per la finestra delle lingue==================

# Заголовок окна выбора языка
# ****************************************************************************
# Language window title.
# ****************************************************************************
# Titolo della finestra delle lingue.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: 'Выбор языка',
#     GB_CODE: 'Language choices',
#     IT_CODE: 'Shelta della lingua',
# }
lang_window_title = {
    RU_CODE: 'Выбор языка',
    GB_CODE: 'Language choices',
    IT_CODE: 'Shelta della lingua',
}

# =========================Настройки для MessageBox===========================
# ============================MessageBox settings=============================
# =======================Impostazioni per MessageBox==========================

# Заголовок окна об ошибке.
# ****************************************************************************
# Error window title.
# ****************************************************************************
# Titolo della finestra di errore.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Ошибка",
#     GB_CODE: "Error",
#     IT_CODE: "Errore",
# }
error_message_title = {
    RU_CODE: "Ошибка",
    GB_CODE: "Error",
    IT_CODE: "Errore",
}

# =========================Настройки для InfoWindow===========================
# ===========================InfoWindow settings==============================
# =======================Impostazioni per InfoWindow==========================
# Это окно вылезает, когда начинается процесс обработки файлов и предупреждает
# юзера, что работа пошла, чтобы юзер не подумал, что приложение зависло.
# ****************************************************************************
# This window pops up when the file processing begins to inform the users that
# the process has started, so they don't think the application has frozen.
# ****************************************************************************
# Questa finestra appare quando inizia il processo di elaborazione dei file e
# avverte l'utente che il lavoro è iniziato, per evitare che pensi che
# l'applicazione si sia bloccata.
# ****************************************************************************

# Заголовок инфобокса.
# ****************************************************************************
# Info window title.
# ****************************************************************************
# Titolo dell'InfoBox.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Для справки!",
#     GB_CODE: "For your information!",
#     IT_CODE: "Per l'informazione",
# }
info_window_title = {
    RU_CODE: "Для справки!",
    GB_CODE: "For your information!",
    IT_CODE: "Per l'informazione",
}

# ==================Настройки информационных окон об успехе===================
# =======================Success info window settings=========================
# ===========Impostazioni delle finestre informative sul successo=============

# Заголовок окна об успехе.
# ****************************************************************************
# Success info window title.
# ****************************************************************************
# Titolo della finestra di successo.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Успех!",
#     GB_CODE: "Success!",
#     IT_CODE: "Successo!",
# }
success_title = {
    RU_CODE: "Успех!",
    GB_CODE: "Success!",
    IT_CODE: "Successo!",
}

# Сообщение окна об успехе сохранения файла настроек.
# ****************************************************************************
# Info window message abot successful saving the settings file.
# ****************************************************************************
# Messaggio della finestra di successo per il salvataggio del file di
# configurazione.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Настройки сохранены!",
#     GB_CODE: "The settings are saved!",
#     IT_CODE: "Impostazioni salvate!",
# }
saved_settings_success_message = {
    RU_CODE: "Настройки сохранены!",
    GB_CODE: "The settings are saved!",
    IT_CODE: "Le impostazioni sono salvate!",
}

# Сообщение окна об успехе сохранения итоговой таблицы.
# ****************************************************************************
# Info window message about saving the summary table.
# ****************************************************************************
# Messaggio della finestra di successo per il salvataggio della tabella
# finale.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Итоговая таблица сохранена в {}",
#     GB_CODE: "The final table is saved in {}",
#     IT_CODE: "La tabella finale è salvata in {}",
# }
saved_file_success_message = {
    RU_CODE: "Итоговая таблица сохранена в {}",
    GB_CODE: "The final table is saved in {}",
    IT_CODE: "La tabella finale è salvata in {}",
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Кнопки         ==========================
# ==========================       COMPONENTS       ==========================
# ==========================        Buttons         ==========================
# ==========================       COMPONENTI       ==========================
# ==========================        Pulsanti        ==========================
# ============================================================================

# ========================Настройки для кнопки "Обзор"========================
# ========================="Browse" button settings===========================
# =================Impostazioni per il pulsante "Navigazione"=================

# Название кнопки.
# ****************************************************************************
# Button name.
# ****************************************************************************
# Nome del pulsante.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Обзор",
#     GB_CODE: "Browse",
#     IT_CODE: "Navigazione",
# }
browse_button_name = {
    RU_CODE: "Обзор",
    GB_CODE: "Browse",
    IT_CODE: "Navigazione",
}

# =================Настройки для кнопок фрейма окна настроек==================
# =======================Settings_window frame settings=======================
# =======Impostazioni per i pulsanti della finestra delle impostazioni========

# Имя кнопки для сохранения.
# ****************************************************************************
# Save button name.
# ****************************************************************************
# Nome del pulsante per il salvataggio.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Сохранить",
#     GB_CODE: "Save",
#     IT_CODE: "Salvare",
# }
save_button_name = {
    RU_CODE: "Сохранить",
    GB_CODE: "Save",
    IT_CODE: "Salvare",
}

# Имя кнопки для отмены.
# ****************************************************************************
# Cancel button name.
# ****************************************************************************
# Nome del pulsante per l'annullamento.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Отмена",
#     GB_CODE: "Cancel",
#     IT_CODE: "Annullare",
# }
cancel_button_name = {
    RU_CODE: "Отмена",
    GB_CODE: "Cancel",
    IT_CODE: "Annullare",
}

# Текст, отображаемый на кнопках окна настроек.
# И процесс, запускаемый для каждой кнопки.
# ****************************************************************************
# Button text displayed in the settings window.
# And the process triggered by each button.
# ****************************************************************************
# Testo visualizzato sui pulsanti della finestra delle impostazioni.
# E il processo attivato da ciascun pulsante.
# ****************************************************************************
#
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

# ===================Настройки фрейма кнопок стартового окна==================
# =====================Start window buttons frame settings====================
# ========Impostazioni del frame dei pulsanti della finestra principale=======

# Имя кнопки для запуска процесса обработки файлов.
# ****************************************************************************
# Run files handling button name.
# ****************************************************************************
# Nome del pulsante per avviare il processo di elaborazione dei file.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Погнали",
#     GB_CODE: "Run",
#     IT_CODE: "Vai",
# }
go_button_name = {
    RU_CODE: "Погнали",
    GB_CODE: "Run",
    IT_CODE: "Vai",
}

# Имя кнопки для очистки всех текстовых полей.
# ****************************************************************************
# Clear textfields button name.
# ****************************************************************************
# Nome del pulsante per cancellare tutti i campi di testo.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Забить",
#     GB_CODE: "Clear",
#     IT_CODE: "Cancellare",
# }
clear_button_name = {
    RU_CODE: "Забить",
    GB_CODE: "Clear",
    IT_CODE: "Cancellare",
}

# Имя кнопки для открытия окна настроек.
# ****************************************************************************
# Open settings window button name.
# ****************************************************************************
# Nome del pulsante per aprire la finestra delle impostazioni.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Настройки",
#     GB_CODE: "Settings",
#     IT_CODE: "Impostazioni",
# }
settings_button_name = {
    RU_CODE: "Настройки",
    GB_CODE: "Settings",
    IT_CODE: "Impostazioni",
}

# Текст, отображаемый на кнопках стартового окна.
# И процесс, запускаемый для каждой кнопки.
# ****************************************************************************
# Button text displayed in the start window.
# And the process triggered by each button.
# ****************************************************************************
# Testo visualizzato sui pulsanti della finestra principale.
# E il processo attivato da ciascun pulsante.
# ****************************************************************************
#
# Default:
# {
#     code: {
#         go_button_name[code]: "start_process",
#         clear_button_name[code]: "clear_entries",
#         settings_button_name[code]: "open_settings",
#     }
#     for code in LANG_CODES
# }
start_buttons_name_to_process = {
    code: {
        go_button_name[code]: "start_process",
        clear_button_name[code]: "clear_entries",
        settings_button_name[code]: "open_settings",
    }
    for code in LANG_CODES
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Лейблы         ==========================
# ==========================       COMPONENTS       ==========================
# ==========================         Labels         ==========================
# ==========================       COMPONENTI       ==========================
# ==========================        Etichette       ==========================
# ============================================================================

# =================Настройки для Лейбла информационного окна==================
# =========================Info window label settings=========================
# ===========Impostazioni per l'etichetta della finestra informativa==========

# Текст информационного сообщения.
# ****************************************************************************
# Info message text.
# ****************************************************************************
# Testo del messaggio informativo.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Работа пошла.\nПодожди немного!",
#     GB_CODE: "The work has started.\nWait a bit!",
#     IT_CODE: "Il lavoro è iniziato.\nAspetta un attimo!",
# }
info_label_text = {
    RU_CODE: "Работа пошла.\nПодожди немного!",
    GB_CODE: "The work has started.\nWait a bit!",
    IT_CODE: "Il lavoro è iniziato.\nAspetta un attimo!",
}

# ====================Настройки лейбла для окна настроек======================
# ======================Settings_window label settings========================
# =======Impostazioni per l'etichetta della finestra delle impostazioni=======

# Текст для лейбла окна настроек.
# ****************************************************************************
# Settings window label text.
# ****************************************************************************
# Testo per l'etichetta della finestra delle impostazioni.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Куда сохранять итоговый файл?",
#     GB_CODE: "Where should I save the final file?",
#     IT_CODE: "Dove salvare il file finale?",
# }
where_to_save = {
    RU_CODE: "Куда сохранять итоговый файл?",
    GB_CODE: "Where should I save the final file?",
    IT_CODE: "Dove salvare il file finale?",
}

# ===================Настройки для лейблов стартового окна====================
# ========================Start_window label settings=========================
# ==========Impostazioni per le etichette della finestra principale===========

# Тексты для лейблов (описание, какой файл необходимо выбрать).
# Будут расположены в том же порядке, в котором перечислены в списке.
# Порядок лучше не менять, иначе все по пизде пойдет.
# Это будет исправлено в будущем.
# ****************************************************************************
# Labels for file descriptions (indicating which file needs to be selected).
# They will be listed in the same order as in the list.
# It’s better not to change the order, or everything will go to hell.
# This will be fixed in the future.
# ****************************************************************************
# Testi per le etichette (descrizione del file da selezionare).
# Saranno visualizzati nello stesso ordine in cui sono elencati.
# Meglio non cambiare l'ordine, altrimenti va tutto a rotoli.
# Questo sarà sistemato in futuro.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: [
#         "Выбери файлы Визуального контроля",
#         "Выбери файлы Радиографического контроля",
#         "Выбери файлы Стилоскопирования",
#         "Выбери файлы Цветной дефектоскопии",
#         "Выбери файлы Твердости",
#     ],
#     GB_CODE: [
#         "Select Visual Inspection files",
#         "Select Radiographic Inspection files",
#         "Select Styloscopy files",
#         "Select the Color Flaw detection files",
#         "Select the Hardness measurement files",
#     ],
#     IT_CODE: [
#         "Scegli i file di controllo visivo",
#         "Scegli i file di controllo radiografico",
#         "Scegli i file di Styloscoping",
#         "Scegli i file di rilevamento dei difetti A Colori",
#         "Scegli i file di misurazione della durezza",
#     ],
# }
labels = {
    RU_CODE: [
        "Выбери файлы Визуального контроля",
        "Выбери файлы Радиографического контроля",
        "Выбери файлы Стилоскопирования",
        "Выбери файлы Цветной дефектоскопии",
        "Выбери файлы Твердости",
    ],
    GB_CODE: [
        "Select Visual Inspection files",
        "Select Radiographic Inspection files",
        "Select Styloscopy files",
        "Select the Color Flaw detection files",
        "Select the Hardness measurement files",
    ],
    IT_CODE: [
        "Scegli i file di controllo visivo",
        "Scegli i file di controllo radiografico",
        "Scegli i file di Styloscoping",
        "Scegli i file di rilevamento dei difetti A Colori",
        "Scegli i file di misurazione della durezza",
    ],
}

"""
========================Константы и переменные логики=========================
=====================Constants & variables of the logic=======================
=====================Costanti e variabili della logica========================
"""
# =========================Настройки для get_xlsx.py==========================
# ============================get_xlsx.py settings============================
# ====================== Impostazioni per get_xlsx.py=========================

# Сообщение о том, что приложение закроется.
# ****************************************************************************
# Message about closing the App.
# ****************************************************************************
# Messaggio che indica che l'applicazione si chiuderà.
# ****************************************************************************
#
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

# Сообщение о том, что загружен файл с непонятным разрешением.
# ****************************************************************************
# Unnknown file extension message.
# ****************************************************************************
# Messaggio che indica che è stato caricato un file con un'estensione
# sconosciuta.
# ****************************************************************************
#
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

# Сообщает, что файл находится не в нужном поле.
# ****************************************************************************
# Message about the wrong place for a file.
# ****************************************************************************
# Indica che il file si trova nel campo sbagliato.
# ****************************************************************************
#
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

# Сообщает о неотслеженной ошибке при проверке файла.
# ****************************************************************************
# Message about an untracked error while checking a file.
# ****************************************************************************
# Segnala un errore non gestito durante la verifica del file.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Ошибка при проверке файла {}: {}",
#     GB_CODE: "File check error {}: {}",
#     IT_CODE: "Errore durante la convalida del file {}: {}",
# }
file_check_error = {
    RU_CODE: "Ошибка при проверке файла {}: {}",
    GB_CODE: "File check error {}: {}",
    IT_CODE: "Errore durante la convalida del file {}: {}",
}

# ==========================Настройки для parser.py===========================
# ============================parser.py settings==============================
# ========================Impostazioni per parser.py==========================

# Регулярное выражение для поиска номера шва. Обычно название шва состоит из
# одной буквы кириллицы, означающей тип шва и случайного набора чисел,
# чередующихся с дефисами.
# ****************************************************************************
# The regexp for the welding joint id searching. Usually joint id is a capital
# letter and random number of the numbers with dashes.
# ****************************************************************************
# Espressione regolare per cercare il numero di giunto. Di solito, il nome del
# giunto consiste in una lettera cirillica che rappresenta il tipo di giunto e
# una sequenza casuale di numeri alternati con trattini.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: r'^[CYTNHСНТУ][-\d]*$',
#     GB_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
#     IT_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
# }
joint_id_regexp = {
    RU_CODE: r'^[CYTNHСНТУ][-\d]*$',
    GB_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
    IT_CODE: r'^[a-zA-ZСНТУ][-\d]*$',
}

# =======================Настройки для create_summary.py======================
# =========================create_summary.py settings=========================
# =====================Impostazioni per create_summary.py=====================

# Имена колонок для генерируемой таблицы.
# Лучше не добавлять и не удалять колонки, а то все по пизде пойдет.
# Но переименовывать можно. В будущем исправлю.
# ****************************************************************************
# Column names for the generated table.
# It’s better not to add or delete new columns, or everything will go to hell.
# But renaming is fine. I’ll fix this in the future.
# ****************************************************************************
# Nomi delle colonne per la tabella generata.
# È meglio non aggiungere o rimuovere colonne, altrimenti va tutto a rotoli.
# Ma si possono rinominare. Questo sarà sistemato in futuro.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: [
#         "Номер шва",
#         "ВИК",
#         "Твёрдость",
#         "Стилоскопирование",
#         "РК или УЗК",
#         "ЦД",
#         "Примечания",
#     ],
#     GB_CODE: [
#         "Joint id",
#         "Visual",
#         "Hardness",
#         "Styloscopy",
#         "Radioghraph or Ultrasonic",
#         "Color",
#         "Notes",
#     ],
#     IT_CODE: [
#         "Id saldatura",
#         "Visivo",
#         "Durezza",
#         "Stiloscopia",
#         "Radiografia o ultrasuoni",
#         "Colore",
#         "Nota",
#     ],
# }
headers = {
    RU_CODE: [
        "Номер шва",
        "ВИК",
        "Твёрдость",
        "Стилоскопирование",
        "РК или УЗК",
        "ЦД",
        "Примечания",
    ],
    GB_CODE: [
        "Joint id",
        "Visual",
        "Hardness",
        "Styloscopy",
        "Radioghraph or Ultrasonic",
        "Color",
        "Notes",
    ],
    IT_CODE: [
        "Id saldatura",
        "Visivo",
        "Durezza",
        "Stiloscopia",
        "Radiografia o ultrasuoni",
        "Colore",
        "Nota",
    ],
}

# Ниже значения, которые мы будем дописывать в note, когда какая-то из дат
# прописана неверно. Название констант будет составляться так:
# note_<тип_контроля>_LT(less_than)_<другой_тип_контроля>, что означает,
# что контроль <тип_контроля> проведен раньше, чем <другой_тип_контроля>,
# что является ошибкой и такого быть не должно.
# ****************************************************************************
# Values below will be added to the note when any of the dates are incorrect.
# Constant names will be constructed as follows:
# note_<control_type>_LT(less_than)_<other_control_type>, indicating that
# <control_type> was completed before <other_control_type>, which is an error
# and should not happen.
# ****************************************************************************
# Valori che verranno aggiunti alla nota quando una delle date è errata.
# I nomi delle costanti saranno formati come segue:
# note_<tipo_di_controllo>_LT(less_than)_<altro_tipo_di_controllo>, il che
# significa che il controllo <tipo_di_controllo> è stato eseguito prima di
# <altro_tipo_di_controllo>, il che è un errore e non dovrebbe accadere.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: "Замер твердости проведен раньше ВИК; ",
#     GB_CODE: "Hardness measurement is carried out before visual control; ",
#     IT_CODE:
#         "Misurazione della durezza eseguita prima del controllo visivo; ",
# }
note_hb_lt_vmc = {
    RU_CODE: "Замер твердости проведен раньше ВИК; ",
    GB_CODE: "Hardness measurement is carried out before visual control; ",
    IT_CODE:
        "Misurazione della durezza eseguita prima del controllo visivo; ",
}
# Default:
# {
#     RU_CODE: "Стилоскопирование проведено раньше ВИК; ",
#     GB_CODE: "Styloscopy is performed before visual control; ",
#     IT_CODE: "Stiloscopia eseguita prima del controllo visivo; ",
# }
note_st_lt_vmc = {
    RU_CODE: "Стилоскопирование проведено раньше ВИК; ",
    GB_CODE: "Styloscopy is performed before visual control; ",
    IT_CODE: "Stiloscopia eseguita prima del controllo visivo; ",
}
# Default:
# {
#     RU_CODE: "Стилоскопирование проведено раньше замеров твердости; ",
#     GB_CODE: "Styloscopy is performed before hardness measurements; ",
#     IT_CODE: "Stiloscopia eseguita prima delle misure di durezza; ",
# }
note_st_lt_hb = {
    RU_CODE: "Стилоскопирование проведено раньше замеров твердости; ",
    GB_CODE: "Styloscopy is performed before hardness measurements; ",
    IT_CODE: "Stiloscopia eseguita prima delle misure di durezza; ",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше ВИК; ",
#     GB_CODE:
#         "Radiography or Ultrasonic are performed before visual control; ",
#     IT_CODE:
#         "Radiografia o Ultrasuoni eseguiti prima del controllo visivo; ",
# }
note_rc_lt_vmc = {
    RU_CODE: "РК или УЗК проведено раньше ВИК; ",
    GB_CODE:
        "Radiography or Ultrasonic are performed before visual control; ",
    IT_CODE:
        "Radiografia o Ultrasuoni eseguiti prima del controllo visivo; ",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше замеров твердости; ",
#     GB_CODE: "Radiography or Ultrasonic are performed before Hardness; ",
#     IT_CODE:
#         "Radiografia o Ultrasuoni eseguiti prima delle misure di durezza; ",
# }
note_rc_lt_hb = {
    RU_CODE: "РК или УЗК проведено раньше замеров твердости; ",
    GB_CODE: "Radiography or Ultrasonic are performed before Hardness; ",
    IT_CODE:
        "Radiografia o Ultrasuoni eseguiti prima delle misure di durezza; ",
}
# Default:
# {
#     RU_CODE: "РК или УЗК проведено раньше стилоскопирования; ",
#     GB_CODE: "Radiography or Ultrasound are performed before Styloscopy; ",
#     IT_CODE: "Radiografia o Ultrasuoni eseguiti prima della Stiloscopia; ",
# }
note_rc_lt_st = {
    RU_CODE: "РК или УЗК проведено раньше стилоскопирования; ",
    GB_CODE: "Radiography or Ultrasound are performed before Styloscopy; ",
    IT_CODE: "Radiografia o Ultrasuoni eseguiti prima della Stiloscopia; ",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше ВИК; ",
#     GB_CODE: "Color flaw detection is performed before visual control; ",
#     IT_CODE: "Difetti di colore eseguiti prima del controllo visivo; ",
# }
note_cd_lt_vmc = {
    RU_CODE: "ЦД проведена раньше ВИК; ",
    GB_CODE: "Color flaw detection is performed before visual control; ",
    IT_CODE: "Difetti di colore eseguiti prima del controllo visivo; ",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров твердости; ",
#     GB_CODE: "Color flaw detection is performed before hardness; ",
#     IT_CODE: "Difetti di colore eseguiti prima delle misure di durezza; ",
# }
note_cd_lt_hb = {
    RU_CODE: "ЦД проведена раньше замеров твердости; ",
    GB_CODE: "Color flaw detection is performed before hardness; ",
    IT_CODE: "Difetti di colore eseguiti prima delle misure di durezza; ",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров стилоскопирования; ",
#     GB_CODE: "Color flaw detection is performed before Styloscopy; ",
#     IT_CODE: "Difetti di colore eseguiti prima della Stiloscopia; ",
# }
note_cd_lt_st = {
    RU_CODE: "ЦД проведена раньше замеров стилоскопирования; ",
    GB_CODE: "Color flaw detection is performed before Styloscopy; ",
    IT_CODE: "Difetti di colore eseguiti prima della Stiloscopia; ",
}
# Default:
# {
#     RU_CODE: "ЦД проведена раньше замеров РК или УЗК; ",
#     GB_CODE:
#         "Color flaw control is performed before Radiography or Ultrasound; ",
#     IT_CODE:
#         "Difetti di colore eseguiti prima dei Radiografia e Ultrasuoni; ",
# }
note_cd_lt_rc = {
    RU_CODE: "ЦД проведена раньше замеров РК или УЗК; ",
    GB_CODE:
        "Color flaw control is performed before Radiography or Ultrasound; ",
    IT_CODE:
        "Difetti di colore eseguiti prima dei Radiografia e Ultrasuoni; ",
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
=====================Константы и переменные логирования=======================
======================Logging constants and variables=========================
======================Costanti e variabili di logging=========================
"""

# ===========================Сообщения для логов==============================
# ============================Logging messages================================
# ============================Messaggi per i log==============================

# Информирует о начале выполнения логики.
# ****************************************************************************
# Informs about logic part starting.
# ****************************************************************************
# Indica l'inizio dell'esecuzione della logica.
# ****************************************************************************
#
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

# Информирует о вызове метода App.calculate_dates.
# ****************************************************************************
# Informs about App.calculate_dates method calling.
# ****************************************************************************
# Informa sulla chiamata al metodo App.calculate_dates.
# ****************************************************************************
#
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

# Информирует о вызове метода App.handle_request.
# ****************************************************************************
# Informs about App.handle_request method calling.
# ****************************************************************************
# Informa sulla chiamata al metodo App.handle_request.
# ****************************************************************************
#
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

# Информирует об ошибке в программе без конкретизации.
# ****************************************************************************
# Informs about an untracked error.
# ****************************************************************************
# Informa di un errore nell'applicazione senza specificazioni.
# ****************************************************************************
#
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

# Информирует о начале проверки файлов.
# ****************************************************************************
# Informs about start files checking.
# ****************************************************************************
# Informa sull'inizio della verifica dei file.
# ****************************************************************************
#
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

# Информирует о вызове метода check_files.
# ****************************************************************************
# Informs about check_files method calling.
# ****************************************************************************
# Informa sulla chiamata al metodo check_files.
# ****************************************************************************
#
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

# Информирует об окончании проверки check_files.
# ****************************************************************************
# Informs that check is done.
# ****************************************************************************
# Informa sulla fine della verifica con check_files.
# ****************************************************************************
#
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

# Информирует начале парсинга.
# ****************************************************************************
# Informs that parsing is started.
# ****************************************************************************
# Informa sull'inizio del parsing.
# ****************************************************************************
#
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

# Информирует вызове метода parser.parse_weld_data.
# ****************************************************************************
# Informs about parser.parse_weld_data method calling.
# ****************************************************************************
# Informa sulla chiamata al metodo parser.parse_weld_data.
# ****************************************************************************
#
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

# Информирование о начале создания итоговой таблицы.
# ****************************************************************************
# Informs about summary table starting creation.
# ****************************************************************************
# Informa sull'inizio della creazione della tabella finale.
# ****************************************************************************
#
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

# Информирует о вызове метода create_summary.create_summary_excel.
# ****************************************************************************
# Informs about create_summary.create_summary_excel method calling.
# ****************************************************************************
# Informa sulla chiamata al metodo create_summary.create_summary_excel.
# ****************************************************************************
#
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

# Информирует о создании итоговой таблицы.
# ****************************************************************************
# Informs that summary table is created.
# ****************************************************************************
# Informa che la tabella finale è stata creata.
# ****************************************************************************
#
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

# Информирует о запуске процесса создания итоговой таблицы.
# ****************************************************************************
# Indicates the start of the process for creating the final table.
# ****************************************************************************
# Informa sull'avvio del processo di creazione della tabella finale.
# ****************************************************************************
#
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

# Информирует о добавлении заголовков в итоговую таблицу.
# ****************************************************************************
# Indicates that headers are being added to the final table.
# ****************************************************************************
# Informa sull'aggiunta delle intestazioni alla tabella finale.
# ****************************************************************************
#
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

# Информирует о начале добавления данных в итоговую таблицу.
# ****************************************************************************
# Indicates the start of the process for creating the final table.
# ****************************************************************************
# Informa sull'inizio dell'inserimento dei dati nella tabella finale.
# ****************************************************************************
#
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

# Информирует о добавлении данных в итоговую таблицу.
# ****************************************************************************
# Indicates that the result data is being added to the final table.
# ****************************************************************************
# Informa sull'aggiunta dei dati nella tabella finale.
# ****************************************************************************
#
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

# Информирует о сохранении итоговой таблицы.
# ****************************************************************************
# Indicates that the final table is being saved.
# ****************************************************************************
# Informa che la tabella finale è stata salvata.
# ****************************************************************************
#
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

# Информирует о том, куда сохранен итоговый файл.
# ****************************************************************************
# Indicates where the final file has been saved.
# ****************************************************************************
# Informa dove è stato salvato il file finale.
# ****************************************************************************
#
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
# ****************************************************************************
# Indicates that parsing is complete and specifies the number of items.
# ****************************************************************************
# Informa che il parsing è completato e indica il numero di elementi.
# ****************************************************************************
#
# Default:
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
# ****************************************************************************
# Indicates that the file is misplaced and shows which file it is and where it
# was uploaded.
# ****************************************************************************
# Informa che il file non si trova nella posizione corretta e mostra quale
# file è e dove è stato caricato.
# ****************************************************************************
#
# Default:
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
# ****************************************************************************
# Indicates that the file has unacceptable extension.
# ****************************************************************************
# Informa che il file caricato ha un'estensione non valida.
# ****************************************************************************
#
# Default:
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

# Информирует о выбранных файлах.
# ****************************************************************************
# Informs about the chosen files.
# ****************************************************************************
# Informa sui file selezionati.
# ****************************************************************************
#
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

# Информирует о том, куда сохраняем таблицу.
# ****************************************************************************
# Indicates the path where we save the final table.
# ****************************************************************************
# Informa dove viene salvata la tabella.
# ****************************************************************************
#
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
================Constants & variables of the graphic interface================
================Costanti e variabili dell'interfaccia grafica=================
"""
# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================     Основные окна      ==========================
# ==========================        WINDOWS         ==========================
# ==========================    Primary windows     ==========================
# ==========================        FINESTRE        ==========================
# ==========================  Finestre secondarie   ==========================
# ============================================================================

# Имя Главного окна.
# ****************************************************************************
# Start window title.
# ****************************************************************************
# Titolo della finestra principale.
# ****************************************************************************
# Default: "Dates Control - v1.0.0"
START_WINDOW_TITLE = "Dates Control - v1.0.0"

# Размеры стартового окна.
# ****************************************************************************
# Start window dimensions.
# ****************************************************************************
# Dimensioni della finestra principale.
# ****************************************************************************
WINDOW_WIDTH = 600  # Default: 600
WINDOW_HEIGHT = 400  # Default: 400

# ========================Настройки работы с иконками=========================
# ===============================Icon settings================================
# ==========================Impostazioni delle icone==========================

# Имя папки, в которой хранятся иконки.
# ****************************************************************************
# The name of the folder where icons are stored.
# ****************************************************************************
# Nome della cartella in cui sono archiviate le icone.
# ****************************************************************************
ICONS_FOLDER_NAME = "files/icons"  # Default: "files/icons"

# Имя файла иконки приложения, которая будет отображаться в углу приложения.
# ****************************************************************************
# The name of the application icon file that will be displayed in the
# corner of the application.
# ****************************************************************************
# Nome del file dell'icona dell'applicazione che verrà visualizzata
# nell'angolo dell'app.
# ****************************************************************************
PNG_ICON_FILENAME = "mark32x32.png"  # Default: "mark32x32.png"

# Имя файла иконки приложения, которая будет отображаться в панели задач.
# ****************************************************************************
# The name of the application icon file that will be displayed in the taskbar.
# ****************************************************************************
# Nome del file dell'icona dell'applicazione che verrà visualizzata nella
# barra delle applicazioni.
# ****************************************************************************
ICO_ICON_FILENAME = "mark32x32.ico"  # Default: "mark32x32.ico"

# Путь к .png иконке приложеня.
# ****************************************************************************
# Path to the .png icon of the app.
# ****************************************************************************
# Percorso dell'icona .png dell'applicazione.
# ****************************************************************************
#
# Default: "files/icons/mark32x32.png"
PNG_ICON_FILEPATH = "files/icons/mark32x32.png"

# Путь к .ico иконке приложеня.
# ****************************************************************************
# Path to the .ico icon of the app.
# ****************************************************************************
# Percorso dell'icona .ico dell'applicazione.
# ****************************************************************************
#
# # Default: "files/icons/mark32x32.ico"
ICO_ICON_FILEPATH = "files/icons/mark32x32.ico"

# Путь к .png иконке флага РФ.
# ****************************************************************************
# Path to the .png icon of the RU flag.
# ****************************************************************************
# Percorso dell'icona .png della bandiera della Federazione Russa.
# ****************************************************************************
#
# # Default: "files/icons/ru40x30.png"
RU_ICON_PATH = "files/icons/ru40x30.png"

# Путь к .png иконке флага Великобритании.
# ****************************************************************************
# Path to the .png icon of the GB flag.
# ****************************************************************************
# Percorso dell'icona .png della bandiera del Regno Unito.
# ****************************************************************************
#
# # Default: "files/icons/gb40x30.png"
GB_ICON_PATH = "files/icons/gb40x30.png"

# Путь к .png иконке флага Италии.
# ****************************************************************************
# Path to the .png icon of the IT flag.
# ****************************************************************************
# Percorso dell'icona .png della bandiera dell'Italia.
# ****************************************************************************
#
# # Default: "files/icons/it40x30.png"
IT_ICON_PATH = "files/icons/it40x30.png"

# ======================Настройки для метода browse_file======================
# =========================browse_file method settings========================
# ===================Impostazioni per il metodo browse_file===================

# Стартовый элемент очистки текстового поля и вставки в него.
# рекомендуется не менять.
# ****************************************************************************
# The starting element for clearing the text field and inserting into it.
# It is recommended not to change it.
# ****************************************************************************
# Elemento iniziale per la pulizia del campo di testo e l'inserimento di nuovi
# dati.
# Si raccomanda di non modificarlo.
# ****************************************************************************
FIRST_ELEMENT = 0  # Default: 0

# Разделитель пути файлов, если выбрано несколько файлов в одном тестовом
# поле.
# ****************************************************************************
# File path divider if several files in the one textfield are chosen.
# ****************************************************************************
# Separatore del percorso dei file, se vengono selezionati più file in un
# unico campo di testo.
# ****************************************************************************
PATH_DIVIDER = '; '  # Default: '; '

# ============================================================================
# ==========================          ОКНА          ==========================
# ==========================  Второстепенные окна   ==========================
# ==========================        WINDOWS         ==========================
# ==========================   Secondary windows    ==========================
# ==========================        FINESTRE        ==========================
# ==========================  Finestre secondarie   ==========================
# ============================================================================

# =========================Настройки для InfoWindow===========================
# ===========================InfoWindow settings==============================
# =======================Impostazioni per InfoWindow==========================
# Это окно вылезает, когда начинается процесс обработки файлов и предупреждает
# юзера, что работа пошла, чтобы юзер не подумал, что приложение зависло.
# ****************************************************************************
# This window pops up when the file processing begins to inform the users that
# the process has started, so they don't think the application has frozen.
# ****************************************************************************
# Questa finestra appare quando inizia il processo di elaborazione dei file e
# avverte l'utente che il lavoro è iniziato, per evitare che pensi che
# l'applicazione si sia bloccata.
# ****************************************************************************

# Ширина инфобокса.
# ****************************************************************************
# Infobox width.
# ****************************************************************************
# Larghezza dell'InfoBox.
# ****************************************************************************
INFO_WINDOW_WIDTH = 300  # Default: 200

# Высота инфобокса.
# ****************************************************************************
# Infobox height.
# ****************************************************************************
# Altezza dell'InfoBox.
# ****************************************************************************
INFO_WINDOW_HEIGHT = 100  # Default: 100

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Фреймы         ==========================
# ==========================       COMPONENTS       ==========================
# ==========================         Frames         ==========================
# ==========================       COMPONENTI       ==========================
# ==========================         Frames         ==========================
# ============================================================================

# =======================Настройки для фрейма ввода пути======================
# ======================Settings for the path input frame=====================
# ===============Impostazioni per il frame del percorso di input==============
# Содержат лейбл, поле для ввода и кнопку.
# ****************************************************************************
# Contain label, textfield and a button.
# ****************************************************************************
# Contiene un'etichetta, un campo di input e un pulsante.
# ****************************************************************************

# Отступы от краев по горизонтали.
# Поскольку заполнение по умолчанию будет на весь размер окна по ширине,
# то отступы будут с обеих сторон.
# ****************************************************************************
# Horizontal padding from the edges.
# Since the default fill will stretch to the full width of the window,
# the padding will apply to both sides.
# ****************************************************************************
# Margini orizzontali dai bordi.
# Poiché il riempimento predefinito sarà per tutta la larghezza della finestra,
# i margini saranno su entrambi i lati.
# ****************************************************************************
FRAME_PADX = 20  # Default: 20

# ==================Настройки для фрейма разделительной строки================
# ========================Settings for the divider frame======================
# ================Impostazioni per il frame della linea divisoria=============
# Строка идет после каждого фрейма и нужна для отделения фреймов
# друг от друга, чтобы они не сливались.
# ****************************************************************************
# The line follows each frame and is needed to separate frames so they don't
# blend together.
# ****************************************************************************
# La linea segue ogni frame ed è necessaria per separare i frame
# l'uno dall'altro, in modo che non si confondano.
# ****************************************************************************

# Высота разделительной строки.
# ****************************************************************************
# The height of the divider line.
# ****************************************************************************
# Altezza della linea divisoria.
# ****************************************************************************
DIVIDER_HEIGHT = 10  # Default: 5

# =======================Настройки для фрейма кнопок==========================
# ==========================Buttons frame settings============================
# ===================Impostazioni per il frame dei pulsanti===================
# Фрейм, который используется для расположения кнопок внизу окна.
# ****************************************************************************
# The frame used for placing buttons at the bottom of the window.
# ****************************************************************************
# Frame utilizzato per posizionare i pulsanti nella parte inferiore della
# finestra.
# ****************************************************************************

# Отступы для фрейма по вертикали в пикселях.
# ****************************************************************************
# Vertical padding for the frame in pixels.
# ****************************************************************************
# Margini verticali del frame in pixel.s
# ****************************************************************************
BUTTONS_FRAME_PADY = 10  # Default: 10

# =========================Настройки для кнопок фрейма========================
# ===========================Frame buttons settings===========================
# ====================Impostazioni per i pulsanti del frame===================
# Отступ от края по вертикали сверху и снизу.
# ****************************************************************************
# Padding from the top and bottom edges vertically.
# ****************************************************************************
# Margine verticale sopra e sotto il bordo.
# ****************************************************************************
SETTINGS_BUTTONS_FRAME_PADY = 20

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Кнопки         ==========================
# ==========================       COMPONENTS       ==========================
# ==========================        Buttons         ==========================
# ==========================       COMPONENTI       ==========================
# ==========================        Pulsanti        ==========================
# ============================================================================

# ===============================Общие настройки==============================
# ===============================Common settings==============================
# ============================Impostazioni generali===========================
# Ширина кнопок фрейма по умолчанию (в количестве вмещаемых символов).
# ****************************************************************************
# Frame buttons width by default (in symbols amount).
# ****************************************************************************
# Larghezza predefinita dei pulsanti del frame (in numero di caratteri).
# ****************************************************************************
BUTTONS_WIDTH = 15  # Default: 15

# =========================Настройки для кнопки "Обзор"=======================
# =========================="Browse" button settings"=========================
# =================Impostazioni per il pulsante "Navigazione"=================

# Отступ слева от кнопки.
# ****************************************************************************
# Left padding for the button.
# ****************************************************************************
# Margine sinistro del pulsante.
# ****************************************************************************
BROWSE_BUTTON_LEFT_PADX = 10  # Default: 10

# Отступ справа от кнопки.
# ****************************************************************************
# Right padding for the button.
# ****************************************************************************
# Margine destro del pulsante.
# ****************************************************************************
BROWSE_BUTTON_RIGHT_PADX = 0  # Default: 0

# =================Настройки для кнопок фрейма окна настроек==================
# ===========Settings for the buttons in the settings window frame============
# ===Impostazioni per i pulsanti del frame della finestra delle impostazioni==

# Отступы от края и друг от друга по горизонтали.
# ****************************************************************************
# Horizontal padding from the edges and between each other.
# ****************************************************************************
# Margini orizzontali dai bordi e tra i pulsanti.
# ****************************************************************************
SETTINGS_BUTTONS_PADX = 5  # Default: 5

# =====================Расположение кнопок внутри фрейма======================
# ================== Placement of buttons inside the frame====================
# ===================Posizionamento dei pulsanti nel frame====================

# Отступы по горизонтали слева и справа для кнопок внутри фрейма.
# ****************************************************************************
# Horizontal padding on the left and right for buttons inside the frame.
# ****************************************************************************
# Margini orizzontali a sinistra e a destra per i pulsanti all'interno del
# frame.
# ****************************************************************************
FRAME_BUTTONS_PADX = 5  # Default: 5

# Отступы по вертикали сверху и снизу для кнопок внутри фрейма.
# ****************************************************************************
# Vertical padding on the top and bottom for buttons inside the frame.
# ****************************************************************************
# Margini verticali sopra e sotto per i pulsanti all'interno del frame.
# ****************************************************************************
FRAME_BUTTONS_PADY = 5  # Default: 5

# =========================Настройки языковых кнопок=========================
# =======================Settings for language buttons=======================
# ==================Impostazioni per i pulsanti della lingua=================

# Путь к иконке в зависимости от выбранного языкового кода.
# ****************************************************************************
# The path to the icon depends on the selected language code.
# ****************************************************************************
# Percorso dell'icona in base al codice della lingua selezionato.
# ****************************************************************************
#
# Default:
# {
#     RU_CODE: RU_ICON_PATH,
#     GB_CODE: GB_ICON_PATH,
#     IT_CODE: IT_ICON_PATH
# }
lang = {
    RU_CODE: RU_ICON_PATH,
    GB_CODE: GB_ICON_PATH,
    IT_CODE: IT_ICON_PATH
}

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================         Лейблы         ==========================
# ==========================       COMPONENTS       ==========================
# ==========================         Labels         ==========================
# ==========================       COMPONENTI       ==========================
# ==========================        Etichette       ==========================
# ============================================================================

# =======================Настройки для Лейбла Авторства=======================
# =======================Settings for the Author Label========================
# ==================Impostazioni per l'etichetta dell'autore==================

# Текст лейбла.
# ****************************************************************************
# Label text.
# ****************************************************************************
# Testo dell'etichetta.
# ****************************************************************************
AUTHOR_LABEL_TEXT = "Created by Viunik"  # Default: "Created by Viunik"

# Отступы по вертикали.
# ****************************************************************************
# Vertical padding.
# ****************************************************************************
# Margini verticali.
# ****************************************************************************
AUTHOR_PADY = -5  # Default: -5

# Устанавливаем горизонтальную позицию от левого края окна (центр).
# Тут 0 - левый край, 1.0 - правый край, 0.5 - середина.
# ****************************************************************************
# Set the horizontal position relative to the left edge of the
# window (center).
# Here, 0 is the left edge, 1.0 is the right edge, 0.5 is the middle.
# ****************************************************************************
# Impostare la posizione orizzontale rispetto al bordo sinistro della
# finestra (centro).
# Qui 0 è il bordo sinistro, 1.0 è il bordo destro, 0.5 è il centro.
# ****************************************************************************
AUTHOR_RELX = 0.5  # Default = 0.5

# Устанавливаем вертикальную позицию от верхнего края окна (центр).
# Тут 0 - верхний край, 1.0 - нижний край, 0.5 - середина.
# ****************************************************************************
# Set the vertical position relative to the top edge of the window (center).
# Here, 0 is the left edge, 1.0 is the right edge, 0.5 is the middle.
# ****************************************************************************
# Impostare la posizione verticale rispetto al bordo superiore della
# finestra (centro).
# Qui 0 è il bordo superiore, 1.0 è il bordo inferiore, 0.5 è il centro.
# ****************************************************************************
AUTHOR_RELY = 1.0  # Default = 1.0

# ==================Настройки для Лейбла информационного окна=================
# ==============Settings for the Label in the Information Window==============
# ===========Impostazioni per l'etichetta della finestra informativa==========

# Отступ по краям окна по горизонтали.
# ****************************************************************************
# Horizontal padding from the edges of the window.
# ****************************************************************************
# Margini orizzontali dai bordi della finestra.
# ****************************************************************************
INFO_LABEL_PADX = 20  # Default: 20

# Отступ по краям окна по вертикали.
# ****************************************************************************
# Vertical padding from the edges of the window.
# ****************************************************************************
# Margini verticali dai bordi della finestra.
# ****************************************************************************
INFO_LABEL_PADY = 20  # Default: 20

# ============================================================================
# ==========================       КОМПОНЕНТЫ       ==========================
# ==========================     Текстовые поля     ==========================
# ==========================       COMPONENTS       ==========================
# ==========================       Textfields       ==========================
# ==========================       COMPONENTI       ==========================
# ==========================     Campi di testo     ==========================
# ============================================================================

# ====================Настройки для текстовых полей фрейма====================
# ===================Settings for text fields in the frame====================
# ================Impostazioni per i campi di testo del frame=================

# Ширина поля (в количестве символов).
# ****************************************************************************
# Field width (in characters).
# ****************************************************************************
# Larghezza del campo (in numero di caratteri).
# ****************************************************************************
ENTRY_WIDTH = 50  # Default: 50

# Растяжение поля при изменении размеров главного окна.
# ****************************************************************************
# Field stretching when resizing the main window.
# ****************************************************************************
# Espansione del campo durante il ridimensionamento della finestra principale.
# ****************************************************************************
ENTRY_EXPAND = True  # Default: True

"""
========================Константы и переменные логики=========================
=====================Constants & variables of the logic=======================
=====================Costanti e variabili della logica========================
"""
# ========================Настройки для get_xlsx.py===========================
# ===========================get_xlsx.py settings=============================
# =======================Impostazioni per get_xlsx.py=========================


# =========================Ключи для проверки файлов==========================
# ========================Keys for file verification==========================
# ======================Chiavi per la verifica dei file=======================
# По этим текстовым ключам проверяется каждый файл. Если указанного
# куска текста нет в указанном файле, значит файл был выбран в
# неправильном текстовом поле.
# Принцип: ищем в первых строках файла текст, который соответствует ключам.
# если текст найден, то файл выбран правильно. Если нет, райзим ошибку.
# Например: файл ВИК был выбран в поле для файлов Стилоскопирования.
# ****************************************************************************
# These text keys are used to verify each file. If the specified text segment
# is not present in the file, it means the file was selected in the wrong text
# field.
# Principle: search the first lines of the file for text matching the keys.
# If the text is found, the file is selected correctly. If not, raise an
# error.
# For example: the VMC file was selected in the field for Styloscopic files.
# ****************************************************************************
# Queste chiavi di testo vengono utilizzate per verificare ogni file.
# Se il segmento di testo specificato non è presente nel file, significa che
# il file è stato selezionato nel campo di testo sbagliato.
# Principio: cerchiamo nelle prime righe del file un testo che corrisponda
# alle chiavi.
# Se il testo viene trovato, il file è selezionato correttamente. In caso
# contrario, viene generato un errore.
# Per esempio: un file VMC è stato selezionato nel campo per i file di
# styloscopia.
# ****************************************************************************

# Ключ для проверки протоколов визуального и измерительного контроля (ВИК).
# ****************************************************************************
# Key for verifying Visual and Measurement Control (VMC) protocols.
# ****************************************************************************
# Chiave per la verifica dei protocolli di Controllo Visivo e di Misura (CVM).
# ****************************************************************************
#
# Default: ["визуальн", "visual", "visiv"]
VMC_CHECK_KEYS = ["визуальн", "visual", "visiv"]

# Ключ для проверки протоколов замеров твердости.
# ****************************************************************************
# Key for verifying Hardness Measurement protocols.
# ****************************************************************************
# Chiave per la verifica dei protocolli di Misurazione della Durezza.
# ****************************************************************************
#
# Default: ["твердост", "твёрдост", "hardness", "durezz"]
HB_CHECK_KEYS = ["твердост", "твёрдост", "hardness", "durezz"]

# Ключ для проверки протоколов радиографического контроля (РК или УЗК).
# ****************************************************************************
# # Key for verifying Radiographic Control (RC or US) protocols.
# ****************************************************************************
# Chiave per la verifica dei protocolli di Controllo Radiografico (CR) o
# Ultrasonico (US).
# ****************************************************************************
#
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

# Ключ для проверки протоколов стилоскопирования (СТ).
# ****************************************************************************
# Key for verifying Styloscopic (ST) protocols.
# ****************************************************************************
# Chiave per la verifica dei protocolli di Styloscopia (ST).
# ****************************************************************************
#
# Default: ["флуоресцент", "styloscop"]
ST_CHECK_KEYS = ["флуоресцент", "styloscop"]

# Ключ для проверки протоколов цветной дефектоскопии (ЦД)
# ****************************************************************************
# Key for verifying Dye Penetrant Testing (CD) protocols.
# ****************************************************************************
# Chiave per la verifica dei protocolli di Controllo dei Difetti
# Colorati (CD).
# ****************************************************************************
CD_CHECK_KEYS = ["капилляр", "color"]  # Default: ["капилляр", "color"]

# Ключи у словаря files_dict у нас тоже настраиваемые и могут быть любыми,
# поэтому перенесем имена ключей в константы.
# Кстати, итоговый словарь, в котором хранятся типы контроля и даты контроля
# каждого типа для каждого шва у нас пока хранится в файле parser.py и
# структура такая:
# {<номер_шва>: {<тип_контроля>: <дата_контроля>}}
# В create_summary нам нужно будет вытащить даты контроля для каждого шва по
# типу контроля, где мы будем использовать эти же константы.
# ****************************************************************************
# The keys in the files_dict dictionary are also configurable and can be any
# value, so let's move the key names to constants.
# By the way, the final dictionary that stores the control types and their
# dates for each weld is currently stored in parser.py, and its structure is
# as follows:
# {<weld_number>: {<control_type>: <control_date>}}
# In create_summary, we will need to extract control dates for each weld by
# control type, where these same constants will be used.
# ****************************************************************************
# Le chiavi nel dizionario files_dict sono anche configurabili e possono
# essere qualsiasi valore, quindi spostiamo i nomi delle chiavi nelle
# costanti.
# A proposito, il dizionario finale che contiene i tipi di controllo e le date
# di controllo per ciascun giunto è attualmente archiviato nel file parser.py
# e ha la seguente struttura:
# {<numero_giunto>: {<tipo_controllo>: <data_controllo>}}
# In create_summary, sarà necessario estrarre le date di controllo per ogni
# giunto per tipo di controllo, dove useremo queste stesse costanti.
# ****************************************************************************

# Ключ для визуального и измерительного контроля.
# ****************************************************************************
# Key for Visual and Measurement Control.
# ****************************************************************************
# Chiave per il Controllo Visivo e di Misura.
# ****************************************************************************
VMC = 'vmc'  # Default: 'vmc'

# Ключ для контроля твердости.
# ****************************************************************************
# Key for Hardness Control.
# ****************************************************************************
# Chiave per il Controllo della Durezza.
# ****************************************************************************
HB = 'hb'  # Default: 'hb'

# Ключ для радиографического или ультразвукового контроля.
# ****************************************************************************
# Key for Radiographic or Ultrasonic Control.
# ****************************************************************************
# Chiave per il Controllo Radiografico o Ultrasonico.
# ****************************************************************************
RC = 'rc'  # Default: 'rc'

# Ключ для ренгенофуоресцентного контроля или стилоскопирования.
# ****************************************************************************
# Key for X-ray Fluorescence or Styloscopic Control.
# ****************************************************************************
# Chiave per il Controllo a Fluorescenza o Styloscopia.
# ****************************************************************************
ST = 'st'  # Default: 'st'

# Ключ для цветной дефектоскопии.
# ****************************************************************************
# Key for Dye Penetrant Testing.
# ****************************************************************************
# Chiave per il Controllo dei Difetti Colorati.
# ****************************************************************************
CD = 'cd'  # Default: 'cd'

# Ключ для словаря files_dict значением которого является путь к файлу
# контроля.
# ****************************************************************************
# Key for files_dict, where the value is the path to the control file.
# ****************************************************************************
# Chiave per il dizionario files_dict, il cui valore è il percorso del file di
# controllo.
# ****************************************************************************
FILES_DICT_PATH_KEY = 'path'  # Default: 'path'

# Ключ для словаря files_dict значением которого являются ключи для проверки
# файлов контроля.
# ****************************************************************************
# Key for files_dict, where the value is the set of keys for verifying control
# files.
# ****************************************************************************
# Chiave per il dizionario files_dict, il cui valore è l'insieme delle chiavi
# per la verifica dei file di controllo.
# ****************************************************************************
FILES_DICT_CHECK_KEY = 'check'  # Default: 'check'

# =============================Остальные настройки============================
# ===============================Other settings===============================
# ==============================Altre impostazioni============================

# Разделитель, который используется для строки, содержащей путь к файлу.
# Необходим для получения имени файла из пути к нему.
# ****************************************************************************
# Separator used in a string containing the file path.
# Necessary for extracting the file name from its path.
# ****************************************************************************
# Separatore utilizzato per una stringa contenente il percorso del file.
# Necessario per ottenere il nome del file dal percorso.
# ****************************************************************************
FILEPATH_DIVIDER = '/'  # Default: '/'

# Разделитель, который используется для строки, содержащей имя файла.
# Необходим для получения разрешения файла из его имени.
# рекомендуется не трогать.
# ****************************************************************************
# Separator used in a string containing the file name.
# Necessary for extracting the file extension from its name.
# Recommended not to change.
# ****************************************************************************
# Separatore utilizzato per una stringa contenente il nome del file.
# Necessario per ottenere l'estensione del file dal suo nome.
# Si consiglia di non modificarlo.
# ****************************************************************************
EXTENSION_DIVIDER = '.'  # Default: '.'

# Разрешения, которые допустимы для файлов.
# ****************************************************************************
# Allowed file extensions.
# ****************************************************************************
# Estensioni consentite per i file.
# ****************************************************************************
EXTENSIONS = ['xlsx']  # Default: ['xlsx']

# Значения, которые определяют, с какой по какую строку мы будем искать
# совпадения по ключам для проверки файлов.
# ****************************************************************************
# Values that define the range of rows within which we will search for key
# matches for file verification.
# ****************************************************************************
# Valori che definiscono l'intervallo di righe in cui cercheremo
# corrispondenze con le chiavi per la verifica dei file.
# ****************************************************************************
MIN_ROW_RANGE_VALUE = 1  # Default: 1
MAX_ROW_RANGE_VALUE = 11  # Default: 10

# ===========================Настройки для parser.py==========================
# =============================parser.py settings=============================
# =========================Impostazioni per parser.py=========================

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
# ****************************************************************************
# Since weld numbers should contain only Cyrillic letters, but there are also
# similar Latin letters, due to human error, the same weld number can be
# written in different layouts in different protocols.
# This is especially true for the letter "C," which is on the same key
# regardless of the layout, and it’s the most idiotic oversight by the guy who
# designed the "ЙЦУКЕН" layout.
# Separately, I could rant about having to hold Shift to type a comma, but
# that’s a story for another time.
# As a result, we need to replace Latin letters with Cyrillic ones for each
# weld number. This dictionary is used for such letter mapping.
# ****************************************************************************
# Poiché i numeri di giunto devono contenere solo lettere cirilliche,
# ma ci sono lettere latine simili, a causa di errori umani, lo stesso numero
# di giunto può essere scritto con layout diversi in protocolli diversi.
# Questo vale soprattutto per la lettera "C," che si trova sullo stesso tasto,
# indipendentemente dal layout, ed è il difetto più idiota di chi ha inventato
# il layout "ЙЦУКЕН". Inoltre, potrei lamentarmi del fatto che per scrivere
# una virgola devo premere Shift, ma questa è un'altra storia.
# Di conseguenza, dobbiamo sostituire le lettere latine con quelle cirilliche
# per ogni numero di giunto. Questo dizionario serve a mappare le lettere.
# ****************************************************************************
#
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
# ****************************************************************************
# Usually, dates in Excel are represented as datetime objects, but if for some
# reason the date is converted to a string, it would be good to verify it as
# well.
# This regex is used to check if the value of the current cell matches one of
# the date formats.
# The formats can be:
# 1. With one or two digits for the day and month.
# 2. With two or four digits for the year.
# 3. With a delimiter in the form of a dot, slash, or dash.
# ****************************************************************************
# Di solito, in Excel, le date sono rappresentate come oggetti datetime, ma se,
# per qualche motivo, la data è convertita in una stringa, sarebbe opportuno
# verificarla.
# Questa regex è necessaria per controllare se il valore della cella corrente
# corrisponde a uno dei formati di data.
# I formati possono essere:
# 1. Con una o due cifre per il numero del giorno e del mese.
# 2. Con due o quattro cifre per l'anno.
# 3. Con un separatore come punto, slash o trattino.
# ****************************************************************************
#
# Default: r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}'
DATE_REGEXP = r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}'

# В конце концов, какой бы не была дата, мы преобразуем ее в полюбившийся
# почти всем формат типа дд/мм/гггг. Ебанем универсалочку, так сказать. В
# таком формате дата будет отображена в итоговом сгенерированном файле.
# ****************************************************************************
# Ultimately, regardless of the original format, we will convert the date to
# the universally loved format of dd/mm/yyyy. Let’s make it a
# one-size-fits-all.
# This is the format in which the date will be displayed in the final
# generated file.
# ****************************************************************************
# Alla fine, indipendentemente dal formato della data, la convertiremo
# nel formato preferito da quasi tutti, del tipo gg/mm/aaaa.
# Un approccio universale, per così dire. In questo formato,
# la data verrà visualizzata nel file finale generato.
# ****************************************************************************
DATE_FORMAT = "%d/%m/%Y"  # Default: "%d/%m/%Y"

# =======================Настройки для create_summary.py======================
# ==========================create_summary.py settings========================
# ======================Impostazioni per create_summary.py====================

# Дефолтное значение ячейки в столбце с примечаниями.
# ****************************************************************************
# Default value for the "Notes" column of a final table.
# ****************************************************************************
# Valore predefinito della cella nella colonna delle note.
# ****************************************************************************
NOTE = ""  # Default: ""

# Формат даты по умолчанию для записи в итоговый файл.
# ****************************************************************************
# Default date format for the record into the final table.
# ****************************************************************************
# Formato data predefinito per la scrittura nel file finale.
# ****************************************************************************
DATE_FORMAT = "%d/%m/%Y"  # Default: "%d/%m/%Y"

# Символ экранирования для даты в эксель.
# ****************************************************************************
# Escape character for dates in Excel.
# ****************************************************************************
# Carattere di escape per le date in Excel.
# ****************************************************************************
EXCEL_ESCAPING_SYMBOL = "'"  # Default: "'"

"""
=====================Константы и переменные логирования=======================
======================Logging constants and variables=========================
======================Costanti e variabili di logging=========================
"""
# Устанавливает максимальное количество строк файла логирования.
# Если при очередном запуске программы файл будет переполнен,
# он очистится.
# ****************************************************************************
# Sets the maximum number of rows for the log file.
# If the file exceeds this limit during the next program launch, it will be
# cleared.
# ****************************************************************************
# Imposta il numero massimo di righe per il file di log.
# Se il file supera questo limite al prossimo avvio dell'applicazione, verrà
# svuotato.
# ****************************************************************************
MAX_LOG_LINES = 50000  # Default: 50000

# Кодировка файла логирования. Необходима для кириллицы. Лучше не трогать.
# ****************************************************************************
# Encoding for the log file. Required for Cyrillic characters. Better not to
# change it.
# ****************************************************************************
# Codifica del file di log. Necessaria per le lettere cirilliche.
# Si consiglia di non modificarla.
# ****************************************************************************
ENCODING = 'utf-8'  # Default: 'utf-8'

# Папка для хранения логов.
# ****************************************************************************
# Log storage folder.
# ****************************************************************************
# Cartella per archiviare i file di log.
# ****************************************************************************
LOG_FOLDER = 'logging_files'  # Default: 'logging_files'

# Имя файла логов.
# ****************************************************************************
# Logger filename.
# ****************************************************************************
# Nome del file di log.
# ****************************************************************************
LOG_FILENAME = 'app.log'  # Default: 'app.log'

# Формат записи логов.
# ****************************************************************************
# Log entry format.
# ****************************************************************************
# Formato per le voci di log.
# ****************************************************************************
# Default: '%(asctime)s - %(levelname)s - %(message)s'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# ============================Сообщения для логов=============================
# ==============================Logging messages==============================
# ============================Messaggi per i log==============================

# Разделитель между логами разных процессов.
# ****************************************************************************
# Separator between logs of different processes.
# ****************************************************************************
# Separatore tra i log di processi diversi.
# ****************************************************************************
# Default: "******************************************************"
LOG_DIVIDER = "******************************************************"

"""
===============Константы и переменные пользовательских настроек===============
==================Constants and variables for user settings===================
==============Costanti e variabili per le impostazioni dell'utente============
"""
# Указываем путь сохранения итогового файла по умолчанию на рабочий стол.
# ****************************************************************************
# Specify the default save path for the final file to the desktop.
# ****************************************************************************
# Specificare il percorso predefinito per salvare il file finale sul desktop.
# ****************************************************************************
#
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
# итогового файла.
# ****************************************************************************
# This specifies the key in the JSON file whose value is the path to save the
# final file.
# ****************************************************************************
# Qui è indicata la chiave del file JSON, il cui valore è il percorso per
# salvare il file finale.
# ****************************************************************************
DEFAULT_SAVE_PATH_KEY = "DEFAULT_SAVE_PATH"  # Default: "DEFAULT_SAVE_PATH"

# Здесь указан ключ файла json, значением которого является словарь с
# языковыми настройками.
# ****************************************************************************
# This specifies the key in the JSON file whose value is a dictionary with
# language settings.
# ****************************************************************************
# Qui è indicata la chiave del file JSON, il cui valore è un dizionario con le
# impostazioni della lingua.
# ****************************************************************************
DEFAULT_LANG_KEY = "lang"  # Default "lang"

# Здесь указан ключ файла json, значением которого является код страны
# выбранного языка.
# ****************************************************************************
# This specifies the key in the JSON file whose value is the country code of
# the selected language.
# ****************************************************************************
# Qui è indicata la chiave del file JSON, il cui valore è il codice del paese
# della lingua selezionata.
# ****************************************************************************
DEFAULT_LANG_CODE_KEY = "code"  # Default: "code"

# Здесь указан ключ файла json, значением которого является путь к файлу с
# иконкой страны выбранного языка.
# ****************************************************************************
# This specifies the key in the JSON file whose value is the path to the file
# with the selected country's icon.
# ****************************************************************************
# Qui è indicata la chiave del file JSON, il cui valore è il percorso del file
# con l'icona del paese della lingua selezionata.
# ****************************************************************************
DEFAULT_LANG_ICON_PATH_KEY = "icon_path"  # Default: "icon_path"

# Указываем имя файла, под которым будут сохраняться пользовательские
# настройки.
# ****************************************************************************
# Specify the file name under which user settings will be saved.
# ****************************************************************************
# Specificare il nome del file in cui verranno salvate le impostazioni
# dell'utente.
# ****************************************************************************
SETTINGS_FILE_NAME = "settings.json"  # Default: "settings.json"

# Путь из корня проекта к папке с логикой.
# ****************************************************************************
# Path from the project root to the folder containing the logic.
# ****************************************************************************
# Percorso dalla radice del progetto alla cartella con la logica.
# ****************************************************************************
LOGIC_PATH = 'logic'  # Default: 'logic'

# Путь из корня проекта к папке с интерфейсом.
# ****************************************************************************
# Path from the project root to the folder containing the interface.
# ****************************************************************************
# Percorso dalla radice del progetto alla cartella con l'interfaccia.
# ****************************************************************************
GUI_PATH = 'gui'  # Default: 'gui'

# Отступ в пробелах для записи в json файл.
# ****************************************************************************
# Indentation in spaces for writing to the JSON file.
# ****************************************************************************
# Spaziatura (in spazi) per la scrittura nel file JSON.
# ****************************************************************************
JSON_INDENT = 4  # Default: 4

# Имя итоговой таблицы.
# ****************************************************************************
# Final table title.
# ****************************************************************************
# Nome della tabella finale.
# ****************************************************************************
SAVE_FILE_NAME = "summary.xlsx"  # Default: "summary.xlsx"

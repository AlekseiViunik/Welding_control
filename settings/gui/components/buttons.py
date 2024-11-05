"""
Здесь будут храниться настройки кнопок.
"""
# ==========================Общие настройки==========================
# Ширина кнопок фрейма по умолчанию (в количестве вмещаемых символов)
BUTTONS_WIDTH = 15  # Default: 15

# Текст, отображаемый на кнопках в порядке указания элементов в массиве
# И процесс, запускаемый для каждой кнопки
# Default: BUTTON_TEXTS = {
#    "Погнали": "start_process",
#    "Забить": "clear_entries",
#    "Настройки": "open_settings",
#    }
START_BUTTON_TEXTS = {
    "Погнали": "start_process",
    "Забить": "clear_entries",
    "Настройки": "open_settings",
}

# ====================Настройки для кнопки "Обзор"===================

# Текст кнопки
BROWSE_BUTTON_TEXT = 'Обзор'  # Default: 'Обзор'

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
SAVE_BUTTON_NAME = "Сохранить"  # Default: "Сохранить"

# Имя кнопки для сохранения
CANCEL_BUTTON_NAME = "Отмена"  # Default: "Отмена"

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

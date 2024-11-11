import tkinter as tk
from tkinter import filedialog

from settings import settings as set


class AppHelper:
    def __init__(self, root, lang_code):
        self.root = root
        self.info_window = None
        self.lang_code = lang_code

    def center_window(self, window, width, height):
        """Центрирует окно на экране."""

        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Вычисляем координаты для центрирования окна
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window_position = f"{width}x{height}+{x}+{y}"
        # Устанавливаем позицию окна
        window.geometry(window_position)

    def show_info_window(self):
        """Показывает информационное окно о начале работы."""
        self.info_window = tk.Toplevel(self.root)
        title = set.info_window_title[self.lang_code]
        self.info_window.title(title)
        self.info_window.geometry(
            f"{set.INFO_WINDOW_WIDTH}x{set.INFO_WINDOW_HEIGHT}"
        )
        self.center_window(
            self.info_window,
            set.INFO_WINDOW_WIDTH,
            set.INFO_WINDOW_HEIGHT
        )

        label = tk.Label(
            self.info_window,
            text=set.INFO_LABEL_TEXT,
            padx=set.INFO_LABEL_PADX,
            pady=set.INFO_LABEL_PADY
        )
        label.pack()

    def browse_file(self, entry, choose_directory=False, parent=None):
        """Открывает диалог выбора файла или директории."""
        if parent:
            # Устанавливаем окно на передний план
            parent.attributes('-topmost', True)
            parent.focus_force()

        if choose_directory:
            # Открываем диалог выбора директории
            path = filedialog.askdirectory()
            if path:  # Проверяем, что пользователь выбрал директорию
                entry.delete(set.FIRST_ELEMENT, tk.END)
                entry.insert(set.FIRST_ELEMENT, path)  # Убираем разделитель
        else:
            # Открываем диалог выбора файла
            paths = filedialog.askopenfilenames()
            if paths:  # Проверяем, что пользователь выбрал файлы
                entry.delete(set.FIRST_ELEMENT, tk.END)
                entry.insert(set.FIRST_ELEMENT, set.PATH_DIVIDER.join(paths))

        if parent:  # Устанавливаем фокус обратно на текущее окно
            parent.attributes('-topmost', False)
            parent.focus_set()

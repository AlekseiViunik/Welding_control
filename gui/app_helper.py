import tkinter as tk
from tkinter import filedialog

from settings.gui.components import (
    buttons as btn,
    labels as lbl,
    textfield as txt,
    frames as fr
)
from settings.gui.windows import (
    windows as win,
    info_windows as info
)


class AppHelper:
    def __init__(self, root):
        self.root = root
        self.info_window = None

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
        self.info_window.title(info.INFO_WINDOW_TITLE)
        self.info_window.geometry(
            f"{info.INFO_WINDOW_WIDTH}x{info.INFO_WINDOW_HEIGHT}"
        )
        self.center_window(
            self.info_window,
            info.INFO_WINDOW_WIDTH,
            info.INFO_WINDOW_HEIGHT
        )

        label = tk.Label(
            self.info_window,
            text=lbl.INFO_LABEL_TEXT,
            padx=lbl.INFO_LABEL_PADX,
            pady=lbl.INFO_LABEL_PADY
        )
        label.pack()

    def create_label_entry_frame(
        self,
        parent,
        label_text,
        hint='',
        choose_directory=False
    ):
        """Создает фрейм с лейблом и текстовым полем."""
        frame = tk.Frame(parent)
        frame.pack(fill=fr.FRAME_FILL_AXIS, padx=fr.FRAME_PADX)

        label = tk.Label(frame, text=label_text)
        label.pack(anchor=lbl.LABEL_ANCHOR)

        entry = tk.Entry(
            frame,
            textvariable=hint,
            width=txt.ENTRY_WIDTH
        )
        entry.pack(
            side=txt.ENTRY_FRAME_SIDE,
            fill=txt.ENTRY_FILL_AXIS,
            expand=txt.ENTRY_EXPAND
        )

        button = tk.Button(
            frame,
            text=btn.BROWSE_BUTTON_TEXT,
            command=lambda e=entry: self.browse_file(
                e,
                choose_directory,
                parent
            )
        )
        button.pack(
            side=btn.BROWSE_BUTTON_SIDE,
            padx=(btn.BROWSE_BUTTON_LEFT_PADX, btn.BROWSE_BUTTON_RIGHT_PADX)
        )
        divider = tk.Frame(parent, height=fr.DIVIDER_HEIGHT)
        divider.pack(fill=fr.DIVIDER_FILL_AXIS)
        return entry

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
                entry.delete(win.FIRST_ELEMENT, tk.END)
                entry.insert(win.FIRST_ELEMENT, path)  # Убираем разделитель
        else:
            # Открываем диалог выбора файла
            paths = filedialog.askopenfilenames()
            if paths:  # Проверяем, что пользователь выбрал файлы
                entry.delete(win.FIRST_ELEMENT, tk.END)
                entry.insert(win.FIRST_ELEMENT, win.PATH_DIVIDER.join(paths))

        if parent:  # Устанавливаем фокус обратно на текущее окно
            parent.attributes('-topmost', False)
            parent.focus_set()

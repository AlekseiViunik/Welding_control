import tkinter as tk
from tkinter import filedialog

from settings import settings as set


class Frame:
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

    def create_entry_frame(self, label_text, hint='', choose_directory=False):
        """Создает фрейм с лейблом и текстовым полем."""
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=set.FRAME_PADX)

        label = tk.Label(frame, text=label_text)
        label.pack(anchor=set.LABEL_ANCHOR)

        entry = tk.Entry(frame, textvariable=hint, width=set.ENTRY_WIDTH)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=set.ENTRY_EXPAND)

        button = tk.Button(
            frame,
            text=set.browse_button_text[self.instance.lang_code],
            command=lambda: self.browse_file(entry, choose_directory)
        )
        button.pack(
            side=tk.RIGHT,
            padx=(set.BROWSE_BUTTON_LEFT_PADX, set.BROWSE_BUTTON_RIGHT_PADX)
        )
        divider = tk.Frame(self.root, height=set.DIVIDER_HEIGHT)
        divider.pack(fill=set.DIVIDER_FILL_AXIS)

        return entry

    def create_button_frame(self, buttons_name_and_process, buttons_args=None):
        """Создает фрейм с кнопками."""
        if buttons_args is None:
            buttons_args = {}

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=set.FRAME_BUTTONS_PADY)

        for name, command_name in buttons_name_and_process.items():
            command = getattr(self.instance, command_name)
            command_args = buttons_args.get(name, [])
            button = tk.Button(
                button_frame,
                text=name,
                command=lambda cmd=command, args=command_args: cmd(*args),
                width=set.BUTTONS_WIDTH
            )
            button.pack(side=tk.LEFT, padx=set.FRAME_BUTTONS_PADX)

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

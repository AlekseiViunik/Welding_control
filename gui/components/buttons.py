import json
import tkinter as tk

from settings.gui.components import buttons as btn
from settings import user_settings as us


class LangButton:
    def __init__(self, root, lang_settings):
        self.root = root
        self.lang_settings = lang_settings
        self.open_settings_button = None

    def create_lang_button(self, root=None, icon_path=None, command=None):
        if not icon_path:
            with open(us.SETTINGS_FILE_NAME, 'r') as f:
                settings = json.load(f)
            self.lang_settings = settings[us.DEFAULT_LANG_KEY]
            img_photo = tk.PhotoImage(
                file=self.lang_settings[us.DEFAULT_LANG_ICON_PATH_KEY]
            )
        else:
            img_photo = tk.PhotoImage(
                file=icon_path
            )
        if not command:
            command = self.open_lang_settings

        if not root:
            root = self.root

        self.img_button = tk.Button(
            root,
            image=img_photo,
            width=40,
            height=30,
            command=command
        )
        self.img_button.image = img_photo
        self.img_button.pack(side=tk.LEFT, padx=20)

    def open_lang_settings(self):
        self.open_settings_button = self.img_button
        lang_window = tk.Toplevel(self.root)
        lang_window.title("Выбор языка")

        for lang_code, icon_path in btn.lang.items():
            # Создаем кнопку для каждого языка
            self.create_lang_button(
                lang_window,
                icon_path,
                command=(
                    lambda lc=lang_code, win=lang_window:
                        self.set_language(lc, win))
            )

    def set_language(self, lang_code, win):
        """Устанавливает язык приложения и обновляет настройки."""
        with open(us.SETTINGS_FILE_NAME, 'r') as f:
            settings = json.load(f)

        settings[us.DEFAULT_LANG_KEY][us.DEFAULT_LANG_ICON_PATH_KEY] = (
            btn.lang[lang_code]
        )
        settings[us.DEFAULT_LANG_KEY][us.DEFAULT_LANG_CODE_KEY] = lang_code

        with open(us.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=us.JSON_INDENT)

        print(f"Язык установлен на: {lang_code}")

        self.update_lang_button()
        win.destroy()

    def update_lang_button(self):
        """Обновляет кнопку выбора языка с новым флагом."""
        self.open_settings_button.destroy()
        self.create_lang_button()

import json
import tkinter as tk

from logic.settings_handler import SettingsHandler
from settings import settings as set


class LangButton:
    def __init__(self, root, lang_settings):
        self.root = root
        self.lang_settings = lang_settings
        self.open_settings_button = None
        self.settings_handler = SettingsHandler()

    def create_lang_button(self, root=None, icon_path=None, command=None):
        if not icon_path:
            img_photo = tk.PhotoImage(
                file=self.lang_settings[set.DEFAULT_LANG_ICON_PATH_KEY]
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

        for lang_code, icon_path in set.lang.items():
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
        settings = self.settings_handler.file_read()

        settings[set.DEFAULT_LANG_KEY][set.DEFAULT_LANG_ICON_PATH_KEY] = (
            set.lang[lang_code]
        )
        settings[set.DEFAULT_LANG_KEY][set.DEFAULT_LANG_CODE_KEY] = lang_code

        with open(set.SETTINGS_FILE_NAME, 'w') as f:
            json.dump(settings, f, indent=set.JSON_INDENT)

        print(f"Язык установлен на: {lang_code}")

        self.update_lang_button()
        win.destroy()

    def update_lang_button(self):
        """Обновляет кнопку выбора языка с новым флагом."""
        settings = self.settings_handler.file_read()
        self.lang_settings = settings[set.DEFAULT_LANG_KEY]
        self.open_settings_button.destroy()
        self.create_lang_button()

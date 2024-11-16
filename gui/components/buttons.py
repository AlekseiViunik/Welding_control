import tkinter as tk

from logic.settings_handler import SettingsHandler
from settings import settings as set


class LangButton:
    def __init__(self, root, lang_settings, instance):
        self.root = root
        self.lang_settings = lang_settings
        self.lang_code = ''
        self.open_settings_button = None
        self.settings_handler = SettingsHandler()
        self.instance = instance

    def create_lang_button(self, root=None, icon_path=None, command=None):
        """
        Creates a language button on the bottom left (by default) corner of
        the start window. After the button was pressed a window with all
        allowed lang buttons will pop up. Then you have to choose the any
        language you need and press its button. The chosen language will set
        up automatically.
        """
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
        """
        Creates a pop up window to chose the language.
        """
        self.lang_code = self.lang_settings[set.DEFAULT_LANG_CODE_KEY]
        self.open_settings_button = self.img_button
        lang_window = tk.Toplevel(self.root)
        lang_window.title(set.lang_window_title[self.lang_code])

        for lang_code, icon_path in set.lang.items():
            # Create a button for each available language
            self.create_lang_button(
                lang_window,
                icon_path,
                command=(
                    lambda lc=lang_code, win=lang_window:
                        self.set_language(lc, win))
            )

    def set_language(self, lang_code, win):
        """Sets up the app language and updates the settings."""
        settings = self.settings_handler.file_read()

        settings[set.DEFAULT_LANG_KEY][set.DEFAULT_LANG_ICON_PATH_KEY] = (
            set.lang[lang_code]
        )
        settings[set.DEFAULT_LANG_KEY][set.DEFAULT_LANG_CODE_KEY] = lang_code

        self.settings_handler.file_write(settings)

        self.instance.lang_settings = settings[set.DEFAULT_LANG_KEY]
        self.instance.lang_code = lang_code
        self.instance.render_main_frame()
        win.destroy()

import tkinter as tk

from settings import user_settings as us


class Button:
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

    def create_lang_button(self, icon_path=None, comand=None):
        if not icon_path:
            img_photo = tk.PhotoImage(
                file=self.instance.lang_settings[us.DEFAULT_LANG_ICON_PATH_KEY]
            )
        else:
            img_photo = tk.PhotoImage(
                file=icon_path
            )
        if not comand:
            comand = self.open_lang_settings
        self.img_button = tk.Button(
            self.root,
            image=img_photo,
            width=40,
            height=30,
            command=comand
        )
        self.img_button.image = img_photo  # Сохраняем ссылку на изображение
        self.img_button.pack(side=tk.LEFT, padx=20)

    def open_lang_settings(self):
        pass

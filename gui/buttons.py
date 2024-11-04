import tkinter as tk

from settings.gui.components import (
    frames as fr,
    buttons as btn
)


class Buttons:

    def __init__(self, root, instance, parent=None):
        self.root = root
        self.instance = instance
        self.parent = parent

    def create_buttons_frame(self, buttons_name_and_process):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=fr.BUTTONS_FRAME_PADY)
        for name, command_name in buttons_name_and_process.items():
            args = (self.instance.current_path, self.parent)
            command = getattr(self.instance, command_name)
            self.create_button(
                button_frame,
                name,
                command,
                btn.BUTTONS_WIDTH,
                side=btn.BUTTONS_SIDE,
                left_padx=btn.BUTTONS_PADX,
                right_padx=btn.BUTTONS_PADX,
                args=args
            )

    def create_button(
            self,
            window,
            button_name,
            process,
            width=15,
            side='left',
            left_padx=0,
            right_padx=0,
            pady=0,
            args=None
    ):
        button = tk.Button(
            window,
            text=button_name,
            command=lambda: process(*args) if args else process(),
            width=width
        )
        button.pack(side=side, padx=(left_padx, right_padx), pady=pady)

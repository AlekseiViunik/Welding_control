import tkinter as tk

from settings import gui_settings as gs


class Buttons:

    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

    def create_buttons_frame(self, buttons_name_and_process):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=gs.BUTTONS_FRAME_PADY)
        for name, command_name in buttons_name_and_process.items():
            command = getattr(self.instance, command_name)
            self.create_button(
                button_frame,
                name, command,
                gs.BUTTONS_WIDTH,
                side=gs.FRAME_BUTTONS_SIDE,
                left_padx=gs.FRAME_BUTTONS_PADX,
                right_padx=gs.FRAME_BUTTONS_PADX,
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
            pady=0
    ):
        button = tk.Button(
            window,
            text=button_name,
            command=process,
            width=width
        )
        button.pack(side=side, padx=(left_padx, right_padx), pady=pady)

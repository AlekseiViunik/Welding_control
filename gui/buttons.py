import tkinter as tk

from gui.app_helper import AppHelper
from settings.gui.components import (
    frames as fr,
    buttons as btn,
    labels as lbl,
    textfields as txt
)


class Buttons:

    def __init__(self, root, instance):
        self.root = root
        self.instance = instance
        self.helper = AppHelper(instance)

    def create_browse_frame(self, label_text, hint='', choose_directory=False):
        browse_frame = tk.Frame(self)
        browse_frame.pack(
            fill=fr.BROWSE_FRAME_FILL_AXIS,
            padx=fr.BROWSE_FRAME_PADX
        )
        label = tk.Label(browse_frame, text=label_text)
        label.pack(anchor=lbl.LABEL_ANCHOR)
        entry = tk.Entry(
            browse_frame,
            textvariable=hint,
            width=txt.TEXT_FIELD_WIDTH
        )
        entry.pack(
            side=txt.TEXT_FIELD_FRAME_SIDE,
            fill=txt.TEXT_FIELD_FILL_AXIS,
            expand=txt.TEXT_FIELD_EXPAND
        )
        button = tk.Button(
            browse_frame,
            text=btn.BROWSE_BUTTON_TEXT,
            command=lambda e=entry: self.helper.browse_file(
                e,
                choose_directory,
                self.instance
            )
        )
        button.pack(
            side=btn.BROWSE_BUTTON_SIDE,
            padx=(btn.BROWSE_BUTTON_LEFT_PADX, btn.BROWSE_BUTTON_RIGHT_PADX)
        )

        tk.Frame(
            self.instance,
            height=fr.DIVIDER_HEIGHT
        ).pack(fill=fr.DIVIDER_FILL_AXIS)

        return entry

    def create_buttons_frame(self, buttons_name_and_process):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=fr.BUTTONS_FRAME_PADY)
        for name, command_name in buttons_name_and_process.items():
            command = getattr(self.instance, command_name)
            self.create_button(
                button_frame,
                name,
                command,
                btn.BUTTONS_WIDTH,
                side=btn.BUTTONS_SIDE,
                left_padx=btn.BUTTONS_PADX,
                right_padx=btn.BUTTONS_PADX,
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
    ):
        button = tk.Button(
            window,
            text=button_name,
            command=process,
            width=width
        )
        button.pack(side=side, padx=(left_padx, right_padx), pady=pady)

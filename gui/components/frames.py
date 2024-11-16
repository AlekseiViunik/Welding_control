import tkinter as tk
from tkinter import filedialog

from settings import settings as set


class Frame:
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

    def create_entry_frame(self, label_text, hint='', choose_directory=False):
        """
        Creates a frame containing a text field, a label, and a "Browse"
        button.

        Args:
            label_text (str): The text to display on the label.
            hint (str, optional): A placeholder or initial text for the text
                field.
            choose_directory (bool, optional): If True, the "Browse" button
                opens a directory dialog. Defaults to False.

        Returns:
            tk.Entry: The text field widget for user input.
        """
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=set.FRAME_PADX)

        label = tk.Label(frame, text=label_text)
        label.pack(anchor=tk.W)

        entry = tk.Entry(frame, textvariable=hint, width=set.ENTRY_WIDTH)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=set.ENTRY_EXPAND)

        button = tk.Button(
            frame,
            text=set.browse_button_name[self.instance.lang_code],
            command=lambda: self.browse_file(entry, choose_directory)
        )
        button.pack(
            side=tk.RIGHT,
            padx=(set.BROWSE_BUTTON_LEFT_PADX, set.BROWSE_BUTTON_RIGHT_PADX)
        )
        divider = tk.Frame(self.root, height=set.DIVIDER_HEIGHT)
        divider.pack(fill=tk.X)

        return entry

    def create_button_frame(self, buttons_name_and_process, buttons_args=None):
        """
        Creates a frame containing multiple buttons.

        Args:
            buttons_name_and_process (dict): A dictionary where keys are button
                labels, and values are the names of methods to call.
            buttons_args (dict, optional): A dictionary with button labels as
                keys and lists of arguments for the corresponding methods.
                Defaults to None.
        """
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
        """
        Opens a file or folder browse dialog and updates the associated text
        field.

        Args:
            entry (tk.Entry): The text field to update with the selected file
                or folder path.
            choose_directory (bool, optional): If True, opens a directory
                selection dialog. Defaults to False.
            parent (tk.Tk or tk.Toplevel, optional): The parent window for the
                dialog. Defaults to None, using the root window.
        """
        if parent:
            parent.attributes('-topmost', True)
            parent.focus_force()

        if choose_directory:
            path = filedialog.askdirectory()
            if path:
                entry.delete(set.FIRST_ELEMENT, tk.END)
                entry.insert(set.FIRST_ELEMENT, path)
        else:
            paths = filedialog.askopenfilenames()
            if paths:
                entry.delete(set.FIRST_ELEMENT, tk.END)
                entry.insert(set.FIRST_ELEMENT, set.PATH_DIVIDER.join(paths))

        if parent:
            parent.attributes('-topmost', False)
            parent.focus_set()

import tkinter as tk

from settings import settings as set


class AppHelper:
    def __init__(self, root, lang_code):
        self.root = root
        self.info_window = None
        self.lang_code = lang_code

    def center_window(self, window, width, height):
        """Centers window on the screen."""

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate centerscreen coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window_position = f"{width}x{height}+{x}+{y}"

        window.geometry(window_position)

    def show_info_window(self):
        """Creates an info window, that informs about the process start."""
        self.info_window = tk.Toplevel(self.root)
        title = set.info_window_title[self.lang_code]
        self.info_window.title(title)
        self.info_window.geometry(
            f"{set.INFO_WINDOW_WIDTH}x{set.INFO_WINDOW_HEIGHT}"
        )
        self.center_window(
            self.info_window,
            set.INFO_WINDOW_WIDTH,
            set.INFO_WINDOW_HEIGHT
        )

        label = tk.Label(
            self.info_window,
            text=set.info_label_text[self.lang_code],
            padx=set.INFO_LABEL_PADX,
            pady=set.INFO_LABEL_PADY
        )
        label.pack()

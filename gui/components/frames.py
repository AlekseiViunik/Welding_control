import tkinter as tk


class Frame:
    def __init__(self, parent, fill=None, padx=0, pady=0):
        self.frame = tk.Frame(parent)
        self.frame.pack(fill=fill, padx=padx, pady=pady)

    def add_widget(self, widget):
        widget.pack(in_=self.frame)

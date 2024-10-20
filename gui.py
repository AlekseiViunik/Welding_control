import tkinter as tk
from tkinter import filedialog

import get_xlsx

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("iWant")
        self.root.geometry("600x400")

        self.file_paths = []

        # Заголовки и текстовые поля
        labels = [
            "Выбери файл визуального контроля",
            "Выбери файл радиографического контроля",
            "Выбери файл Стилоскопирования",
            "Выбери файл цветной дефектоскопии",
            "Выбери файлы твердости"
        ]

        for i, label_text in enumerate(labels):
            label = tk.Label(root, text=label_text)
            label.pack(anchor='w', padx=20)  # Устанавливаем отступ 20 пикселей слева

            frame = tk.Frame(root)
            frame.pack(fill='x', padx=20)  # Создаем фрейм для текстового поля и кнопки

            entry = tk.Entry(frame, width=50)
            entry.pack(side='left', fill='x', expand=True)  # Заполняем доступное пространство

            button = tk.Button(frame, text="Обзор", command=lambda e=entry: self.browse_file(e))
            button.pack(side='right', padx=(10, 0))  # Кнопка справа от текстового поля

            self.file_paths.append(entry)

            # Разделительная строка
            tk.Frame(root, height=5).pack(fill='x')  # Добавляем пустую строку для разделения

        # Кнопки "Погнали" и "Забить"
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        start_button = tk.Button(button_frame, text="Погнали", command=self.start_process)
        start_button.pack(side='left', padx=5)

        clear_button = tk.Button(button_frame, text="Забить", command=self.clear_entries)
        clear_button.pack(side='left', padx=5)

    def browse_file(self, entry):
        """Открывает диалог выбора файла."""
        file_path = filedialog.askopenfilename()
        if file_path:
            entry.delete(0, tk.END)  # Очищаем текущее значение
            entry.insert(0, file_path)  # Вставляем выбранный путь

    def start_process(self):
        """Запускает процесс обработки."""
        vmc_path = self.file_paths[0].get()  # Путь из первого текстового поля
        hb_path = self.file_paths[1].get()   # Путь из второго текстового поля
        rc_path = self.file_paths[2].get()   # Путь из третьего текстового поля
        st_path = self.file_paths[3].get()   # Путь из четвертого текстового поля
        cd_paths = self.file_paths[4].get()  # Путь из пятого текстового поля, если несколько

        # Вызываем функцию из get_xlsx с нашим словарем
        get_xlsx.handle_request(vmc_path, hb_path, rc_path, st_path, cd_paths)

        print("Запуск обработки...")

    def clear_entries(self):
        """Очищает все текстовые поля."""
        for entry in self.file_paths:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
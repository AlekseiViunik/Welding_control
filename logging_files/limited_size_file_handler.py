"""
Класс для работы с файлом логирования. Задает максимальное количество строк в
файле и по умолчанию при переполнении файла, очищает его.
"""
import logging


class LimitedSizeFileHandler(logging.FileHandler):
    def __init__(self, *args, max_lines=20, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_lines = max_lines

    def emit(self, record):
        if self.should_rollover():
            self.rollover()
        super().emit(record)

    def should_rollover(self):
        try:
            with open(self.baseFilename, 'r', encoding='utf-8') as f:
                line_count = sum(1 for _ in f)
            return line_count >= self.max_lines
        except FileNotFoundError:
            return False

    def rollover(self):
        """
        Удаляет файл логов и создает новый, если количество строк превышает
        максимальное.
        """
        with open(self.baseFilename, 'w',  encoding='utf-8'):
            pass

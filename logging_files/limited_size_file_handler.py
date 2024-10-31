"""
Класс для работы с файлом логирования. Задает максимальное количество строк в
файле и по умолчанию при переполнении файла, очищает его.
"""
import logging

from settings import logging_settings as log


class LimitedSizeFileHandler(logging.FileHandler):
    def __init__(self, *args, max_lines=log.MAX_LOG_LINES, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_lines = max_lines

    def emit(self, record):
        if self.should_rollover():
            self.rollover()
        super().emit(record)

    def should_rollover(self):
        try:
            with open(self.baseFilename, 'r', encoding=log.ENCODING) as f:
                line_count = sum(1 for _ in f)
            return line_count >= self.max_lines
        except FileNotFoundError:
            return False

    def rollover(self):
        """
        Удаляет файл логов и создает новый, если количество строк превышает
        максимальное.
        """
        with open(self.baseFilename, 'w',  encoding=log.ENCODING):
            pass

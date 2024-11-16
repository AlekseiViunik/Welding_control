import json

from settings import settings as set


class SettingsHandler:
    def __init__(self):
        self.settings_filename = set.SETTINGS_FILE_NAME

    def file_read(self, to_return='', endcoding=set.ENCODING):
        """
        Reads the settings file. If to_return param is provided, returns a
        value for that key. Otherwise returns the whole settings dict.
        """
        with open(self.settings_filename, 'r', encoding=endcoding) as f:
            settings = json.load(f)
            if to_return:
                return settings[to_return]
            return settings

    def file_write(self, to_write=None, encoding=set.ENCODING):
        """
        Rewrites the settings json file using 'to_write'
        param to put it in the file as a new settings dict.
        """
        with open(self.settings_filename, 'w') as f:
            json.dump(to_write, f, indent=set.JSON_INDENT)

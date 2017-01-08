import os
import platform
from selenium.webdriver.common.keys import Keys

class System:

    @classmethod
    def search_file_contains(cls, path, keyword):
        for filename in os.listdir(path):
            fp = os.path.join(path, filename)
            if os.path.isdir(fp) and keyword in filename:
                return fp
            elif os.path.isdir(fp):
                cls.search_file_contains(fp, keyword)

    @staticmethod
    def get_os_name():
        return platform.system().lower()

    @staticmethod
    def is64bit():
        return platform.architecture()[0].lower() == "64bit"

    @staticmethod
    def map_ascii_key_code_to_key(key_code):
        map = {
            0: Keys.NULL,
            8: Keys.BACK_SPACE,
            9: Keys.TAB,
            10: Keys.RETURN,
            13: Keys.ENTER,
            24: Keys.CANCEL,
            27: Keys.ESCAPE,
            32: Keys.SPACE,
            42: Keys.MULTIPLY,
            43: Keys.ADD,
            44: Keys.SEPARATOR,
            45: Keys.SUBTRACT,
            56: Keys.DECIMAL,
            57: Keys.DIVIDE,
            59: Keys.SEMICOLON,
            61: Keys.EQUALS,
            127: Keys.DELETE
        }
        key = map.get(key_code)
        if key is None:
            key = chr(key_code)
        return key

    def map_named_key_code_to_special_key(key_name):
        try:
           return getattr(Keys, key_name)
        except AttributeError:
           message = "Unknown key named '%s'." % (key_name)
           raise ValueError(message)

import pandas as pd
import Constants as c

from pathlib import Path as pth


class TextFileHandler(object):

    @staticmethod
    def __get_path_for_text_files(file_name):
        return pth.joinpath(pth(c.data_files_dir), file_name)

    @staticmethod
    def load_text_from_file(file_name):
        file_handle = open(TextFileHandler.__get_path_for_text_files(file_name), c.file_read_command)
        text = file_handle.read()
        file_handle.close()

        return text

    @staticmethod
    def save_text_to_file(text, file_name):
        file_handle = open(TextFileHandler.__get_path_for_text_files(file_name), c.file_append_command)
        file_handle.write(text)
        file_handle.close()

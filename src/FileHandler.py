import pandas as pd
import Constants as c
from pathlib import Path as pth


class FileHandler(object):

    @staticmethod
    def get_path_for_data_files(file_name):
        return pth.joinpath(pth(c.data_files_dir), file_name)

    @staticmethod
    def load_data_frame_from_csv(file_name):
        return pd.read_csv(FileHandler.get_path_for_data_files(file_name))

    @staticmethod
    def save_data_frame_to_csv(data_frame, file_name):
        data_frame.to_csv(pth(FileHandler.get_path_for_data_files(file_name)))

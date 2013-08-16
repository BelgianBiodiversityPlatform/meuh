import os


def sample_data_path(filename):
    return os.path.join(os.path.dirname(__file__), 'sample_data_files', filename)


def sample_config_path(filename):
    return os.path.join(os.path.dirname(__file__), 'sample_config_files', filename)

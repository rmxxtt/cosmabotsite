import configparser


def read_config(path: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(path)
    return config

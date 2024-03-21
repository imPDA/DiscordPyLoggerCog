import logging.config
import pathlib

import yaml


DEFAULT_PATH = pathlib.Path(__file__).resolve().parent / "logging.yaml"


def setup_logging(path=DEFAULT_PATH, default_level=logging.DEBUG) -> None:
    with open(path, 'r') as f:
        try:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        except Exception:  # noqa
            logging.basicConfig(level=default_level)

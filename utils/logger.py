import os
import logging


class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        log_directory = os.path.join(os.path.dirname(__file__), "../logs")
        os.makedirs(log_directory, exist_ok=True)  # Create the 'logs' directory if it doesn't exist

        log_file_path = os.path.join(log_directory, "log_file.log")
        self.logger = self.setup_logger(log_file_path)

    def setup_logger(self, log_file_path):
        logger = logging.getLogger("CustomLogger")
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)

        # Remove existing handlers to avoid duplication
        for handler in logger.handlers:
            logger.removeHandler(handler)
        logger.addHandler(file_handler)

        return logger

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message):
        self.logger.exception(message)

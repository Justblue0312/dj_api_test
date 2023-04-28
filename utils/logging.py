import logging
import os


class CustomLogger:
    """
    A custom logger that writes log messages to a file.
    """

    def __init__(self, file_name: str):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create the Log folder if it doesn't exist
        log_folder = "logs"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Create a file handler to write log messages to a file
        log_file = f"{log_folder}\\{file_name}"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a formatter to specify the format of the log messages
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message: str):
        """
        Log an info message.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Log a warning message.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Log an error message.
        """
        self.logger.error(message)

"""
Implementation for logger services

"""

from logging import handlers, Formatter, StreamHandler, getLogger, DEBUG

from os import getcwd, makedirs, getenv
from os.path import exists

from sys import stdout

FORMATTER = Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

LOG_DIRECTORY = "{current_working_dir}/logs".format(current_working_dir=getenv('LOG_DIR', getcwd()))

LOG_FILE = "{log_directory}/App.log".format(log_directory=LOG_DIRECTORY)

if not exists(LOG_DIRECTORY):
    makedirs(LOG_DIRECTORY)

# Create the file if it doesn't exist
open(LOG_FILE, 'w+').close()


class Logger:
    """
    Logging class for implementing logger functions
    """
    @staticmethod
    def get_console_handler():
        """

        :return:
        """
        console_handler = StreamHandler(stdout)
        console_handler.setFormatter(FORMATTER)
        return console_handler

    @staticmethod
    def get_file_handler():
        """

        :return:
        """
        file_handler = handlers.TimedRotatingFileHandler(LOG_FILE, when='midnight')
        file_handler.setFormatter(FORMATTER)
        return file_handler

    @staticmethod
    def get_logger(logger_name):
        """

        :param logger_name:
        :return:
        """
        logger = getLogger(logger_name)
        logger.setLevel(DEBUG) # better to have too much log than not enough
        logger.addHandler(Logger.get_console_handler())
        logger.addHandler(Logger.get_file_handler())
        # with this pattern, it's rarely necessary to propagate the error up to parent
        logger.propagate = False
        return logger

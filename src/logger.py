import datetime
import logging
import sys


class Logger:
    def __init__(self, name=__name__):
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        handler = handlers.RotatingFileHandler(filename = 'your_log_path.log',
                                               maxBytes = 1048576,
                                               backupCount = 3)
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


class NoPassFilter(logging.Filter):
    """
    Create a log-only class and make it inherit
    logging.Filter information
    """
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


def logger(loglevel, msg, ext_flg=0, verbose=0):
    """
    Log Print
    -----
    loglevel : int
        Log level to output
    msg : str
        Log message to output
    exit_flg:
        Flag to terminate program
    verbose:
        whether to show details at the time of log output
    """
    date = datetime.datetime.now()
    if loglevel is "DEBUG":
        if verbose > 1:
            print(f'[{loglevel:5}] {date} : {msg}')
    else:
        print(f'[{loglevel:5}] {date} : {msg}')

    if ext_flg == 1:
        sys.exit(ext_flg)

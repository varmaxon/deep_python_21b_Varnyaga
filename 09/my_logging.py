import logging


class MyFilter(logging.Filter):
    def filter(self, record):
        return "successfully" not in record.msg


def create_logger():
    formatter1 = logging.Formatter(
        "%(asctime)s\t%(levelname)s\t[file]\t%(message)s"
    )

    file_handler = logging.FileHandler(filename="cache.log", mode="w")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter1)

    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    return logger


def create_stream_logger(logger):
    formatter2 = logging.Formatter(
        "%(asctime)s\t%(levelname)s\t[stdout]\t%(message)s"
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter2)

    logger.addHandler(stream_handler)

    return logger


def create_filter(logger):
    for handler in logger.handlers:
        handler.addFilter(MyFilter())

    return logger

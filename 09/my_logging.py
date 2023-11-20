import logging


class MyFilter(logging.Filter):
    def filter(self, record):
        return "successfully" not in record.msg


class Logger:
    def __init__(self):
        self.formatter1 = logging.Formatter(
            "%(asctime)s\t%(levelname)s\t[file]\t%(message)s"
        )
        self.formatter2 = logging.Formatter(
            "%(asctime)s\t%(levelname)s\t[stdout]\t%(message)s"
        )

        self.file_handler = logging.FileHandler(filename="cache.log", mode="w")
        self.file_handler.setLevel(logging.INFO)
        self.file_handler.setFormatter(self.formatter1)

        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.file_handler)


class StreamLogger(Logger):
    def __init__(self):
        super().__init__()

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(self.formatter2)

        self.logger.addHandler(stream_handler)


class FilterLogger(Logger):
    def __init__(self):
        super().__init__()

        for handler in self.logger.handlers:
            handler.addFilter(MyFilter())

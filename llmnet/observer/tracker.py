import logging

COLORS = {
    "DEFAULT": "\033[0m",
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
}

track = logging.getLogger(__name__)
track.setLevel(logging.WARNING)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        level = record.levelname
        message = super().format(record)

        if level == "INFO":
            message = COLORS["GREEN"] + message + COLORS["DEFAULT"]
        elif level == "WARNING" or level == "DEBUG":
            message = COLORS["DEFAULT"] + message + COLORS["DEFAULT"]
        elif level == "ERROR" or level == "CRITICAL":
            message = COLORS["RED"] + message + COLORS["DEFAULT"]

        return message


formatter = ColoredFormatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)

track.addHandler(handler)

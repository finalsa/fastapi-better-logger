import logging

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[%dm"


class ColoredFormatter(logging.Formatter):

    COLORS = {
        logging.DEBUG: f"{COLOR_SEQ % (30 + BLUE)}",
        logging.INFO: f"{COLOR_SEQ % (30 + GREEN)}",
        logging.WARNING: f"{COLOR_SEQ % (30 + YELLOW)}",
        logging.ERROR: f"{COLOR_SEQ % (30 + RED)}",
        logging.CRITICAL: f"{COLOR_SEQ % (30 + MAGENTA)}",
    }

    def __init__(self, fmt, use_color=True):
        super().__init__(fmt)

        self.use_color = use_color

    def format(self, record: logging.LogRecord) -> str:
        levelname_color = f"{self.COLORS[record.levelno]}{record.levelname}{RESET_SEQ}"
        record.levelname = levelname_color
        return logging.Formatter.format(self, record)

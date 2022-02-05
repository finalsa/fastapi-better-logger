from typing import List
from logging import Handler, Logger

def add_handlers_to_loggers(loggers: List[Logger], handler: Handler):
    try:
        for logger_helper in loggers:
            for handler in logger_helper.handlers:
                logger_helper.removeHandler(handler)
            logger_helper.addHandler(DefaultLogger.get_handler_logger(settings))
    except Exception as ex:
        logger.exception(ex)
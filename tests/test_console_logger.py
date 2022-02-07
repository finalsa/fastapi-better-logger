import logging
import sys 
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi_better_logger.formatters import(
    ColoredFormatter, ColoredAccessFormatter
)


logger = logging.Logger(__name__)
handler = logging.StreamHandler()

def log_from_logger(args:dict= {}):
    global logger
    logger.debug("", "GET",  "/",  "HTTP/1.1",  20)
    logger.info("", "GET",  "/",  "HTTP/1.1",  20)
    logger.warning("", "GET",  "/",  "HTTP/1.1",  20)
    logger.error("", "GET",  "/",  "HTTP/1.1",  20)
    logger.critical("", "GET",  "/",  "HTTP/1.1",  20)


def log_from_logger_na():
    global logger
    logger.debug("Debug message ", )
    logger.info("Info message",  )
    logger.warning("Warning message", )
    logger.error("Error message", )
    logger.critical("Critical ", )

handler.setFormatter(ColoredFormatter('%(levelprefix)s %(message)s (%(filename)s:%(lineno)d)'))
logger.addHandler(handler)

log_from_logger_na()

handler.setFormatter(ColoredFormatter('%(levelprefix)s %(message)s [%(filename)s:%(lineno)d]'))

log_from_logger_na()


handler.setFormatter(ColoredAccessFormatter('%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'))


log_from_logger({})


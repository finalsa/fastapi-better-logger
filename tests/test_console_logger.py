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
    logger.debug("Debug message ", args)
    logger.info("Info message",  args)
    logger.warning("Warning message", args)
    logger.error("Error message", args)
    logger.critical("Critical ", args)


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




log_from_logger({"client_addr" :  "ssaaaa", "method" : "GET", "full_path" : "/", "http_version" : "1.1", "status_code" : 200})


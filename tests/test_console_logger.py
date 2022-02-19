import logging

from fastapi_better_logger import(
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


def test_logger_console():
    handler.setFormatter(ColoredFormatter('%(levelprefix)s %(message)s (%(filename)s:%(lineno)d)'))
    logger.addHandler(handler)

    log_from_logger_na()
    assert len(logger.handlers) == 1
    handler.setFormatter(ColoredFormatter('%(levelprefix)s %(message)s [%(filename)s:%(lineno)d]'))

    log_from_logger_na()


    handler.setFormatter(ColoredAccessFormatter('%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'))

    log_from_logger({"client_addr" :  "ssaaaa", "method" : "GET", "full_path" : "/", "http_version" : "1.1", "status_code" : 200})


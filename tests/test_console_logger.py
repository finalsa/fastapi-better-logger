import logging
import sys 
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi_better_logger.formatters import(ColoredFormatter)


logger = logging.Logger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter('%(levelprefix)s %(message)s'))
logger.addHandler(handler)

logger.debug("debug message",  )
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical ")


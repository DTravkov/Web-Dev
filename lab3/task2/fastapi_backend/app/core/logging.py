import logging
import sys

from core.config import settings

#logging.
def setup_logging() -> None:
     
    logging.getLogger("httpx").setLevel("CRITICAL") #disable httpx nasty logging
    format_string = "[%(asctime)s] [%(levelname)s /%(name)s] %(message)s"

    log_formatter = logging.Formatter(format_string, 
                                  datefmt='%d/%m/%y %H:%M:%S')
    
    level = logging.DEBUG if settings.DEBUG else logging.INFO


    file_handler = logging.FileHandler("../database/.log")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(level)

    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(level)

    root_logger = logging.getLogger('root')
    root_logger.setLevel(level)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)

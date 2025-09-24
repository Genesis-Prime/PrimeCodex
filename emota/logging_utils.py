import logging
import os
try:
    from pythonjsonlogger import jsonlogger
except ImportError:  # pragma: no cover
    jsonlogger = None


def configure_logger(name: str = "primecodex", level: str = "INFO", json_mode: bool = False):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    handler = logging.StreamHandler()
    if json_mode and jsonlogger:
        fmt = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    else:
        fmt = logging.Formatter("[%(asctime)s] %(levelname)s %(name)s: %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
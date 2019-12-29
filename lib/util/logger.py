import logging

# LOG_FORMAT = "(%(filename)s:%(lineno)d) %(message)s"
LOG_FORMAT = "%(message)s"

def init_logger():
  logging.basicConfig(format=LOG_FORMAT)
  logger = logging.getLogger("logger")
  logger.setLevel(20)
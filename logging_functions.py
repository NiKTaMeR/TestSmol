import logging

def setup_logger():
    logger = logging.getLogger("SaaS Metrics Calculator")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("saas_metrics_calculator.log")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)

def log_warning(message):
    logger.warning(message)
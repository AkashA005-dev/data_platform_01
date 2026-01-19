## Centralized Logger

import logging
from datetime import datetime
import os

def get_logger(name):
    os.makedirs("logs",exist_ok=True)

    log_file = f"logs/pipeline_{name}-{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s "
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


<<<<<<< HEAD
# src/pipeline/utils.py

"""
Utility functions for pipeline scripts.
Add helper functions here to reuse across modules.
"""

import logging

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """Setup logger with file output and console."""
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console)

    return logger
=======
# src/pipeline/utils.py

"""
Utility functions for pipeline scripts.
Add helper functions here to reuse across modules.
"""

import logging

def setup_logger(name: str, log_file: str, level=logging.INFO):
    """Setup logger with file output and console."""
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.addHandler(console)

    return logger
>>>>>>> 804fdd5ffc11025b1a7a4ad3a77889966f0e7142

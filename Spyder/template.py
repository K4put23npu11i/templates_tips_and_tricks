# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import logging
from datetime import datetime

# Configure logging
easy_logging = True
if easy_logging is True:
    # Configure logging
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(funcName)s: %(message)s")
else:
    logger = logging.getLogger()
    # create file handler which logs even debug messages
    fh = logging.FileHandler(str(__file__.split('/')[-1].split('.')[0]) + '.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s [%(funcName)s]: %(message)s', "%Y-%m-%d %H:%M:%S")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh) 
    logger.setLevel(logging.DEBUG)

# Measure running time:
start_time = datetime.now()
logger.info('Script started successfully!')


def main():
    """
    Main function to call all other functions in a specific order
    """
    
    return None


if __name__ == "__main__":
    main()


# Measure running time:
end_time = datetime.now()
logger.info('End of Script!')
logger.debug('Runtime of script: {}'.format(end_time - start_time))
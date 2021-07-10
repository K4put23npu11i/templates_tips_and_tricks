import logging
import FancyThings


logger = logging.getLogger()


def main():
    
    # create file handler which logs even debug messages
    fh = logging.FileHandler('Main.log')
    fh.setLevel(logging.DEBUG)
    
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s [%(module)s]: %(message)s',
                                  "%Y-%m-%d %H:%M:%S")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    


    logger.debug('debug message - Level 10')
    logger.info('info message - Level 20')
    logger.warning('warn message - Level 30')
    logger.error('error message - Level 40')
    logger.critical('critical message - Level 50')
    
    # Call another module
    FancyThings.fancy_stuff_doing()
    
    print('Print: Ende')



"""
Hinweise zum Logging - Level
von: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

DEBUG:
    ausführliche Details, internal state of loops, ...
    
INFO:
    handling requests or server state changed
    
WARNING:
    needs your attention, but not an error
    user attempts to log in with a wrong password
    
ERROR:
    exception is thrown, IO operation failure or connectivity issue
    
CRITICAL:
    something horrible happens
    out of memory, the disk is full or a nuclear meltdown

"""

if __name__ == '__main__':
    main()
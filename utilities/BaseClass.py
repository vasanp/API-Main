
import logging
import inspect

#baseclass for common utilities
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]

        # create logger with 'spam_application'
        logger = logging.getLogger(loggerName)

        # create file handler which logs even debug messages
        fileHandler = logging.FileHandler('/Users/vasanp/PycharmProjects/pythonProject/API_MainAssignment/Logs/logfile.log')

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s--||--%(levelname)s-||-%(name)s--||--%(funcName)s--||--%(message)s')
        fileHandler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger
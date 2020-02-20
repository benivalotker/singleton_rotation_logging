#/path/path/
#title           :Singleton Rotation Logging Class
#description     :rotation logging create log file with rotation backup file.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :veriosn 1.0 - singleton class.
#python_version  :3.6  
#==============================================================================
\
import os
import time
import logging
import config
from logging.handlers import RotatingFileHandler


'''
Singleton Pattern:
    - can create only one instance from this object
    - use this object globally
'''
class RotatingLog():
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if RotatingLog.__instance == None:
            RotatingLog()
        return RotatingLog.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if RotatingLog.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RotatingLog.__instance = self

            # create folder and log by server OS
            if os.name == "nt":
                if not os.path.exists(config.win_log_path):
                    os.mkdir(config.win_log_path)

                log_path = config.win_log_path
            else:
                if not os.path.exists(config.unix_log_path):
                    os.mkdir(config.unix_log_path)
                    
                log_path = config.unix_log_path

            # initial logging class
            self.logger = logging.getLogger(config.log_title)

            # set rotatating handler setting
            handler = RotatingFileHandler(log_path + config.file_name, maxBytes=config.file_size , backupCount=config.file_num)

            # rotatating log format.
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # logging level
            self.logger.setLevel(config.log_level)

            # set handler
            self.logger.addHandler(handler)

    
    def info(self, info_text):
        self.logger.info(info_text)
    
    
    def error(self, error_text):
        self.logger.error(error_text)

    
    def debug(self, debug_text):
        self.logger.debug(debug_text)

    
    def warning(self, warning_text):
        self.logger.warning(warning_text)

    
    def critical(self, critical):
        self.logger.critical(critical)


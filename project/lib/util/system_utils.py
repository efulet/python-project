"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import sys

# http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
import logging
import logging.config

from file_utils import FileUtils

class SystemUtils:
    """Define methods for configuring the system environment"""
    PROGRAM_NAME = "project"
    
    def __init__(self):
        pass
    
    def check_version_2_7(self):
        if sys.version_info[:2] != (2, 7):
            raise Exception("It seems python v2.7 is not installed on your system")
    
    def configure_log(self):
        logging.config.dictConfig({
            'version': 1,              
            'disable_existing_loggers': False,
        
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level':'INFO',    
                    'class':'logging.StreamHandler',
                },  
            },
            'loggers': {
                '': {                  
                    'handlers': ['default'],        
                    'level': 'INFO',  
                    'propagate': True  
                }
            }
        })
        
        logger = logging.getLogger(self.PROGRAM_NAME)
        
        handler = logging.FileHandler(FileUtils().log_file())
        handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        return logger

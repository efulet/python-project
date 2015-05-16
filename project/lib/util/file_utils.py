"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import os


class FileUtils:
    """Define a simple class with useful methods for handling files"""
    LOG_BASE_DIR_NAME = "log"
    LOG_FILENAME = "project.log"
    
    def __init__(self):
        pass
    
    def do_path(self, paths=[]):
        if not paths:
            raise Exception("There is no paths to join")
        return os.path.join(*paths)
    
    def log_path(self):
        pathfile = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(pathfile, "..", "..", "..", self.LOG_BASE_DIR_NAME)
    
    def log_file(self):
        return os.path.join(self.log_path(), self.LOG_FILENAME)

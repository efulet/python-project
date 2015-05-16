"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


class KlassException(Exception):
    """Define an exception class for customizing errors"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from klass_exception import KlassException


class Klass:
    """Define a sample class"""
    
    def __init__(self):
        pass
    
    def new_method(self):
        raise KlassException("Not implemented yet")
    
    def __str__(self):
        return "Define a string representation for this class"

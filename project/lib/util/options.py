"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from argparse import ArgumentParser


class Options:
    """Define options for this project"""
    def __init__(self):
        self.parser = ArgumentParser(usage='python project.py')
        self._init_parser()
    
    def _init_parser(self):
        self.parser.add_argument("-v", dest="verbose",
                                 action='store_true',
                                 help="verbose")
    
    def parse(self, args=None):
        return self.parser.parse_args(args)
    
    def print_help(self):
        self.parser.print_help()

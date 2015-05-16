"""
==========================
Skeleton Project Directory
==========================

This defines a basic structure of your skeleton directory.

@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import sys

from lib.util import Options, SystemUtils
from lib.module import Klass


def main(args):
    try:
        # Parse options
        options = Options()
        parse_args = options.parse(args[1:])
        
        # Configure logging
        logger = SystemUtils().configure_log()
        
        logger.info(__doc__)
        options.print_help()
        
        # Instance Klass sample
        my_klass = Klass()
        my_klass.new_method()
        
        return 0
    except Exception, err:
        logger.error(str(err), exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

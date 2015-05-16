#!/bin/bash


# Script for running your project
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>

BINPATH=`dirname $0`

python ${BINPATH}/../project/project.py "$@"

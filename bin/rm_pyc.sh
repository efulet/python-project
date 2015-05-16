#!/bin/bash


# Script for removing *.pyc
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>

BINPATH=`dirname $0`

find ${BINPATH}/../project -type f -name '*.pyc' -delete

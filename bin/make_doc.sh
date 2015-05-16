#!/bin/bash


# Script for generating docs using Sphinx
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>

if ! which sphinx-build >/dev/null
then
  echo "It seems Sphinx is not installed on your system"
  exit 1
fi

BINPATH=`dirname $0`

cd ${BINPATH}/../docs && make html

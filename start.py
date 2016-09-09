#!/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: start.py
# Author: billowqiu
# mail: billowqiu@163.com
# Created Time: 2016-09-09 15:46:20
# Last Changed: 2016-09-09 15:47:36
#########################################################################
import re
import sys
from graphite_beacon.app import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(run())

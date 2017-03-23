#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def do_map(record):
    data = record.split(",")
    yield data[2].strip(), data[4].strip()


for line in sys.stdin:
    for key, value in do_map(line):
        print '%s\t%s' % (key,value)
        

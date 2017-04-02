#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def do_map(line):
    data = line.split("\t")

    #trying to convert types
    ts = user = url = ""
    try:
        user = long(data[0].strip())
        ts = long(float(data[1].strip())*1000)
        url = data[2].strip()
    except:
        return

    if (url and user and ts):
        print '{}\t1'.format(url)
    else:
        return

for line in sys.stdin:
    do_map(line)

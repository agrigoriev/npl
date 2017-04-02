#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def do_reduce(key, values):
    return key, sum(values)

prev_key = None
values = []

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    if key != prev_key and prev_key is not None:
        result_key, result_value = do_reduce(prev_key, values)
        print '%s\t%s' % (result_key,result_value)
        values = []
    prev_key = key
    values.append(int(value))

if prev_key is not None:
    result_key, result_value = do_reduce(prev_key, values)
    print '%s\t%s' % (result_key,result_value)

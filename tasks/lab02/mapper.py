#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import happybase


#trying to connect to Hbase and create table if it doesn't exist
try:
    connection = happybase.Connection('node2.newprolab.com')
    connection.open()
    if "alexey.grigoriev" not in connection.tables():
        table = connection.create_table('alexey.grigoriev', {'data': dict(max_versions=4096)})
    else:
        table = connection.table('alexey.grigoriev')
except Exception as e:
    print "Error in DB connection"
    raise

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

    #pushing record to DB
    if (url and user%256==194 and ts):
        table.put(str(user), {b"data:url": url}, ts)
    else:
        return

for line in sys.stdin:
    do_map(line)


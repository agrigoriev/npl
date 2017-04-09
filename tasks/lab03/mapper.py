#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urlparse
import urllib
import re


def url2domain(url):
   try:
       a = urlparse.urlparse(urllib.unquote(url.strip()))
       if (a.scheme in ['http','https']):
           b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
           if b is not None:
               return str(b).strip()
           else:
               return ''
       else:
           return ''
   except:
       return

domain_groups = {
    "1": [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru'],
    "2": [u'vk.com', u'mail.qip.ru', u'lk.ssl.mts.ru'],
    "3": [u'games.mail.ru', u'igrystrelyalki.ru', u'consol-games.net'],
    "4": [u'5ballov.qip.ru', u'mgimo.ru', u'referat.arxiv.uz']
    }

def do_map(record):
    data = record.split("\t")
    if len(data) < 3:
        return
    user = data[0].strip()
    domain = url2domain(data[2].strip())
    for gid,group in domain_groups.iteritems():
        if domain in group:
            print "{}\t{}".format(user,gid)

for line in sys.stdin:
    do_map(line)

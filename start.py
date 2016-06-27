# -*- coding: UTF-8 -*
import urllib2,os,conf
from os.path import basename
from urlparse import urlsplit

def url2name(url):
    return basename(urlsplit(url)[2])

def download(url):
    f = urllib2.urlopen(url)
    if not os.path.exists(conf.dir):
        os.mkdir(conf.dir)
    with open(conf.dir+'/'+url2name(url), 'wb') as code:
        code.write(f.read()) 

if __name__ == '__main__':
    for i in range(int(conf.start),int(conf.end)+1):
        print str(i)
        download(conf.url.replace('%s',conf.addZero(len(conf.start),str(i))))

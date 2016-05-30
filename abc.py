import hashlib
import os
import sys
import logging
import requests,time,re,zipfile
from bs4 import BeautifulSoup
PY_VERSION = sys.version_info[0]
if PY_VERSION == 2:
    import urllib2
if PY_VERSION == 3:
    import urllib.request


def get_hash(file_path):
    read_size = 64 * 1024
    with open(file_path, 'rb') as f:
        data = f.read(read_size)
        f.seek(-read_size, os.SEEK_END)
        data += f.read(read_size)
    return hashlib.md5(data).hexdigest()


def sub_downloader(file_path):
    try:
        root, extension = os.path.splitext(file_path)
        headers = {'User-Agent': 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/manojmj92/subtitle-downloader)'}
        url = "http://api.thesubdb.com/?action=download&hash=" + get_hash(file_path) + "&language=en"
        if PY_VERSION == 3:
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req).read()
        if PY_VERSION == 2:
            req = urllib2.Request(url, '', headers)
            response = urllib2.urlopen(req).read()
        with open(root + ".srt", "wb") as subtitle:
            subtitle.write(response)
    except:
    	a=1

def main():
    root, _ = os.path.splitext(sys.argv[0])
    for path in sys.argv:
        if os.path.isdir(path):
            for dir_path, _, file_names in os.walk(path):
                for filename in file_names:
                    file_path = os.path.join(dir_path, filename)
                    sub_downloader(file_path)
        else:
            sub_downloader(path)
    

if __name__ == '__main__':
    main()
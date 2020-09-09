#!/usr/bin/env python3

import unittest
import sys, requests
from you_get import *
from you_get.extractors import (
    imgur,
    magisto,
    youtube,
    missevan,
    acfun,
    bilibili,
    soundcloud,
    tiktok
)

class YouGetTests(unittest.TestCase):
    def test_magisto(self):
        magisto.download(
            'http://www.magisto.com/album/video/f3x9AAQORAkfDnIFDA',
            info_only=True
        )
 
 print(sys.version_info)
 print("Python 4 Beginners: \n")
 response1 = requests.get('https://channel9.msdn.com/Series/Intro-to-Python-Development?WT.mc_id=python-c9-niner')
 print(response1.text, end=' ')
 print("More Python 4 Beginners: \n")
 response2 = requests.get('https://channel9.msdn.com/Series/More-Python-for-Beginners')
 print(response2.text, end=' ')
 print("Even More Python 4 Beginners: \n")
 response3 = requests.get('https://channel9.msdn.com/Series/Even-More-Python-for-Beginners-Data-Tools')
 print(response3.text, end=' ')
 url = input("please type the website link of the video you want to download: \n")
 def download_videos(url):
     magisto.download(
         url,
         info_only=True
     )

if __name__ == '__main__':
    unittest.main()
    download_videos()

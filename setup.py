#!/usr/bin/env python3

from setuptools import setup, find_packages  

setup(  
 name = "python videos for beginners",  
 version = "1.0",  
 keywords = ("python", "python videos","python online","beginners"),  
 description = "python online videos for beginners",  
 long_description = "Probably the largest hurdle when learning any new programming language is simply knowing where to get started. This is why we decided to create this series about Python for Beginners. Even though we won't cover everything there is to know about Python in the course, we want to make sure we give you the foundation on programming in Python, starting from common everyday code and scenarios. At the end of the course, you'll be able to go and learn on your own, for example with docs, tutorials, or books.",  
 license = "Apache License 2.0",  
 
 url = "https://github.com/nickcafferry/Python-videos-for-beginners",  
 author = "Wei MEI",  
 author_email = "nickcafferry@gmail.com",  
 
 packages = find_packages('source'),  
 package_dir = {'' : 'source'},
 test_suite = 'tests',
 
 include_package_data = True,  
 platforms = "any",  
 install_requires = [],  
 zip_safe = True,
 
 scripts = [],  
 entry_points = {  
  'console_scripts': [  
   'test = test.help:main'  
  ]  
 }  
)  

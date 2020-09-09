#!/usr/bin/env python3

from setuptools import * 

PYTHON_REQUIRES = '>=3.0,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*'

SETUPTOOLS_KWARGS = {
    'install_requires': [
        'you-get',
        'requests',
    ],
    'zip_safe': False,
}

setup(  
 name = "python videos for beginners",  
 version = "1.0",  
 keywords = ["python", "python videos","python online","beginners"],  
 description = "python online videos for beginners",  
 long_description = "Probably the largest hurdle when learning any new programming language is simply knowing where to get started. This is why we decided to create this series about Python for Beginners. Even though we won't cover everything there is to know about Python in the course, we want to make sure we give you the foundation on programming in Python, starting from common everyday code and scenarios. At the end of the course, you'll be able to go and learn on your own, for example with docs, tutorials, or books.",  
 license = "Apache License 2.0",  
 
 url = "https://github.com/nickcafferry/Python-videos-for-beginners",  
 author = "Wei MEI",  
 author_email = "nickcafferry@gmail.com",  
 
 packages = ['source'],  
 ext_package = 'source',
 
 include_package_data = True,  
 platforms = "any",  
 classifiers = [],  
 zip_safe = False,
 
 scripts = [],  
 entry_points = {  
  'console_scripts': [  
   'test = test.help:main'  
  ]  
 }  
)  

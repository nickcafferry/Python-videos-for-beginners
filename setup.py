 1 from setuptools import setup, find_packages  
 2   
 3 setup(  
 4     name = "test",  
 5     version = "1.0",  
 6     keywords = ("test", "xxx"),  
 7     description = "eds sdk",  
 8     long_description = "eds sdk for python",  
 9     license = "MIT Licence",  
10   
11     url = "http://test.com",  
12     author = "test",  
13     author_email = "test@gmail.com",  
14   
15     packages = find_packages(),  
16     include_package_data = True,  
17     platforms = "any",  
18     install_requires = [],  
19   
20     scripts = [],  
21     entry_points = {  
22         'console_scripts': [  
23             'test = test.help:main'  
24         ]  
25     }  
26 )  

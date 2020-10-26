|Deployment Status|  |Apache License|  |Documentation Status|  |Python Online|  |Python version|  |--|  |today| 

-------------------

.. |Deployment Status| image:: https://github.com/nickcafferry/Python-videos-for-beginners/workflows/deploy/badge.svg
   :target: https://github.com/nickcafferry/Python-videos-for-beginners/runs/1054191359?check_suite_focus=true
.. |Documentation Status| image:: https://readthedocs.org/projects/python-videos-for-beginners/badge/?version=latest
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/?badge=latest
.. |Apache License| image:: https://img.shields.io/github/license/nickcafferry/Python-videos-for-beginners
   :target: https://github.com/nickcafferry/Python-videos-for-beginners/blob/master/LICENSE
.. |Python version| image:: https://img.shields.io/badge/python-3.7,%203.8-brightgreen.svg
   :target: https://www.python.org/
.. |Python Online| image:: https://img.shields.io/badge/platform-python%20online-blue
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/pyonlineindex.html

.. |--| unicode:: U+02014 .. em dash
   :trim:

Copyright |copy| Wei MEI, |MLMS (TM)| |---|
all rights reserved. 
|bamboo|

.. |copy| unicode:: 0xA9 .. copyright sign
.. |MLMS (TM)| unicode:: MLMS U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

.. |bamboo| unicode:: 0x1F024 .. bamboo

Overview
====================

Getting started with a new environment can be challenging, especially when you literally don't even speak the language. Fortunately, we created a set of videos to help get you up and running with the language, so you can focus on the task at hand - learning how to create applications using Python.

We don't dig into specific frameworks, but we help get you ready to start exploring on your own. We'll show you the core Python concepts you'll need as you begin your journey into web development on popular frameworks such as `Django <https://djangoproject.com>`_ and `Flask <https://flask.palletsprojects.com/en/1.1.x/>`_, use AI services such as `Cognitive Services <https://azure.microsoft.com/services/cognitive-services/>`_, or even machine learning.

print
------

.. toctree::
   :maxdepth: 5

   python-for-beginners/02 - Print/index

comments
---------
.. toctree::
   :maxdepth: 5

   python-for-beginners/03 - Comments/index

string variables
----------------

.. toctree::
   :maxdepth: 5


   python-for-beginners/04 - String variables/index


What you'll learn
===================

- The basics of Python
- Starting a project
- Common syntax
- Package management

numeric variables
-----------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/05 - Numeric variables/index

dates
------------

.. toctree::
   :maxdepth: 5


   python-for-beginners/06 - Dates/index


What we don't cover
===================

- Class design and inheritance
- Asynchronous programming
- Basics of programming

error handling
--------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/07 - Error handling/index
   
handling conditions
-----------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/08 - Handling conditions/index

handling multiple conditions
----------------------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/09 - Handling multiple conditions/index

Prerequisites
===============

- `An understanding of Git <https://git-scm.com/book/en/v1/Getting-Started>`_
- Light experience with another programming language, such as `JavaScript <https://www.edx.org/course/javascript-introduction>`_


complex condition checks
------------------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/10 - Complex conditon checks/index


collections
------------------

.. toctree::
   :maxdepth: 5
   
   python-for-beginners/11 - Collections/index
   

Next steps
===========

As the goal of this course is to help get you up to speed on Python so you can work through a quick start, the next step after completing the videos is to follow a tutorial! Here's a few of our favorites:

- `Quickstart: Detect faces in an image using the Face REST API and Python <https://docs.microsoft.com/azure/cognitive-services/face/QuickStarts/Python?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner>`_
- `Quickstart: Analyze a local image using the Computer Vision REST API and Python <https://docs.microsoft.com/azure/cognitive-services/computer-vision/quickstarts/python-disk?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner>`_
- `Quickstart: Using the Python REST API to call the Text Analytics Cognitive Service <https://docs.microsoft.com/azure/cognitive-services/Text-Analytics/quickstarts/python?WT.mc_id=python-c9-niner?WT.mc_id=python-c9-niner>`_
- `Tutorial: Build a Flask app with Azure Cognitive Services <https://docs.microsoft.com/azure/cognitive-services/translator/tutorial-build-flask-app-translation-synthesis?WT.mc_id=python-c9-niner>`_
- `Flask tutorial in Visual Studio Code <https://code.visualstudio.com/docs/python/tutorial-flask?WT.mc_id=python-c9-niner>`_
- `Django tutorial in Visual Studio Code <https://code.visualstudio.com/docs/python/tutorial-django?WT.mc_id=python-c9-niner>`_


loops
------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/12 - Loops/index

functions
-------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/13 - Functions/index

function parameters
------------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/14 - Function parameters/index

packages
-------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/15 - Packages/index

calling APIs
--------------

.. toctree::
   :maxdepth: 5

   python-for-beginners/16 - Calling APIs/index
   
json
---------

.. toctree::
   :maxdepth: 5

   python-for-beginners/17 - JSON/index

decorators
-----------

.. toctree::
   :maxdepth: 5

   python-for-beginners/18 - Decorators/index

Introducing Python
======================

Before you get started on your journey towards learning Python, it's important to know why! We'll talk through what Python is, where you'll use it, and how it can help you problem solve.


.. raw:: html

    <video poster="_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w6.huya.com/2022/344485830/yuanhua/c8fe293f2aaecb29b2d608def201d9aa.mp4" type="video/mp4">
    </video>

Getting started
============

Now that we know about Python, the next question is, how do we get started? Well, the first thing that we're going to need is somewhere for Python to run.

Python is an interpreted language, so you will need a runtime in which Python can execute. Fortunately, all that you need to do is head on over to Python.org/downloads and you can go ahead and grab it from there.

.. raw:: html

    <video poster="_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w10.huya.com/2022/344487200/yuanhua/c9b95fb279267491745053a7628b17f2.mp4" type="video/mp4">
    </video>


Configuring Visual Studio Code
==================================

So previously, we took a look at the three things that we're going to need to actually start doing our Python code. We'll need somewhere for our Python code to run.

We'll need something to edit it with, VS Code in our case, and then we'll need an extension for a VS Code. Now those first two, Python and VS Code itself,
you'll install the same way that you are going to install anything else onto
your operating system.

.. raw:: html

    <video poster="_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w20.huya.com/2022/344490820/yuanhua/0cb0b983df988425c7ce85d3dc6c5994.mp4" type="video/mp4">
    </video>

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="_static/P4All_Lecture2/main.html"></iframe>

        </div>


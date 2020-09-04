|Deployment Status|  |Apache License|  |Documentation Status|  |Python Online|  |Python version|  |--|  |today| 

-------------------

.. |Deployment Status| image:: https://github.com/nickcafferry/Python-videos-for-beginners/workflows/deploy/badge.svg
   :target: https://github.com/nickcafferry/Python-videos-for-beginners/runs/1054191359?check_suite_focus=true
.. |Documentation Status| image:: https://readthedocs.org/projects/python-videos-for-beginners/badge/?version=latest
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/?badge=latest
.. |Apache License| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg?style=flat)
   :target: http://www.apache.org/licenses/LICENSE-2.0
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

Strings
==============

Python can store and manipulate strings. Strings can be enclosed in single or double quotes. There are a number of string methods you can use to manipulate and work with strings

- `strings <https://docs.python.org/3/tutorial/introduction.html#strings>`_
- `string methods <https://docs.python.org/3/library/stdtypes.html#string-methods>`_

.. literalinclude:: strings_in_variables.py
   :language: python
   :linenos:

Converting to string values

.. literalinclude:: string_functions.py 
   :language: python
   :linenos:

- `str <https://docs.python.org/3/library/functions.html#func-str>`_

When naming variables follow the PEP-8 Style Guide for Python Code

- `PEP-8 Style Guide <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_

.. literalinclude:: format_strings.py
   :language: python
   :linenos:

.. literalinclude:: combine_strings.py
   :language: python
   :linenos:

String Concepts
================

Let's get in and take a look at probably one of the most common things that you'll be doing in programming, and that is working with strings.
Now, when it comes to strings and actually just variables in Python, it's relatively straightforward to take a string and store it inside of a variable.

Now as a real quick aside, if you're not already familiar with variables, variables windup acting as placeholders inside of your code for some values.

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w21.huya.com/2022/344499848/yuanhua/b2a3b82de7a64afb08ee5ddeeee9f903.mp4" type="video/mp4">
    </video>

Demo: Strings
=============

So let's take a look at some of those neat little string functions that we saw previously.

So I'm going to start off by just simply typing in first_name equals Christopher, we'll just skip that stored, and then last_name, equals Harrison.

Perfect. Now, like we have already seen, we can concatenate things together by using that plus sign. So if I say "Print" and I say "first_name," and by the way, a little IntelliSense Beta functionality for you.

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w20.huya.com/2022/344510334/yuanhua/236f68b8914c7c3c3a829c20f8a8d582.mp4" type="video/mp4">
    </video>

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture5/main.html"></iframe>

        </div>

Challenges time
=================

Check the following script and try to find the mistake:

.. literalinclude:: code_challenge.py
   :language: python
   :linenos:

solutions:

.. literalinclude:: code_challenge_solution.py
   :language: python
   :linenos:

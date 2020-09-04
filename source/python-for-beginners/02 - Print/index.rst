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

print
======

The print function allows you to send output to the terminal：

.. py:function:: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
   
   Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.
   
   All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.
   
   The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.
   
   Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.
   
   Changed in version 3.3: Added the flush keyword argument.

.. literalinclude:: hello_world.py
   :language: python
   :linenos:

Find more details on  `print <https://docs.python.org/3/library/functions.html#print>`_.

.. literalinclude:: print_blank_line.py 
   :language: python
   :linenos:

Strings can be enclosed in single quotes or double quotes

- "this is a string"
- 'this is also a string'

.. literalinclude:: single_or_double_quotes.py
   :language: python
   :linenos:

input
======

The input function allows you to prompt a user for a value：

.. py:function:: input([prompt])

   If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
   
   >>> s = input('--> ')  
   --> Monty Python's Flying Circus
   >>> s  
   "Monty Python's Flying Circus"
   
   If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.
   
   Raises an auditing event builtins.input with argument prompt before reading input

   Raises an auditing event builtins.input/result with the result after successfully reading input.

.. literalinclude:: ask_for_input.py
   :language: python
   :linenos:

Find more details on `input <https://docs.python.org/3/library/functions.html#input>`_.
  
Parameters:

- `prompt`: Message to display to the user  

return value:

- string value containing value entered by user

Challenges time
=================

There are some challenges you can try to take:

.. literalinclude:: coding_challenge.py 
   :language: python
   :linenos:

solutions:

.. literalinclude:: coding_challenge_solution.py 
   :language: python
   :linenos:

Introducing Python
======================

Before you get started on your journey towards learning Python, it's important to know why! We'll talk through what Python is, where you'll use it, and how it can help you problem solve.


.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w21.huya.com/2022/344494668/yuanhua/da4a1524c70e108d480399bb1670aabb.mp4" type="video/mp4">
    </video>


PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture3/main.html"></iframe>

        </div>

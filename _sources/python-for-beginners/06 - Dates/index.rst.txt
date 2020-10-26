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

Date
==============

The `datetime module <https://docs.python.org/3/library/datetime.html>`_ contains a number of classes for manipulating dates and times.

.. automodule:: datetime
   :members:
   :undoc-members:
   :show-inheritance:

Date and time types:

- `date` stores year, month, and day
- `time` stores hour, minute, and second
- `datetime` stores year, month, day, hour, minute, and second
- `timedelta` a duration of time between two dates, times, or datetimes

When naming variables follow the PEP-8 Style Guide for Python Code

- `PEP-8 Style Guide <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_

Converting from string to datetime

- `strptime <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_

.. autofunction:: datetime.datetime.strptime
   :members:
   :undoc-members:
   :show-inheritance:   
   

Date data types
================


.. literalinclude:: date_functions.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w21.huya.com/2023/344517370/yuanhua/bfd1a260bddd958583415f4b84d1ab65.mp4" type="video/mp4">
    </video>

.. literalinclude:: format_date.py
   :language: python
   :linenos:

Demo: dates
=============


.. literalinclude:: get_current_date.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w21.huya.com/2023/344519832/yuanhua/e1e19e1747a980581472708c6c1a5c47.mp4" type="video/mp4">
    </video>

.. literalinclude:: input_date.py
   :language: python
   :linenos:

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture7/main.html"></iframe>

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


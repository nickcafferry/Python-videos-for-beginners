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

Error Handling
==============

Error handling in Python is managed through the use of `try/except/finally <https://docs.python.org/3.7/reference/compound_stmts.html#except>`_

Python has numerous `built-in exceptions <https://docs.python.org/3.7/library/exceptions.html>`_. When creating `except` blocks, they need to be created from most specific to most generic according to the `hierarchy <https://docs.python.org/3.7/library/exceptions.html#exception-hierarchy>`_.


Date data types
================


.. literalinclude:: syntax.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w20.huya.com/2023/344537804/yuanhua/6d9febed495843b58fbbd3b1ac086454.mp4" type="video/mp4">
    </video>

.. literalinclude:: runtime.py 
   :language: python
   :linenos:

Demo: dates
=============


.. literalinclude:: logic.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w10.huya.com/2023/344535278/yuanhua/c6a9f01a1e0360df7dabbedf4b56bc39.mp4" type="video/mp4">
    </video>

.. literalinclude:: input_date.py
   :language: python
   :linenos:

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture8/main.html"></iframe>

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


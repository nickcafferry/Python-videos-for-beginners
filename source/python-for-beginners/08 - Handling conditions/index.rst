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

Handling conditions
===================

Conditional execution can be completed using the `if <https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>`_ statement

`if` syntax

.. code:: python
  
    >>> if expression:
    # code to execute
    >>> else:
    # code to execute
    ```
    
`Comparison operators <https://docs.python.org/3/library/stdtypes.html#comparisons>`_

- < less than
- < greater than
- == is equal to
- \>= greater than or equal to
- <= less than or equal to
- != not equal to


.. literalinclude:: comparing_strings.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w21.huya.com/2023/344540624/yuanhua/561e0e6fab1e21e84b6f2303a04dafad.mp4" type="video/mp4">
    </video>

.. literalinclude:: check_tax.py 
   :language: python
   :linenos:

Demo: dates
=============


.. literalinclude:: case_insensitive_comparisons.py
   :language: python
   :linenos:

.. raw:: html

      <iframe src="https://channel9.msdn.com/Series/Intro-to-Python-Development/Python-for-Beginners-20-of-44-Demo-Conditional-Logic/player?format=html5#ccLang=en" width="690" height="402" allowFullScreen frameBorder="0" title="Python for Beginners [20 of 44] Demo: Conditional Logic - Microsoft Channel 9 Video"></iframe>

.. literalinclude:: add_else.py
   :language: python
   :linenos:


.. literalinclude:: add_else_different_indentation.py
   :language: python
   :linenos:

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture9/main.html"></iframe>

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


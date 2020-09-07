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

Complex condition checks
=============================

Conditional execution can be completed using the `if <https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>`_ statement.

`if` syntax

.. code:: python
    
    
    >>> if expression:
            # code to execute
        elif expression:
            # code to execute
        else:
            # code to execute
        ```

`Boolean values <https://docs.python.org/3/library/stdtypes.html#boolean-values>`_ can be either `False` or `True`

`Boolean operators <https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not>`_

- **x *or* y** - If either x **OR** y is true, the expression is executed
- **x *and* y** - If x **AND** y are both true, the expression is executed

`Comparison operators <https://docs.python.org/3/library/stdtypes.html#comparisons>`_

- < less than
- < greater than
- == is equal to
- \>= greater than or equal to
- <= less than or equal to
- != not equal to
- **x *in* [a,b,c]** Does x match the value of a, b, or c


.. literalinclude:: using_and.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w6.huya.com/2023/344542000/yuanhua/3ab547e1b48ab0eae8232e2c07aca854.mp4" type="video/mp4">
    </video>

.. literalinclude:: use_in_statements.py
   :language: python
   :linenos:

Demo: dates
=============


.. literalinclude:: use_elif.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w10.huya.com/2023/344546610/yuanhua/a5c015437495ac5bf294b8fdabbf6fd1.mp4" type="video/mp4">
    </video>

.. literalinclude:: boolean_variables.py
   :language: python
   :linenos:


PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture11/main.html"></iframe>

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


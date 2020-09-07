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

Collections
==================

Collections are groups of items. Python supports several types of collections. Three of the most common are dictionaries, lists and arrays.

Lists
===============

`Lists <https://docs.python.org/3/tutorial/introduction.html#lists>`_ are a collection of items. Lists can be expanded or contracted as needed, and can contain any data type. Lists are most commonly used to store a single column collection of information, however it is possible to `nest lists <https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions>`_

Arrays
===============

`Arrays <https://docs.python.org/3/library/array.html>`_ are similar to lists, however are designed to store a uniform basic data type, such as integers or floating point numbers.

Dictionaries
===============

`Dictionaries <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_ are key/value pairs of a collection of items. Unlike a list where items can only be accessed by their index or value, dictionaries use keys to identify each item.


.. literalinclude:: ranges.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w10.huya.com/2023/344701112/yuanhua/9fa751bd82d75720c8a123db33e74f23.mp4" type="video/mp4">
    </video>

.. literalinclude:: lists.py
   :language: python
   :linenos:

Demo: dates
=============


.. literalinclude:: dictionaries.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="https://huya-w20.huya.com/2023/344701770/yuanhua/09db1befbbc09554558f5660691ed5b8.mp4" type="video/mp4">
    </video>

.. literalinclude:: common-operations.py
   :language: python
   :linenos:


PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture15/main.html"></iframe>

        </div>


.. literalinclude:: arrays.py
   :language: python
   :linenos:

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

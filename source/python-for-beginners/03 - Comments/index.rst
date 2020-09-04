|Deployment Status|  |Apache License|  |Documentation Status|  |Huawei Cloud|  |Python version|  |--|  |today| 

-------------------

.. |Deployment Status| image:: https://github.com/nickcafferry/Python-videos-for-beginners/workflows/deploy/badge.svg
   :target: https://github.com/nickcafferry/Python-videos-for-beginners/runs/1054191359?check_suite_focus=true
.. |Documentation Status| image:: https://readthedocs.org/projects/python-videos-for-beginners/badge/?version=latest
   :target: https://python-videos-for-beginners.readthedocs.io/en/latest/?badge=latest
.. |Apache License| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg?style=flat)
   :target: http://www.apache.org/licenses/LICENSE-2.0
.. |Python version| image:: https://img.shields.io/badge/python-3.7,%203.8-brightgreen.svg
   :target: https://www.python.org/
.. |Huawei Cloud| image:: https://img.shields.io/badge/platform-huawei%20cloud-blue
   :target: https://auth.huaweicloud.com/authui/login.html?service=https%3A%2F%2Fconsole.huaweicloud.com%2Fconsole%2F%3Flocale%3Dzh-cn#/login

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


Comments
========

Comments start with a hash character (#) and allow you to document your code. Comments are ignored when code is executed.

- `Comments <https://docs.python.org/3/reference/lexical_analysis.html?highlight=comment>`_

A comment starts with a hash character (#) that is not part of a string literal, and ends at the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax.


.. literalinclude:: comments_are_not_executed.py 
   :language: python
   :linenos:

.. literalinclude:: enable_pin.py 
   :language: python
   :linenos:

Challenges time
=================

Check the following script and try to find the mistake:

.. literalinclude:: comments_for_debugging.py 
   :language: python
   :linenos:

solutions:

.. literalinclude:: string_in_double_quotes.py
   :language: python
   :linenos:

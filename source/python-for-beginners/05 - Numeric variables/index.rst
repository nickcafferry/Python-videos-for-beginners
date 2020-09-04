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

Numeric values
===============

Python can store and manipulate numbers. Python has two types of numeric values: integers (whole numbers) or float (numbers with decimal places)

- `numeric types <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>`_

When naming variables follow the PEP-8 Style Guide for Python Code

- `PEP-8 Style Guide <https://www.python.org/dev/peps/pep-0008/#naming-conventions>`_

Converting to numeric values

- `int <https://docs.python.org/3/library/functions.html#int>`_

.. py:class:: int(x, base=10)

      Return an integer object constructed from a number or string x, or return 0 if no arguments are given. If x defines __int__(), int(x) returns x.__int__(). If x defines __index__(), it returns x.__index__(). If x defines __trunc__(), it returns x.__trunc__(). For floating point numbers, this truncates towards zero.
      
      If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in radix base. Optionally, the literal can be preceded by + or - (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35. The default base is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code. Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('010') is, as well as int('010', 8).
      
      The integer type is described in Numeric Types — int, float, complex.
      
      Changed in version 3.4: If base is not an instance of int and the base object has a base.__index__ method, that method is called to obtain an integer for the base. Previous versions used base.__int__ instead of base.__index__.
      
- `float <https://docs.python.org/3/library/functions.html#float>`_

.. py:class:: float([x])

      Return a floating point number constructed from a number or string x.
      
      If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be '+' or '-'; a '+' sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or a positive or negative infinity. More precisely, the input must conform to the following grammar after leading and trailing whitespace characters are removed:
      
      sign           ::=  "+" | "-"
      infinity       ::=  "Infinity" | "inf"
      nan            ::=  "nan"
      numeric_value  ::=  floatnumber | infinity | nan
      numeric_string ::=  [sign] numeric_value
      
      Here floatnumber is the form of a Python floating-point literal, described in Floating point literals. Case is not significant, so, for example, “inf”, “Inf”, “INFINITY” and “iNfINity” are all acceptable spellings for positive infinity.

      Otherwise, if the argument is an integer or a floating point number, a floating point number with the same value (within Python’s floating point precision) is returned. If the argument is outside the range of a Python float, an OverflowError will be raised.

      For a general Python object x, float(x) delegates to x.__float__(). If __float__() is not defined then it falls back to __index__().
      
      If no argument is given, 0.0 is returned.

      Examples:
      
      >>> float('+1.23')
      1.23
      >>> float('   -12345\n')
      -12345.0
      >>> float('1e-003')
      0.001
      >>> float('+1E6')
      1000000.0
      >>> float('-Infinity')
      -inf

- `complex <https://docs.python.org/3/library/functions.html#complex>`_

.. py:class:: complex([real[, imag]])
   
      Return a complex number with the value real + imag*1j or convert a string or number to a complex number. If the first parameter is a string, it will be interpreted as a complex number and the function must be called without a second parameter. The second parameter can never be a string. Each argument may be any numeric type (including complex). If imag is omitted, it defaults to zero and the constructor serves as a numeric conversion like int and float. If both arguments are omitted, returns 0j.

      For a general Python object x, complex(x) delegates to x.__complex__(). If __complex__() is not defined then it falls back to __float__(). If __float__() is not defined then it falls back to __index__().
      
     :note: When converting from a string, the string must not contain whitespace around the central + or - operator. For example, complex('1+2j') is fine, but complex('1 + 2j') raises ValueError.
     
     

Numeric Data Types
================

So now you've learned how to work with strings, let's take a look at how we work with numbers inside our Python code as well. Just like strings numbers can be stored inside variables.

We always want to give those variables nice meaningful names get in
the habit of that right away, and we can pass those variables into functions like the print statement.

So the print statement can take a variable that contains a string, a variable that contains a number.It really doesn't matter either way, it'll just print what it's received out onto the screen.

.. literalinclude:: print_pi.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w10.huya.com/2023/344527226/yuanhua/1f921801ca2bdd5067565ed634efd26d.mp4" type="video/mp4">
    </video>

.. literalinclude:: combining_strings_and_numbers.py
   :language: python
   :linenos:

Demo: Numbers
=============

So I've got Visual Studio open. Let's go and take a look at some code.
So I'm going to create my variable pi 14159 I know of is more digits
and app but I've gotta stop somewhere and I'm storing that value in a variable and then I can just print that value up on the screen using
control S to save here.

.. literalinclude:: doing_math.py
   :language: python
   :linenos:

.. raw:: html

    <video poster="../../_static/images/GCC.png" width="690" height="402" controls="controls">
        <source src="//huya-w6.huya.com/2023/344529278/yuanhua/86101ae7d8256d746ce076545bdf5827.mp4" type="video/mp4">
    </video>

.. literalinclude:: numbers_treated_as_strings.py
   :language: python
   :linenos:

PPT Demonstrations
===================

.. raw:: html

    <div class="slideshow">

            <iframe style="border: none; width: 100%; height: 402px" name="embedded_lecture1_anywhere" src="../../_static/P4All_Lecture6/main.html"></iframe>

        </div>

.. literalinclude:: convert_strings_to_numbers_for_math.py
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

